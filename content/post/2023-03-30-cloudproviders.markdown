---
layout: post
title: "Cloud Providers"
date: 2023-03-30 00:00:00 -0700
categories: Blog update
---

I've used linode to host a mail server for a few years now. They are changing their pricing, and I thought I would try out Digitalocean, see what it was like. I appreciated the aws-like product offering, and spent some time writing terraform to spin up a new email server there. I get it all spun up and lo and behold, Digitalocean now blocks port 25.

It is disappointing that it is getting so difficult to host an email server. Too many bad actors spoiled it for the rest of us by taking advantage of lack standards and controls to send spam. People don't want to run their email servers themselves, because of the legacy of malicious behaviour, so those of us that want to start without the static IPs with reputation are left wanting.

Just a rant and a warning: no Digitalocean for mail servers!
