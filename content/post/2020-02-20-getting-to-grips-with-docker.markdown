---
layout: post
title:  "Getting to Grips with Docker"
date:   2020-02-20 12:00:33 -0700
categories: Blog update 
---

I had a job interview recently, and I learned how this prospective employer was doing their infrastructure: using Docker and Ansible. I have been using Ansible more and more, getting to grips with how best to employ the tool. I have some work to do catching up there, but totally doable. I did feel lacking in my practical skillset with Docker; I had just docker run some things before. So I set about wrapping my head around the technology, and it just clicked. 

First off, I already recognised that Docker is meant to deploy applications, in a means that is declarative, meaning that really the compose file etc is meant to be the means to the end, which the application stack. To a newbie, that is way off in left field, but I had an inclanation of what that really meant, because Ansible is the same way. You don't write a srcipt in Ansible, you DECLARE what state you want the system at when it finishes. That mental shift takes some time, as it did to application based deployment, versus a full VM or more traditional container. 

To solve the problem, I wanted to see go through the process of what migrating one of my existing applications would look like moving to Docker. I chose Mediawiki, as it has both a web and database component. The backend to me was the easy part; running up the actual software server is pretty straight forward with existing containers etc. What did not make sense to me was how to manage the assignment and config of networking. The most common forms of Docker networking is using the host as a bridge, or passing through a port, NAT style. Okay, but what if I want to use DHCP? Can't really do that with macvlan networking, just static IPs. But that is one of the interesting things about my small scale deployment hump; I'm not used to having to deploy more than a single instance of anything to bring a project online. 

Using load balancers and reverse proxies is standard practice in big enterprise, to ensure full run time and availability. Point your DNS entry to a jump server, which proxies to the Docker host, which forwards the port through. The port NAT system is still a little ugly, as ports should be checked/incremented for mass deployment, but the concept is there. Docker is meant to solve large scale problems, problems that are not even issues down low, or in private networks, where the majority of my experience lies. This paradigm shift is what I was ultimately fighting, and took some serious head bashing to figure out. 

I am very pleased with my adventures here, and in the other tech I've been exploring with recently. It has been a great deal of catch up to get to this point, but solving the problems the same way as everybody else years ago helps me understand why things are where they are, and how people reached the same conclusions. I may be off base with some specifics, but I believe I have the concepts of distributed, redundant, and declaritive computing down. Pets versus cattle, and the farm is getting a whole lot bigger. 
