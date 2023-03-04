---
layout: post
title:  "Ryzen Woes"
date:   2020-10-23 12:00:33 -0700
categories: Blog update 
---

First gen Ryzen seems like great value for money, even when compared to the Xeon builds that have been floating around the market for a few years now. I upgraded my storage server with a Ryzen 1600, but then had cpu lockup issues. Somehow, these seemed to only occur on my build on Linux while running ZFS; this turned out to be a red herring, as I found the issue (after my system has been stable after a few days) to be to do with cstate instructions. 

The patch for this issue was made in microcode, in turn placed in newer revision firmware, which of course my cheap motherboard did not get the update for. I found a python script to take of [this](https://github.com/r4m0n/ZenStates-Linux). By disabling c state 6, the machine runs fine so far!
