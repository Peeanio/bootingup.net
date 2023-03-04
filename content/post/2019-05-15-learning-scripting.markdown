---
layout: post
title:  "Learning Scripting"
date:   2019-05-25 20:54:33 -0700
categories: linux update
---
I should preface by saying I am in no way good, proficient, or authoritative about scripting in *nix or any other computing environments. But I have had an absolute blast getting started, and wanted to share my thoughts and discoveries. Anyone else who has already been here, feel free to call me a n00b.

It started out when I found myself installing webmin a lot on my new servers. I got tired of going through the whole things time after time, and I thought it made sense to finally start scripting things. I mean, it is very easy to just chain commands like that together into an executable script, so that way my first: a shell script to install webmin. I was hooked after that.

I am an IT administrator, so automation is key to saving time. Something I noticed a few machines having was a lack of reporting over SMART values. I wanted weekly or daily reports about SMART status on disks, so I could know hopefully beforehand about failing disks and system crashes. Now for this script, I wanted it to run, without any hardcoding of disk names or numbers, and to send emails. Sounds pretty straight forward. But to get all this information, it took multiple read throughs of several man pages to formulate the equation of getting, finding, and then narrowing down to actually important data about disks. I had to learn about programs that are long-standing tools in the OS arsenal, but most average users don't use for desktop or routine operations. I got to feel like a hacker in the original sense of the word, and it was great. Learning scripting is a fantastic way to increase proficiency and efficiency of a given install, and definitely more software-side than I usually like to run.

Thanks for reading, come back for more!