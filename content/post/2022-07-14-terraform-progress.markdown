---
layout: post
title: "Terraform Progress"
date: 2022-07-14 00:00:00 -0700
categories: Blog update
---

Terraform has been going well, it's been nice to use the tool to do what it takes some serious scripting to work around. The one thing I'm concerned about, especially with the libvirt provider, is how terraform remediates minor things in the infrasturcure. That begets the question, is it then something that is a core part of the deployment strategy to work around? Using a tool as part of the process, vs using the tool and working within its confines is something that has always been difficult to determine the best practice of. 

Using the Docker provider, on the other hand, has been much easier to work with. It seems stronger easier to "define and forget;" libvirtd needs to be copied as a huge chunk in order to deal with the network and storage resources alone. Overall, looking forward to see how far I can take it. 
