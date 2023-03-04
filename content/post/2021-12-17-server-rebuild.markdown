---
layout: post
title:  "Server Rebuild"
date:   2021-12-17 00:00:33 -0700
categories: Blog update 
---

Rebuild my main server, which currently has a 2x2 striped mirror ZFS pool (8TB usable), KVM, LXC and a few native servers. I needed more space (so adding another 4tb), which meant a case change (from an old Supermicro workstation to a cheap 3u rack mount). Unfortunately, this new case didn't work out: I needed more SATA ports, so I needed a HBA, so I needed more PCIE slots, so I needed to change out to a full ATX board, which doesn't fit with the HDD bays mounted. Now, I need to get a 4u chassis, move the server to that, and use the 3u for a container host to serve replies for the ZFS pool.

And I want bigger HDDs, so this is going to be an expensive project.
