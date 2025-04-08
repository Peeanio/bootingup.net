---
layout: post
title: "Preseeding and Autoinstall"
date: 2021-01-11 12:00:00 -0700
categories: Blog update
---
I have been using a script on my git site (git.bootingup.net) for headless VM installations, and it has been working so well for me, I missed the functionallity at work, where VM installs have been manual. At home I use Debian, work Ubuntu, so I wanted to port my preseed configs over. This went smoothly (after I worked out that Ubuntu shipped their netinstall kernelwith different permissions than Debian) for 18.04 and older, but 20.04 moved away from the preseed architecture, towards a new system called autoinstall. 

This yaml based approach is very similar: pass the config file in, declare what you want, but more what the people are used to with the syntax and features in todays enviornments. The new system is not as easy to setup with a PXE enviornment as the netinstall disks are, as it requires the use of an NFS server, but it operates fairly similarly logically, and does not require canonical to maintain multiple install disks (which is their problem anyway). I will put the pxelinux config files on the git, and potentially do a more in depth write up, but for now I'm just happy that I cracked this one, and it was something so easyily solvable. 
