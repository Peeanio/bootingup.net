---
layout: post
title: "Terraform Working"
date: 2022-07-22 00:00:00 -0700
categories: Blog update
---

Progress on two fronts: I actually got keycloak working behind Haproxy, something that has eluded me on and off for months, and using Terraform to throw up the Docker containers with everything that is needed. It's nice to be able to run containers that are "tied" together without needing compose, or going as far overboard with k8s. Some things that needs some work would be to move away from strings in the resource definition and move towards using both common vars and security/password vaults. There is also a move towards DNS names and networks, but thats the next step. But here's the terraform:

```
terraform {
  required_providers {
     docker = {
       source = "kreuzwerker/docker"
     }
 }
}

provider "docker" {
  host     = "ssh://max@drake.bootingup.lan"
  ssh_opts = ["-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null"]
}

resource "docker_container" "keycloak_db" {
  name = "keycloak_db"
  image = "postgres:14"
  env = [
    "POSTGRES_PASSWORD=db",
    "POSTGRES_DB=keycloak",
    "PGDATA=/var/lib/postgresql/data/pgdata"
  ]
  networks_advanced {
    name = "bootingup.lan"
    aliases = ["keycloak_db"]
    ipv4_address = "172.18.0.10"
  }
  volumes {
     container_path = "/var/lib/postgresql/data"
     host_path = "/pool2/docker/keycloak_db"
  }
}

resource "docker_container" "keycloak_app" {
  name = "keycloak_app"
  image = "quay.io/keycloak/keycloak"
  env = [
    "KEYCLOAK_ADMIN=admin",
    "KEYCLOAK_ADMIN_PASSWORD=pass",
    "KC_DB=postgres",
    "KC_DB_URL=jdbc:postgresql://172.18.0.10:5432/keycloak",
    "KC_DB_USERNAME=postgres",
    "KC_DB_PASSWORD=db",
    "KC_PROXY=edge"
  ]
  command = ["start-dev"]
  networks_advanced {
    name = "bootingup.lan"
    aliases = ["keycloak_app"]
    ipv4_address = "172.18.0.9"
  }
}
```

And the Haproxy config:

```
frontend main
	mode http
	bind :80
	redirect scheme https code 301 

frontend ssl
	mode http
	bind :443 ssl crt /usr/local/etc/haproxy/combined.pem

	acl host_keycloak hdr(host) -i keycloak.bootingup.net
	use_backend keycloak if host_keycloak
	http-request set-header X-Forwarded-Proto https

backend keycloak
	balance roundrobin
	server keycloak 172.18.0.9:8080 check

```

The things that tipped these off were to use `http-request set-header X-Forwarded-Proto https` in haproxy and `KC_PROXY=edge` in keycloak.
