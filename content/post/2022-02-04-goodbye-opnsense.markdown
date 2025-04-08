---
layout: post
title:  "Goodbye Opnsense"
date:   2022-02-04 00:00:33 -0700
categories: Blog update 
---

I went through a LOT of changes lately on my router system. I wanted to create a VM for it and passthrough a PCIE card, but combined with a fan failure and I only just got it finished. During that time, I had to buy new 10GB fiber cards (no drivers for cheap old ones), then had to get a new CPU for IOMMU groups, and then a new fan. I fought with two clean Opnsense installs, trying to get VLAN tagging working on a Mikrotik SFP+ port, but it was not working correctly. I decieded to try PFsense instead, maybe the kernel had some differnet modules, and while it didn't work initally, I did get the second SFP+ port working on the Mikrotik, so maybe Opnsense would have worked after all. By then though, I was too far into my build and had to to get it all working, so here I am on PFsense.

So far, seems far more commerical and pointing towards the company support than OPNsense. Wireguard installed okay, which was one reason I went with OPNsense to begin with, so not too mad. Will just need to recreate my rules and let it sit for a while. The network issues have been holding me back from some real work for so long, I nearly forgot what I was working on! Having real VLAN traffic for everthing, along with the router system I intend to run 24/7, I should be in a better place for some Snort or Wireguards shenanigans.
