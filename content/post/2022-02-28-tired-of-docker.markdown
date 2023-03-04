---
layout: post
title:  "Tired of Docker?"
date:   2022-02-28 00:00:33 -0700
categories: Blog update 
---

The Docker deployment I am using is looking more promising, especially for web front ends. The Let's encrypt wildcard is easy to use, so using the single wildcard with haproxy makes for a compelling single moving part. I suppose a clustered deploy would be useful, to prevent downtime with the single load balancer, but that's okay for my size. 

Next, I want to get some NIPS or perhaps WAF in place behind the SSL balancer, to keep that honest, before opening up the firewall. As I'm typing that, doing some more firewall rules on the docker host to prevent action when comprimised, but that's another kettle of fish.
