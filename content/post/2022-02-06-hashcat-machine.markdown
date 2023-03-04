---
layout: post
title:  "Hashing Machines"
date:   2022-02-06 00:00:33 -0700
categories: Blog update 
---

Imagination sparked to run a GPU accelerated VM for hash cracking with hashcat. Having run it with CPUs, before, I know how to do that part, but I needed to get a GPU involved. I did this on my Fedora desktop, which had no problems with the drivers. But when I went to use a dedicated VM with PCI passthrough (something else I had just started doing with a fiber card for my router), I got stuck. I figured out how to do it, so I have a quick write up to share.

Basically, the device needed to be manually assigned to the VFIO modules instead of being picked up by the nvidia drivers used by the normal system. I tried many things before I found this problem out, but I found this guide which helped: https://github.com/f0cus3d/fedora30-pci-passthrough. Note steps may be different on other distros.

1. Find the device ID's (as described in guide)
2. Install @virtualisation
3. Setup the grub kernel configs ("iommu=1 intel_iommu=on rd.driver.pre=vfio-pci")
4. Add the device ids to /etc/modprobe.d/vfio.conf. There's two, one for the card and one for the audio portion. Both need to be passed through.
5. Dracut whined at my at the next step as written, so the following worked on Fedora 35. Add 'add_drivers+=" vfio vfio_iommu_type1 vfio_pci vfio_virqfd "', which is to say just add some spaces. For the dracut command, I had to run "kernel=`uname -r` ; dracut -f -k /lib/modules/$kernel", as it got stuck on the -kver and path being not relative. 
6. "grub2-mkconfig > /etc/grub2-efi.cfg" as decribed.

And it all came up after the reboot. Happy cracking
