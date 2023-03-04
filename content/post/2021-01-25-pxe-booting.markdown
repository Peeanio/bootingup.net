---
layout: post
title:  "PXE Booting"
date:   2021-01-25 12:00:33 -0700
categories: Blog update 
---

One of my latest projects has been to get PXE booting auto installation working in a more dynamic way. This was sparked when reading the iPXE website, where they mention dynamic booting, using a webserver with PHP to select the install files based off hardware information. I don't know PHP, but I do know how to tweak a config file, so I set about trying to do this using just the iPXE stack.

My solution was to use predefined "channels" based off the hardware's UUID. The goal was to be able to be prompted at the menu for real hardware, but have newly defined VMs go through an unattended install. KVM allows the UUID to be specified, so I could define the domain with a pre-defined "Debian install" or "Alpine install" by giving the VM the UUID for that script. This could then be changed after installation to a normal generated UUID, although there still remains a collision chance, it is improbable. 

I will put my config file for iPXE in my [git](https://git.bootingup.net). This setup still does depend on an external storage medium (TFTP, HTTP, NFS, USB, etc) to pull in the kernel etc, but that is covered seperately. This config file has the TFTP sections left for an impression of a working file. 
