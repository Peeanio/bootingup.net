---
layout: post
title:  "Work Projects"
date:   2022-04-25 00:00:33 -0700
categories: Blog update 
---

My work projects have mostly scratched my dev itch lately, but with a good one coming to an end, its time to share. I've been enjoying writing a switch management project in Ansible, as its been great to have a hack at API's, network gear, and plain old optimisiation logic. The API's have been loads of fun and really interesting to get into, after being on my to-do list for ages, and I have a good feeling for JSON structs. This project has been mainly object orientated (if I have terminology right), being that we have an object (the switch) and are making tasks based on what is where. At home, I want to write some API servers for my own use case to get a good feel and slide yet further into dev land.

We needed this switch management plain for two reasons: we have three different switch vendors with different syntax and management/diagnostic methods, and we want a central source of truth to keep things consistent and in compliance. We decided that an Ansible inventory, with profiles for each switch port (ie trunk, shut, access vlan, etc) would be a good way to know what is supposed to be where and do what, but take the decision making of how to acchomplish that out of the operator's limited bandwidth. Having ten profiles to start with, we managed to get some branching logic so that we only need three different functions to actually lay that out: one for access ports (of various vlan, which is pulled based on the profile name and a dictionary of what VLAN that means), one for trunks, and one for the bridging AP ports. Really fun project to run out, and maybe that could be made public at some point.
