---
layout: post
title: "Terraform Rundown"
date: 2022-09-25 00:00:00 -0700
categories: Blog update
---

I want to show off some Terraform code, and how and why descisions were made in writing the project. This is to demonstrate some features of Terraform, as well as how I've used it for some local infrastructure. Again, Infrastructure as Code is all about following Patterns, one of which is relying on Primitives to exist, like a secret or user management service. That being said, we can define Primitives using IaC methods, which is an iterative pattern all of its own. 

## 1. Ansible for Configuration management
Use configuration management to put the configs in place. If using VMs or VPS instead of containers, this step may be hooked into differently, like during or after the build step of Terraform, but we can prestage our environment when Docker containers.
```
---
- hosts: "{{ targets }}"
  become: true
  become_method: sudo
  vars:
    - docker_path: "/pool2/docker"
    - containers: [glauth, haproxy, vault, wekan-app, wekan-db]
  tasks:
    - name: debian docker prereqs
      apt:
        name:
          - ca-certificates
          - gnupg
      when: "ansible_distribution == 'Debian'"
    - name: docker apt key
      apt_key:
        url: https://download.docker.com/linux/debian/gpg
        state: present
      when: "ansible_distribution == 'Debian'"
    - name: debian docker repo
      apt_repository:
        repo: "deb https://download.docker.com/linux/debian {{ ansible_distribution_release }} stable"
        state: present
      when: "ansible_distribution == 'Debian'"
    - name: docker ce repo centos
      yum_repository:
        name: docker
        description: docker-ce
        #    baseurl: https://download.docker.com/linux/centos/docker-ce.repo
        baseurl: "https://download.docker.com/linux/{{ansible_distribution|lower}}/{{ansible_distribution_major_version}}/x86_64/stable/"
      when: "ansible_distribution == 'CentOS'"
    - name: docker packages from repo
      package:
        name:
          - docker-ce
          - docker-ce-cli
          - containerd.io
          - docker-compose-plugin
        state: present
    - name: docker daemon config
      copy:
        src: "files/daemon.json"
        dest: "/etc/docker/daemon.json"
      notify: "restart docker daemon"
``` 
The above code installs and configures Docker. This is nice to have as configuration managed by code, as it will allow for the script to also act as a bootstrap, kicking everything into gear quickly, from nothing, in the same way. Docker is the application that iron serves, and the apps in the containers bear no relation to their iron any longer.

```
    - name: docker directories
      file:
        path: "{{docker_path}}/{{ item}}"
        state: directory
      with_items:
          - "{{containers}}"
    - name: vault config dir
      file:
        path: "{{docker_path}}/{{item}}/config"
        state: directory
      with_items:
        - "vault"
    - name: glauth config dir
      file:
        path: "{{docker_path}}/{{item}}/config"
        owner: "999"
        group: "999"
        state: directory
      with_items:
        - "glauth"    
    - name: wekan-app config dir
      file:
        path: "{{docker_path}}/{{item}}/files"
        owner: "999"
        group: "999"
        state: directory
      with_items:
        - "wekan-app"
    - name: haproxy config file
      copy:
        src: "files/{{item}}.cfg"
        dest: "{{docker_path}}/{{item}}/{{item}}.cfg"
      with_items:
        - "haproxy"
      notify: "restart docker container haproxy"
    - name: run terraform locally
      become: false
      connection: local
      local_action: "command terraform apply -auto-approve -target=docker_container.{{ item }}"
      args:
        chdir: "{{ terraform_path }}"
      with_items:
          - "{{ containers }}"
      register: tf_apply
      changed_when: "'1 added' in tf_apply.stdout" 

  handlers:
    - name: restart docker container haproxy
      docker_container:
        name: haproxy
        state: started
        restart: yes
    - name: restart docker daemon
      service:
        name: docker
        state: restarted
```
Continuing on, there are storage directories for the containers created and seeded. This works well as a single git project, with both ansible and terraform code. Terraform can be run individually, or with run on a schedule with ansible (remember, if you worry about the configuration management breaking things, you've done it wrong - its too fragile). 

That's a point this script needs to work on: it works well as a maintainance script, but there is an order to how it needs to be stood up. Other apps need the secret manager vault, which needs haproxy to be running in front of it, providing the shim from public subnets and SSL termination. You will see later how dependencies are built into the terraform code. 

## 2. Terraform Primitives
We need to give terraform the libraries needed to actuate our code for Docker, as well as how to access our Secrets (also through its own provider). Things like network and other variables are defined.
```
##PROVIDERS
terraform {
  required_providers {
     docker = {
       source = "kreuzwerker/docker"
     }
 }
}
provider "docker" {"
  host     = "ssh://user@host"
  ssh_opts = ["-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null"]
}
provider "vault" {
  address = "https://vault.bootingup.net"
  token = var.vault_token
}
##VARIABLES
variable "nat_subnet" {
  type = string
  default = "172.18.0.1/24"
}
variable "storage_path" {
  type = string
  default = "/pool2/docker"
}
variable "vault_addr" {
  type = string
  default = "172.18.0.14"
}
variable "vault_token" {
  type = string
  sensitive = true
}
##NETWORKS
resource "docker_network" "nat" {
  name = "bootingup.lan"
  driver = "bridge"
  ipam_config {
    gateway = "172.18.0.1"
    ip_range = var.nat_subnet
    subnet = var.nat_subnet
  }
}
##SECRETS
data "vault_generic_secret" "glauth" {
        path = "secret/glauth"
}
```
## 3. Docker containers

Below we define our containers, as well as how to run them. This is done in two steps, as we can have images saved without running them, so the provider takes this into account. The drawback I have found to this method is we run our images using a sha256sum for the id to use, even if we pull the latest for it; this means watchtower, or a cron script to pull latest and restart, would fail: that sha256sum will never change, as it is exact on the <code>docker run</code>-stype API call. We do it this way as otherwise, it pulled and ran the images too often; this way at least Terraform does a good job of managing state. 

```
##IMAGES
###vault
data "docker_registry_image" "vault" {
  name = "hashicorp/vault"
}
resource "docker_image" "vault" {
  name = data.docker_registry_image.vault.name
  pull_triggers = [data.docker_registry_image.vault.sha256_digest]
}
###vault
resource "docker_container" "vault" {
  name = "vault"
  image = docker_image.vault.latest
  restart = "always"
  capabilities {
    add = ["IPC_LOCK"]
  }
  lifecycle {
    create_before_destroy = false
  }
  env = ["VAULT_ADDR=http://${var.vault_addr}:8200", 
        "VAULT_UI=true",
        "VAULT_LOCAL_CONFIG={\"storage\": [{\"file\": {\"path\": \"/opt/vault/data\"}}], \"default_lease_ttl\": \"168h\", \"max_lease_ttl\": \"720h\", \"listener\": [{\"tcp\": {\"address\": \"${var.vault_addr}:8200\", \"tls_disable\": 1}}] }"]
  networks_advanced {
    name = docker_network.nat.name
    aliases = ["vault"]
    ipv4_address = "${var.vault_addr}"
  }
  volumes {
    container_path = "/vault/"
    host_path = "${var.storage_path}/vault"
  }
  volumes {
    container_path = "/opt/vault/data"
    host_path = "${var.storage_path}/vault/data"
  }
  command = ["server"]
}
###haproxy
data "docker_registry_image" "haproxy" {
  name = "haproxy"
}
resource "docker_image" "haproxy" {
  name = data.docker_registry_image.haproxy.name
  pull_triggers = [data.docker_registry_image.haproxy.sha256_digest]
}
###haproxy
resource "docker_container" "haproxy" {
  name = "haproxy"
  image = docker_image.haproxy.latest
  restart = "always"
  lifecycle {
    create_before_destroy = false
  }
  ports {
    internal = 80
    external = 80
    protocol = "tcp" 
  }
  ports {
    internal = 443
    external = 443 
    protocol = "tcp"
  }
  networks_advanced {
    name = docker_network.nat.name
    aliases = ["haproxy"]
    ipv4_address = "172.18.0.17"
  }
  mounts {
    target = "/usr/local/etc/haproxy/haproxy.cfg"
    source = "${var.storage_path}/haproxy/haproxy.cfg"
    type = "bind"
    read_only = true
  }
  mounts {
    target = "/usr/local/etc/haproxy/combined.pem"
    source = "${var.storage_path}/haproxy/combined.pem"
    type = "bind"
    read_only = true
  }
}
###wekan-db
data "docker_registry_image" "wekan-db" {
  name = "mongo:4"
}
resource "docker_image" "wekan-db" {
  name = data.docker_registry_image.wekan-db.name
  pull_triggers = [data.docker_registry_image.wekan-db.sha256_digest]
}
###wekan-app
data "docker_registry_image" "wekan-app" {
  name = "quay.io/wekan/wekan"
}
resource "docker_image" "wekan-app" {
  name = data.docker_registry_image.wekan-app.name
  pull_triggers = [data.docker_registry_image.wekan-app.sha256_digest]
}
###wekan-db
resource "docker_container" "wekan-db" {
  name = "wekan-db"
  image = docker_image.wekan-db.latest
  restart = "always"
  lifecycle {
    create_before_destroy = false
  }
  networks_advanced {
    name = docker_network.nat.name
    aliases = ["wekan-db"]
    ipv4_address = "172.18.0.22"
  }
  volumes {
    container_path = "/etc/localtime"
    host_path = "/etc/localtime"
    read_only = true
  }
  volumes {
    container_path = "/etc/timezone"
    host_path = "/etc/timezone"
    read_only = true
  }
  volumes {
    container_path = "/data/db"
    host_path = "${var.storage_path}/wekan-db/db"
  }
  volumes {
    container_path = "/dump"
    host_path = "${var.storage_path}/wekan-db/dump"
  }
}
###wekan-app
resource "docker_container" "wekan-app" {
  name = "wekan-app"
  image = docker_image.wekan-app.latest
  restart = "always"
  depends_on = [docker_container.wekan-db]
  lifecycle {
    create_before_destroy = false
      }
  env = [
		...
        ]
  networks_advanced {
    name = docker_network.nat.name
    aliases = ["wekan-app"]
    ipv4_address = "172.18.0.23"
  }
  volumes {
    container_path = "/etc/localtime"
    host_path = "/etc/localtime"
    read_only = true
 }
  volumes {
    container_path = "/data"
    host_path = "${var.storage_path}/wekan-app/files"
  }
}
```
Also note how no hard passcodes are installed, even in the vault config. Vault saves all the configs to disk (which is maintained out of bound, possibly from ansible), and everything else is a variable pulled at runtime, In theory, all secrets could be flushed at whim, after being changed centrally. With the right backend (doesn't have to be vault, keepass also has a provider), you could have autoexpiring tokens that change themselves when scheduled config managment happens.

This doesn't cover most of the issues I have with Terraform, just what I have found works; I hope that this gave some insight into how to run IaC right, and how limitless the possibilities are. 
