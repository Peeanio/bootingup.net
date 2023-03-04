---
layout: post
title:  "Minecraft Server: Part Two"
date:   2019-08-26 21:00:33 -0700
categories: linux blog update
---

I wrote my first post about the Minecraft server I have been running eight months ago, and I have changed a few things since then. I ran the server with a bit more than the default vanilla Minecraft, on a AMD FX-8350, which really is not the best CPU to run with. Keeping in mind that the jvm server is single-threaded, clock speads are a pretty big determinator of what the server will run like. There were some datapacks, no mods, and no more than five consecutive players, and I managed to get it playable. Here's some things I did. 

Aside from the CPU, there are two hardware performance improvements to make: RAM and disk I/O. RAM does little over 4GB to increase speeds, so I just overallocated and left it. For disk I/O, running an SSD, or better yet, a NVME SSD, can yield huge improvements for lag, block lag especially. Software-wise, there were a few parameters I passed to JVM, my start up script being

 <code>screen -dmS minecraft java -Xms8G -Xmx8G -XX:+UseG1GC -server -jar \
        /mnt/games/minecraft3/minecraft_server.1.14.4.jar nogui</code>. 

The -server and garbage collection tweaks seemed to make a slight difference, but I could not quantify it. Lastly, I implemented server reboots to clear cache etc. I started doing full reboots daily, then every four hours, then just stopping and starting the JVM every four hours. This seemed to get bogged down after a few days, so the best comprimise I found were JVM stop/starts every four hours and full reboots at night when no one is on. This really helped, and does not have to take long. 

I have several different types of backups running: full restorable ISOs and file backups. Every day I use rear to backup restorable ISOs, just in case anything really bad goes wrong, to an external server. Whenever the server stops, before restarting, I copy the minecraft server directory, tar it, and copy it off too. This way I can roll back only a few hours or have a quick export etc. 

I learned more about server administration and troubleshooting during this time, really seeing what performance tweaks can be made and tailoring the running enviornment, both hardware and software, to really get the most of the server itself. I highly recommend it as a learning experience, and and happy to answer any questions about getting started.

Thanks for reading!
