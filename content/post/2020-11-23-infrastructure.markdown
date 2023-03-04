---
layout: post
title:  "Infrastructure: A question of scale"
date:   2020-11-23 12:00:33 -0700
categories: Blog update 
---

Its easy to get caught up in the intracacies of servers and deployment, overbuilding for a given problem, but it is just as easy to not plan enough, and be left with something that is unworkable and unsustainable. In general, it is better to overbuild than under, but not when building the infrastructure creates paralysis that prevents things from being done. Building a whole automated provisioning stack just to get a single web page up is too much, but where does one draw the line? 

At the end of the day, it comes down to cost. Cost of time, cost of manpower, cost of resources. If one can afford the expense of occasionally needing to spin up a server, that's okay; an automated system isn't needed. If there's a mistake, then there should be enough time to correct it before it is noticable. If it is a process that needs to be repeatable and consistant, that is when the system needs to be built. Following a devops mentality, there should be testing, practice, and a continous revisement of goals and theories towards the end goal of getting things done.
