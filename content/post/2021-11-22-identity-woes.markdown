---
layout: post
title:  "Identity Woes"
date:   2021-11-22 00:00:33 -0700
categories: Blog update 
---

Been looking at server to use as identiy backends for a build out of my infrastructure in a clear and manageable way. I want to use centralised identities, and in my head I had SAML, but the servers I use do not use it natively. I can look into locking down the reverse proxy with SAML and just use Keycloak, as an easy server to set up, but going with a different tool such as Gluu or LemonLDAP-ng would give me multiple backends to work with. That brings into question what's really the point of settings up security with MFA if I end up using LDAP or RADIUS and disregard the MFA to begin with?

It would take care of the password management, allow me audit accounts much easier (as well as mitigate comprimised credentials), but its a bit far from the modern way of doing things. This also got me thinking about using WPA2-Enterprise: what's the use in it from a security perspective if it is so easy to comprimise credentials during that step of the process? If everything else is hardened with MFA, its not the end of the world if the password is found, but everything not hardened is then open for abuse. 

There's levels of comprimise, and I'll just see where I end up with. Will post about it.
