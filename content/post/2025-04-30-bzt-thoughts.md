---
layout: post
title: "BZT Thoughts"
date: 2025-04-30 00:00:00 -0700
categories: Blog update bzt
---

A collection of some thoughts about BZT, zero trust solutions, and zero trust in general.

## Device-aided BZT

Trusted device start is an important factor in a zero trust architecture. Storing a secret key in a TPM and using that Key to authenticate a device and encrypt is a solid baseline to work past in the boot process.

Such a process would look like storing a secret key in the TPM, and use it with the IPSEC daemon. IPSEC policy drops non-IPSEC as normal to and from devices. Client auths normally over strong auth when attempting to use application traffic.

## Wireguard

Using Wireguard with tunnels in ZTA is still providing an authentication point, but by ending in a tunnel means server hosts end up trusting private tunnel subnets.

## MTLS

While MTLS is useful for encrypting and authenticating the session used for an application, it does not stop unauthenticated traffic or protect all IP protocols. Firewalls can be trusted to drop blacklisted ahead of time traffic, either at network ingress or at the host level, but is potentially not dynamic enough. Having per-session encryption settings, as well as potentially easier implemetation, can make MTLS a more attractive setup than full IPSEC.

## IPSEC Drawbacks

With Transport Mode, each packet would need to be decrypted before it could be evaluated; this means packets would need to go through an expensive decrypt client-side before they hit a firewall, taxing the CPU. XFRM policies help drop unauthati cared packets quicker however, although that may not be a huge savings in aggragate. This is mitigated by being able to verify the source hosts that are sending traffic.

Unfortunately, just limiting the packets that get to a host, doesn't nessesarily mean that the end-to-and encryption is complete. Some host level processes, liko on proxy, may be a final unencrypted jump for traffic. The fact that it is local to the host is still largely irrelevant. Having a proxy in the middle breaks the end to end encryption, but trust between the proxy and the backend can still be created.

Using load balancers, backend systems can share a certificate, as long as the client is configured to allow traffic with valid signatures from globbed or wildcard source addresses.
