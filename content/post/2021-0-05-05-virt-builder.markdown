---
layout: post
title:  "The Next Step: Virt Builder"
date:   2021-05-05 12:00:33 -0700
categories: Blog update 
---

I have been using Debian/Ubuntu preseed files for a while now, automating installation of machines as defined by a preseeded config file, which works great (don't get me started on how much I hate 20.04 though). While discussing the merits of images versus automated installation, I looked at and like the libguestfs suite of tools, notably the virt-builder tools for standing up a VM in less time. 

It was to my surprise that virt-builder builds its images from pressed and kickstart files, then just anonymises those disks to be used as templates. That was exactly what I wanted; a means of building images that works great and is easy to use, and a way to put those into templates that are virtually on tap. 

I will be working on some pipelines and workflows to take a preseed file and turning it into any number of virtual machines. From there, I want to start working on hardening system images, for purposes of having an even more secure linux host from the time that the system boots.
