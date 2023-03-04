---
layout: post
title: "Reading Up"
date: 2022-08-08 00:00:00 -0700
categories: Blog update
---

I stayed up late too many nights struggling over what would be the best way to tackle some problems with IaC deployments, that I could not solve myself or by reading other blogs; my brain was too focused on my small deployment, and blogs typically covered even smaller and very specific cases. Learning a quick and easy way to Terraform a container is one thing, but how does that process carry over to Terraforming a VM with Ansible managing the config. Do I use cloud-config to enroll in Ansible roles, or use Terraform actions to hit the configs? How do I go about dependencies that are crucial to the stack I am creating? I was scrabbling for best practices. 

Kief Morris in <ins>Infrastructure as Code, Second Edition</ins> was the book I needed because it specifically focused on what the authour calls "patterns," rather than any sort of "best" practice. I latched onto some concepts that really provide some direction, and I want to share:

1. Primitives, or elementals, are some underlying building blocks that IaC as a process need to really operate as smoothly as it claims to allow. These include things like DNS, secret management, and things that lie beneath. A cloud provider typically offers these as services, which further allow for a "cloud-only" deployment, but with local or hybrid infrastructure these usually suffer a chicken or the egg problem, ie which comes first? I found this really answered by point two, or:
2. IaC is a process, and is therefore organic. It does not have to start with everything defined ahead of time, as that would mean that much time was spent with NO infrastructure at all. It is good to deploy everything with or through configuration/structure management, but by no means does that mean everything is automated in one go, but that is the goal. Build up from zero to automated everything, iterating in small chunks along the way. Automate the primitives, then automate the applications. 
3. There are patterns, not best practice. No organisation's requirements are the same, but enough orgs follow the similar enough paths that newcomers can follow the tracks. Declarative is not neceassarily better than imperative definitions, because either can be stronger in specific cases. Mixing the two is therefore GOOD, if the admin plays to their strengths and keeps the concepts and code bases straight. Either right size the server in the definition, and dynamically configure the application, or flip it and dynamically provision the server with a a static config, but don't do it in the same tool. Not that that practice is set in stone either ;)

So where does that leave me with my stack? I have some patterns I am following, and it's working; so I can keep following that until the pain is too much, make a pattern change, and carry on. Fail often, fail small, and fail forward until there's nothing that hurts. That looks like using pre-build docker containers and managing their configs in a repo that ansible can keep track of for me, and I can run idempotently. If managing the primitives comes next, great, or if changing from Docker to K8s or provisioned VM's works better for the flow, I can change patterns again. 

Stay tuned
