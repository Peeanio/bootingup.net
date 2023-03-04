---
layout: post
title:  "More Docker"
date:   2022-02-19 00:00:33 -0700
categories: Blog update 
---

At work, there's a push towards using K8s. I've setup a test K8s, I've run some docker, but I'm no expert. As I mess with all that tech, I'm starting to get behind it as a concept and want to use it in a meaningful way, and get away from "my apt packages and debian servers work fine thanks." 

Some of the services I run at home are now in containers. I've set up a haproxy server to act as a load balancer entry point, complete with SSL. This is funky, as in the backend network, everything is exposed (and some Docker containers expect the security to be on the host, implictly trusting traffic), but also means I need a wildcard cert. Will need to read up on Lets Encrypt to see how that is this days. 

This hopefully is another push towards self hosting again. My storage server needs to stay storage, but then my "compute" machine has been setup as a security weapons lab, not a container host. I've got some work to do, but I don't expect to run it all rock solid and full bore: there will be some services going up and down, as long as I learn some tricks doing it
