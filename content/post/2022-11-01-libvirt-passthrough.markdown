---
layout: post
title: "libvirt passthrough"
date: 2022-11-01 00:00:00 -0700
categories: Blog update
---

Quick note on using a windows gaming vm on a libvirt host. Using pcie passthough can be a pain if using nvidia drivers, doing blacklisting on the drivers. Huge pages and the looking glass performance improvement page cpu tweaks did work, but when carving out ram and doing cpu pinning, you start to wonder about why even using a vm. It really is like having a hard resource divider, and not a resource pool dynamic allocation, because speed matters. Maybe its down to the age of the gear, not actually really able to play the games I was trying. The software and hardware support will come into its own in the next few years regardless.
