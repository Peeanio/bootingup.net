---
layout: post
title:	"Building a Homelab"
date:	2018-12-19 22:10 -0800
categories: homelab update
---
# Intro

  For those not already in the know, homelabs are a staple for those in IT: a place to build, test and play with technologies to improve understanding for use in a production or home deployment. There are somethings that people should know before getting into homelabbing, as it can be an expensive and draining hobby if done improperly. These are some of my notes and ideas from building my own enviornment.

# 1. Buy/Scavenge Used Enterprise Gear

  Old business grade kit can go on incredibly good deals on eBay or other resellers or recyclers, if one knows what to look for. Enterprise equipment has much more functionality than new soho (small office home) grade gear, and often has more support or availibility than homebrewing. So while Raspberry Pis or buying new networking gear like Ubiquiti may be appealing for price, there are often better reasons to buy old gear. Improving knowledge with vendor specific equipment like Cisco can pay dividends further down the career.

# 2. Plan Deployments

  I have picked up more gear for the lab because it was a good deal and still haven't been able to put it to use properly, because there was no plan. I have also had to spend more to fix a poor purchasing mistake because I did not plan out exactly my use case or end goal with it. This is case of not only practicing optimising uses for servers and networking gear by comparing feature sets, but also a chance to see what makes one product better than another. It also helps cut down on overbuilding the lab, as not everybody needs a huge core count virualisation servers, no matter how cool they are!

# 3. Suggested Build Order

## 1. Start with a NAS

   Network Attached Storage devices, or NASes, can be bought from companies such as Synology for moderate rates, but these are not what I am refering to. Going back to point 1, buy old enterprise gear. Get an old Supermicro or ECC capable machine to build a huge storage array. These are great places to learn about how and where to create critical infrastructure, such as backups and databases, as well as keep any materials for the lab. While FreeNAS may be an appealing option to run, with ZFS and minimal install size, I recommend OpenMediaVault Linux with ZFS raid pools for optimal results. I'll touch upon this in the future, so follow the website!

## 2. Network Backbone Next

   Up to this point, it is likely that you have a consumer grade router or only a few ports used. But to start getting serious, it is a good idea to start building a competant firewall and high speed router/switching enviornment. Not essential to some, but better have the backbone in place before adding too many different devices and services to the network, such as cameras or VOIP phones. Mikrotik makes very competant and affordable business networking equipment (especially routers with RouterOS), or build something with pfSense. For switches, it again can be benefical to run old Cisco or other brand that are in use at the office.

## 3. Virtual Hosts

   The storage and network is built up to acceptable standards, so now its time to build up some VMs! Virtual machines or containers allow very powerful machines to partition out resources to smaller, logical devices on one physical machine. Many different ways can be used to do this, but I can whole-heartedly recommended Proxmox. An open-source Linux distro with an incredibly powerful front-end for KVM and LXC, Proxmox is fast and efficent as well as easy to use. Did I mention free? For more free software, Virtual Box and Docker are useful tools to run on top of regular desktop operating systems to get the same job done.

# Conclustion

  What I have written down here are the notes that I have made while building my own homelab. I will have another write-up for my own equipment, as well as purchasing guide soon to help the budding enthusiasts out there. Any questions, feel free to ask below!
