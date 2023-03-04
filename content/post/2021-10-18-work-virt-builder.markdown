---
layout: post
title:  "Virt-Builder at Work"
date:   2021-10-18 12:00:33 -0700
categories: Blog update 
---

At work, we use a very basic KVM stack. It's bog standard KVM, with virt-manager to mess with VMs as needed. I would not recommend this, but its legacy and its there. VPSes like AWS and Linode have some pretty great scripts to roll out VMs based on a distro and a "tshirt size" of small, medium or large, essentially. We wanted to recreate this process without using any special tools like OpenStack or Proxmox, so we ended up doing it with virt-builder and Ansible. 

I wrote a series of scripts that in essence turn a server ISO installer into a disk image, which can be called on top. This significantly reduces the amount of time Windows takes to install (because yes, it does Windows and Ubuntu atm). Ubuntu installs with the subiquity installer (why they left debian installer for this crap, I really can't understand) easily enough, is then stored in a repo for virt-builder to pull and virt-sysprep to prepare for use with a static IP and some preconfigurations. Windows is installed with Packer, which is a good tool, and took the headache of doing the preseeding steps in ansible (which was the first prototype). It is still harder than Linux to inject configs etc at runtime, but isn't surmountable if one does most things after installation. 

Overall, it has been a headache experience to devise and implement this method, especially with the hodgepodge servers that we use. Very few commonalities exist to work up from, so the process changes almost machine to machine, but doing it this way will hopefully help our team get our legacy VMs changed over. That is untilwe are arbitrarily ordered to move to AWS and scrape everything.

Lesson of the day: do some planning when doing strategic changes. It helps prevent wasted man hours. And don't let yourself drown in technical debt
