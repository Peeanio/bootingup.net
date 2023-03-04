---
layout: post
title: "glauth and Keycloak"
date: 2022-09-20 00:00:00 -0700
categories: Blog update
---

Finally, I have an application looking at keycloak over oauth2, which is in turn fed over ldap. Single sign on is more of a reality, but perhaps more important is having mfa in either keycloak or glauth. The deployment wasn't easy, as the several of the elements weren't plug and play. 

glauth config:
```
[backend]
  datastore = "config"
  baseDN = "dc=bootingup,dc=net"
  nameformat = "cn"
  groupformat = "ou"

[[users]]
   name = "reader"
   uidnumber = 5001
   primarygroup = 5501
   passsha256 = ""
   mail = "reader@bootingup.net"
    [[users.capabilities]]
    action = "search"
    object = "*"

[[users]]
   name = "max"
   uidnumber = 5002
   primarygroup = 5503
   passsha256 = ""
   mail = "max@bootingup.net"
   
[[groups]]
  name = "svcaccts"
  gidnumber = 5501

[[groups]]
  name = "users"
  gidnumber = 5502
```

LDAP federation in keycloak:
```
UUID LDAP Attribute: uid
User Object Class: posixAccount
```

wekan oaut settings:
```
"OAUTH2_SERVER_URL=https://keycloak.bootingup.net"
```
(note the now <code>/auth</code> at the end)

Hope that helps someone
