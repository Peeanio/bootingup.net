---
layout: post
title: "IAC Epiphanies"
date: 2022-07-30 00:00:00 -0700
categories: Blog update
---

Writing my services in IAC (being Terraform and Ansible), as well as being able to for the most part start from a clean state, has been a hugely thought provoking and ultimately rewarding exersise. I have embraced the infrastructure as code ethos, and would gladly die on that hill after seeing it work as it should. Getting away from pets, hand crafted deployments, and hero efforts has given me the insights that I want to share. 

IAC deployments hinge around three components, the first being IAM (Identity Access Management). This mechanically is usually user credentials or system tokens, but newer methods like Consul are other options of Identity control and flow. AWS IAS could likely take on any of these individual tasks, or multiple discrete applications like Okta and Hashicorp Vault could be combined tackle the AAA challenges. Version Control Systems are a huge part of IAC, as without a means to track, maintain, and share the same picture of the deployment, the goal would be hopeless. Crucially, I see this as not just the playbooks or recipes of the applications, but of using state tracking a la Terraform's shared `.tfstate`. Git and S3 would be both halves of the VCS split. Finally, but perhaps not quite the most fleshed out concept (and really not a name I'm fond of), the Networking a component of IAC. I grouped routing and firewalls with DNS together because I could not cleanly fit either into a application definition, or an application identity; perhaps this is an outdated way of looking at networks (pre-zero trust and other modern ideas). 

As the reader could possibly determine, ideas are bubbling over in my head, but with so many possibilities the implications are not fully fleshed out. So several blogs like this could come out and help hone these ideas. Until then, I want to pen my idea for an IAC rollout at this time. Some of the thinking comes directly to solving challenges posed directly by the tools I have picked up and looking from the perspective of needing to 0-stage and N-stage (ie bootstrap from nothing, as well as having it work every run thereafter, idempotently) on local bare iron. Terraform, for instance, doesn't seem to allow me to elagantly rollout some "core" applications like Vault, but in the same definition file use secrets from that server which would not be setup without secrets and certs contained within. Barring those hesitations, I see:

A core VPC (Virtual Private Cloud)/zone/tier with:

| Resposibility | Selfhost | Service Provider |
| :---: | :---: | :---:|
| IAM | OpenLDAP, Keycloak, Vault | AWS IAM, Okta |
| VCS | git, S3-compatible | git, S3-compatible |
| Network | dnsmasq, pihole, Pfsense | Cloud-specifc tooling |

The IAM has the most variety of options, but the problem to solve would be to centralise users, credentials and their authority. Version control is almost uniformily git, but what remote server depends on flavour acceptable. S3 is at this point a ubiquitus API and offered everywhere; it would be used for shared object storage, application configs, and retention. Finally, network is the biggest thorn again on self hosted infra, as VPS-providers all offer solid API's to configure access.

The second zone would the remaining apps in more of a DMZ that would be seperated from the tightly protected core and interact through monitored, encrypted, and hopefully zero-trust connection points. This could be scaled and maintained in many different ways, from thick vms to individual containers to orchestration. At that point, the IAC would be working for you and enabling that to happend quickly with the intial organisation bootstraping done. 

Just my thoughts for now, keep posted!

