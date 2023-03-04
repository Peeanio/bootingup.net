---
layout: post
title: "What I learned running Linux Minecraft Servers"
date: 2018-12-17 20:54:33 -0800
categories: minecraft update
---
# Intro

Running Minecraft servers on linux the manual way isn't too bad: just execute the jar file with java and leave it running. What if you want to automate it, or need to send in commands? One needs to be able to easily access the run session easily, and the tools I used was screen.

Screen creates a vtty that can be attached and detached as the running tty locally or over and SSH tunnel, making it ideal for automation and remote management. Simply start the screen session, leave it running and forget. Using Debian, a systemd distro, I used screen, a systemctl service, and a bash script to get things running. This was an excellent chance to experiment with these tools for a useful application.

# Setup

What you need to include on the system:
1. Minecraft server user for security/ease of use (in my case, minecraft)
2. Screen (in most repos)
3. Minecraft server files (theres guides for this; I can make one for this method if requested)


# Steps
1. In the minecraft directory, create a shell script to launch the screen session. I used the following: <code>screen -dmS minecraft java -jar minecraft_server.1.13.2.jar -o true</code>
   * To break this down: start a screen detached named minecraft, executing java with jar file <code>minecraft_server.1.13.2.jar</code>.
2. Once this is working, all it takes is to create a way to run on startup. I am running this on Debian 9 Stretch, a systemd distro, so I created a service through that. My service, <code>/etc/systemd/system/minecraft.service</code> reads: <code>ExecStart=/bin/su minecraft -c /minecraft/startup.sh.</code>
   * To break this down, the service uses minecraft user to run command startup.sh

# Conclusion
I did not follow a specific guide to build my servers this way, just experimentation to find the right combination of steps to get it to work. I learned that these tools are powerful, and great for creating automated systems. This method can be used to run multiple instances in multiple screens, as I do on my production enviornment.

Any comments, please contact me below. 