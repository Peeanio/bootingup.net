---
layout: post
title:  "Ethical Starts"
date:   2022-01-29 00:00:33 -0700
categories: Blog update 
---

Got serious about the CEH. Got a No Starch Press Ethical Hacking book which I am now working through, as I want to feel confident on hard skills in addition to the theory of the CEH. Setting up my "weapons lab" vlan proved more difficult than it needed to be with VLAN tagging on Linux bridges on Mikrotiks. For anyone who reads this, I had to set the guests in KVM to use macvtap (which I never use, as I want the host to talk to the guests) instead of bridge mode. Likely something to do with the MAC addresses, but didn't read too far into it once I saw the right traffic. 

As I work through the examples and problems in the book, I will be putting my work into a git repo on the usual server. I don't know if that will be an issue, hosting crypto malware and botnet source code on the server, but I guess have a backup, right? 
