---
layout: post
title:  "Automatic Debian Installs"
date:   2020-05-03 12:00:33 -0700
categories: Blog update 
---

When embracing "devops"-style workflows as a sysadmin, one of the most important things is to reduce time to get tasks done; this is why we use Ansible, Docker, and all manner of other tools. Creating VMs is not a quick pactice most of the time. One of the common ways to get around this is to have a golden image and clone it for new VMs, but I don't find that cloning is the best practice, as images may need to be changed or adapted to fit other workflows. It also does not help as much for physical installs. I found that the best way is to use Debian Preseed configuration to do this all for me, automatically, in an extensible manner.

[Debian Preseed](https://wiki.debian.org/DebianInstaller/Preseed) is fairly straightforward; one configures a text file with a series of options, which the installer loads at runtime and uses to select the install options. It can be baked into the iso, so it is completely independent, or it can be loaded off of a web server, which for ease and extensibility is what I went for. The options here are open and usable, with the ability to configure networking and disks fully, install packages at install time, and put in a hashed password for security. The preseed file is the easy part, and doing it on a physical machine is easy as hitting a button, but what about using preseed automatically with virt-install, or without specifying an ISO file?

I found two options to use with virt-install that would make for an easy script to load in these two settings. For use of downloading and running an ISO from RAM, I used `--location http://ftp.us.debian.org/debian/dists/buster/main/install-amd64/`, which saves me ISO management. The option I ended up using was `--extra-args "priority=critical auto=true console=tty0 console=ttyS0, 115200 url=http://<webserver>/d-i/buster/preseed.cfg"`. This handy option essentially uses the tty to specify the web server, much as one would manually. The other ways of specifying the preseed are listed in the linked article above.

No what about the extensible part, one would ask? This is certainly possible with if/else statements with a normal shell script, but as an Ansible fan, I found it just as practical to do so in a playbook. The esscence was to use a few options to set variables for things like disk size and RAM based on roles to be defined, then use group-based preseeds as needed (one for web-servers, database, or Docker hosts), and then add the resulting VM to inventory to integrate with the standard Ansible setup.

This is an example workflow I found to be effective, and I am curious to find out others are doing to minimise work and add repeatability to their infrastructure. Let me know!
