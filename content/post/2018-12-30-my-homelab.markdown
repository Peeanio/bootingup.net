---
layout: post
title: "My Homelab"
date: 2018-12-30 22:00:00 -0700
cateories: homelab update
---
# Intro

I have a lot of equipment in my lab, and not all of it runs all the time. It does however make it convienient for when I need to get something running or try something out: I have hardware ready to go. To this end however, most of my gear would not cut it in a production space. I bought cheap to get the good enough experience, so like I said previously, plan your deployments.

# NAS

My Supermicro 1U X8DTU-F is my pride and joy: two Xeon E5620 quad cores with hyper threading run the few things I have running on it, and 32GB of RAM keep the ZFS pool running smoothly. The ZFS is a Z1 with 4x2TB drives, for about 6TB useable. Not too much for the number of disks, but the drives are cheap and redundant. I currently run FreeNAS 11 on it, with a few jails for Nextcloud and Plex. It has some Samba and NFS shares for backups and Windows to pull games from. Only complaint I have is the volume of the tiny fans inside, but I live with it.

# VM Host

This more recent addition is fairly built, but I don't run anything full time production on it anymore. Its an HP DL385 G7, with two eight core AMD Opteron 6220s and 48GB of RAM. This one runs Proxmox on a Z2 array of 4x146GB 10k SAS drives, and also has a Z2 pool of 4x120GB SSDs. I love knowing I am booting off of ZFS on Linux, but there is a boot issue with importing the zpool, and I am unsure if that is isolated to my install or not yet. I want to rebuild it again, at which point I'll get to the bottom of it. Rock solid aside from that issue.

# Networking

I have a pair of Cisco switches for the datacenter, but the routing and wireless equipment is Mikrotik. I enjoy RouterOS and work with it, so I use it at home as well. The Ciscos have minimal config while I study for the CCNA; this goes back again to purchasing. Sometimes its better to buy for the career than initial useability.


Thanks for reading, as always contact info is below.