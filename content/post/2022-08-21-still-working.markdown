---
layout: post
title: "Still Working"
date: 2022-08-21 00:00:00 -0700
categories: Blog update
---

I took a bit of a step back to get some more perspective, but also because my environment seems to be struggling a bit. I have all my resources from different in a single project, from the "primitives" to the multiple applications, and it just was not happy spinning things up. It appears that single project IaC is a mammoth task; the other projects I've looked at seem to limit to individual services. That seems like a decent approach; roll out each service one by one, allowing the operator to handle the dependency order. I wrote an ansible script in the beginning to handle that (and pre-reqs), so I may split my terraform code into primitives (or multiple, if that needs to be split down further), and main application service stacks. Kubernetes seems to do this itself, but because I was rolling with docker, it all seemed to blend together. So, my choice of tool lead me into bad practices that I may have avoided if I knew what I was doing. Good to know; that's what testing is for. 

So I hope to be able to keep throwing stuff out there, but we shall see how my docker testing deployment goes. I have <strong>Kubernetes Up & Running</strong> to go through and hopefully teach myself that (when not playing some vanilla wow, oops). Application designing, especially in regards to getting the tool ready from as soon as it is run, is a bit of a chanllenge. I guess that's why some people get paid the big bucks. 
