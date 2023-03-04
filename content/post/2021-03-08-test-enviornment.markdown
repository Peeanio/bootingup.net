---
layout: post
title:  "Test Enviornment"
date:   2021-03-08 12:00:33 -0700
categories: Blog update 
---

When gearing up to make changes on a production network, there's almost always something that would be great to just try first; it could be because one is unsure on the exact behaviour, or there's some ambiguity over what the best approach is. Keeping those tests away from a network that matters is important, and while having a separate VLAN is a pretty good approach, one of my favourite domains is to build a virtualisation host, and to use it as a router for a self-contained network segment. 

There is a lot of upsides here: there is only a single point of contact to the upstream network, it's all relatively local (localhost, in fact), and one could test routing easily without needing multiple VLANs. Most of these are network side advantages (which is why it appeals to a network guy), but for server people there's also the upside of all the disks being local, so many times mountpoints can be exposed physically instead of over a network share.

Physically, the setup tends to look like a KVM host with two network bridges; one is for normal northbound traffic (or hosts who should be in that broadcast domain), and a second one to act as a NAT router for any internal subnet(s). If KVMs are too fat, then LXC or Dockers are spun up at whim too. First should be a DHCP/DNS server (personal choice atm is dnsmasq), then building up with a PXE and ansible systems. 

At the end of the day, its a great way of having a world in a box, to build as close to or as simplistic as needs must.
