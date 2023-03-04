---
layout: post
title:  "Fighting OAUTH"
date:   2022-01-10 00:00:33 -0700
categories: Blog update 
---

Spent the whole day today working on getting a working solution going for OAUTH2 with Keycloak today. Started with trying to get it with oauth2-proxy, which I got no results from. Both portions were in Docker containers, but I just could not what seemed to be cookies working fully. Then with vouch-proxy, I get stuck in a redirection loop with a JWT error.

Long story short, I have a few options. Ask for help, or move on from this idea. I view getting something like this as a huge win at home at work, as SSO is something that organisations just need now. There's few things that feel boiler-plate and drop in enough to get going easily, which is a shame. Although maybe keycloak is just worse than lemonldap-ng. 
