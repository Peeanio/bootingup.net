---
layout: post
title:  "Project Update 2: Containers"
date:   2019-12-17 12:00:33 -0700
categories: Blog update Linux project
---
Today was mostly about realising what LXC is and does, and what Docker is for. LXC is a Linux container; like a BSD jail, it is just compartimentalised filesystem that shares the host kernel. Docker is different, it is primarily driven by what application it is intended to deliver: a Docker container pulls its config from the dockerfile, and is meant to die when that container and application are done. LXC is more similar to a virtual machine, but there are less wasted resources spent on recreating some components. 

This brought me to the conclusion that really, VMs are not what I should be using for this, use LXC containers and use Ansible just the same. These are easier to bring up, manage, and scale. With something like k8s to manage, then potentially clustering and other high availability options are available too.

Going forward now, I have options. If I want to learn the devops way and practices, then building some clusters and configs with scipts and apps is the way to go. If I want to roll as a sysadmin, then building a domain with FreeIPA would be great practice for AAA and other domain activities. I can always do both, but I think for the next step, devops will be great to have to build some serious infrastructure. 

Wish me luck, and I would love to hear any input, advice, or comments for those reading. Email always available.
