---
layout: post
title:  "Project Update 1: KVM and Preseed"
date:   2019-12-17 12:00:33 -0700
categories: Blog update Linux project
---

I spent my first night on the project, and while it was not without its frustrations, it was successful: I was able to install Debian from a preseed file, and learned how to use KVM properly from the command line. The most difficult issues for me were finding correct and accurate examples of syntax for using the extra arguments on the virt-install script to get things correct. That was of course, after I spent at least an hour trying to boot from a correct ISO. The --location switch is very picky with the type of ISO that can be used, and to be perfectly honest, I found it by accident. The final stumbling block I had was even though I had automated what I could in the preseed, I was still being prompted to manually intervene during the install. Some extra arguements saved me there. Overall, I am impressed by what I can do with preseed and virt-install. I already use KVM daily, so I look forward to more automation with that. The preseed can be quite basic, but there is a lot during the partition step that can be modified, which speaks to preseed's power. Hosting a random web server with a sped up preseed.cfg to install on many systems is any interesting idea :).

With the first day done, what feels to be the hard part is over. The quest for automatic and domain managed end points is under way, and I believe the next step is the domain management. I will look into FreeIPA and perhaps more for this step. Having had good success however with automatic VMs (or even physical machines), I think it may be worthwhile to try my hand more completely at writing container configs, whether with LXC, Docker, or K8s. PXE booting is great, but it isn't really required; starting a physcial machine from a preseed is one line, perhaps even a HID Arduino I have build could help there ;). Anyway, more to come!
