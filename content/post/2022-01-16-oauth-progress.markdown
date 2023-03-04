---
layout: post
title:  "Oauth Progress"
date:   2022-01-16 00:00:33 -0700
categories: Blog update 
---

Made progress with oauth2-proxy by using Okta instead of keycloak, which was likely a partial source of much trouble, although I will backport some of my config in order to see what the issue is. 

Some observations were made using from using this though: what to do with the headers or cookie for legacy apps? Should the cookie be made as minimal as possible with the headers as stripped as possible, or should some work be done to work with whatever authentication method the app uses? SSO is the end goal, so it is completely desireable to get that working throughout, but that means learning all about web auth. Oh well, that's something to add to the CV!
