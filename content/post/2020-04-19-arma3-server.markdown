---
layout: post
title:  "Arma 3 Server"
date:   2020-04-19 12:00:33 -0700
categories: Blog update 
---

I set up an Arma server for my friends during the downtime of socail isolation, which was fun and fairly easy. I did it on a Linux host, and then on a Linux VPS, and had some good and bad experiences. For bad, Arma is primarily a Windows game, and the anti-cheat, BattleEye, does not work properly even in Wine, so it has to be disabled for me to play on my Linux rigs. That means I could not use the RCON BattleEye features, which I wanted to use to do some remote management and monitoring. Installing mods was a bit of a pain, but doable once I found some download sites for downloading mods from the Steam workshop, as steamcmd does not have that capability (wishlist!). But there is a Linux server binary, and it works fine, is stable, and uses minimal resources. The config file is pretty easy to work with, and although the documentation isn't great, it isn't insurmountable. Always happy to answer questions for anyone wanting to run servers on Linux, based on my experiences!

