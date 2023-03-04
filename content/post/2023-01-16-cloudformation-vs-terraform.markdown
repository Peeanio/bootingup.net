---
layout: post
title: "CloudFormation vs Terraform"
date: 2023-01-16 00:00:00 -0700
categories: Blog update
---

At work, we use CloudFormation, dating back to when the org first onboarded into AWS. Since then Terraform has come out and I've used in AWS and other provider settings. There are some differences, which are interesting to note, but I think in general I stand behind Terraform. 

CloudFormation tracks state better. It is easy to trust CF to tear down a stack COMPLETELY, but there are some limitations then. It is difficult to programatically get resources, sometimes even information, when they are from outside the stack. This comes up rarely as an issue for full time Cloud Formation users, but there's an itch for those who aren't to just want an API call to answer to fill in gaps. Reaching outside the somewhat limited CloudFormation options is impossible. Terraform allows this, as it is all just in front of the standard SDK, but that also means the state can get away from a user if they are not careful. Less so with the AWS (fully-baked provider), but I've lost my state or resources don't import correctly, meaning I don't have unequivocal definition of state. 

Terraform requires a more careful and considered hand, but is easier to work with, especially when working multi-cloud or even with just different providers. Building holistic infrastructure with configuration is easier to achive with a tool that allows everything to fit and be plugged in. 
