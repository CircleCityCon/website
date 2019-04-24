---
title: "Building Virtual Labs: CCC Edition"

---

Most IT and Infosec professionals agree that hands-on experience is the key to developing your talent, and advancing your career. Everyone needs a place to practice, because practice makes perfect, Right? But where do you start? That is what this training is all about!

This goal of this training will be to teach students on how to build a virtual lab environment for studying various aspects of information technology that interest *you*. I'll show you what you need to know in order to build a self-contained, baseline lab environment that can then, with the knowledge you have gained, be customized to suit your needs and your interests. I will show you best practices for maintaing your virtual machines and lab environment, as well as how to take necessary precautions and measures to contain and isolate your lab environment. 

In this course, you will learn about how virtualization works in general, how to isolate your VMS to harden your lab environment against VM escapes, learn about network segmention and fail-close networking, how to configure an NSM/IDS platform for monitoring your lab environment, How to set up Splunk in order to read your IDS logs easily, as well as how to configure remote administration (e.g. key-based SSH auth) and update automation, to ensure that your virtual machines are updated regularly.

This session will be focused on setting up an environment using the virtualbox hypervisor. I will cover how to set up your lab environment on Windows, Linux or OSX hosts. In order to participate, here are the hardware requirements I recommend:

RAM: minimum of 8GB of RAM, with 16GB recommended
Disk Space: minimum of 500GB of free disk space to account for ISOs, applications, snapshots and VM disk images.
CPU: CPU needs to support 64-bit operation and either needs to have AMD's AMD-V or Intel's VT-x capability. Recommend something with at least 4 cores or more.
Motherboard: BIOS needs to support AMD-V or VT-x

In the interest of saving us all time and bandwidth, I highly recommend downloading your ISOs, applications, and setting up online accounts in advance. If you cannot do so, I will provide thumb drives with ISOs/applications available for students to copy.

Here are the ISOs and Virtual machines you will want to download before the training:
-Ubuntu Server 18.04.x: https://www.ubuntu.com/download/server
-Kali Linux, whatever the latest "full" 64-bit release is: https://www.kali.org/downloads
-pfSense (select "AMD64 (64-bit)" as the Architecture, and "CD Image (ISO) Installer" as the Installer): https://www.pfsense.org/download/
-metasploitable 2: https://sourceforge.net/projects/metasploitable/files/Metasploitable2/

Here is a link to the virtualbox downloads page: https://www.virtualbox.org/wiki/Downloads
-Download and install the latest version available. Windows and Linux users can simply download and run the installer package. Linux users can navigate to: https://www.virtualbox.org/wiki/Linux_Downloads . This page will show you how to install virtualbox through your operating system's package manager, or you can select the "All distributions" link, and download a ".run" package.

Now, for Windows users, you will want to download and install the following packages:
-mRemoteNG: https://mremoteng.org/download
-WinSCP: https://winscp.net/eng/download.php
-7-zip: https://www.7-zip.org/download.html
-puttygen (64-bit): https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
-Notepad++ (64-bit): https://notepad-plus-plus.org/download/
-KeePassXC (64-bit): https://keepassxc.org/download/#windows

For OSX users, we will be utilizing a lot of command-line utilities. You will be using vi/vim, ssh, ssh-keygen, scp, zip/unzip, gzip/gunzip, and alias. All of these commands should be installed and available by default. In addition to these utilities, I recommend downloading and installing the following:
-iTerm2: https://www.iterm2.com/downloads.html
-One of the following text editors:
--BBEdit (no, you don't need to purchase any of the advanced features): https://www.barebones.com/products/bbedit/download.html
--Sublime text editor: https://www.sublimetext.com/3
-KeepassXC: https://keepassxc.org/download/#mac

For Linux users, we will be utilizing a lot of the same command line utilities that the OSX users have. Since every distro is different, I can't assume that you have these tools, but in most cases they are installed as "core utilities", or something to that effect. Make sure that you have vi/vim, ssh, ssh-keygen, scp, zip/unzip, gzip/gunzip, and alias commands installed.
-I recommend having a text editor of some sort available -- gedit, kwrite, leafpad, whatever comes with your distribution should work just fine.
I also recommend having a terminal application of some sort installed -- Konsole, Terminal, gnome terminal, etc. I highly recommend installing terminator (https://gnometerminator.blogspot.com/p/introduction.html) if your distribution has a package available for it, since it has a lot of feature parity with OSX iTerm2.
-Ensure that you have a window manager of some sort installed -- Gnome, KDE, XFCE, etc. We won't be doing virtualbox headless, so you need a WM to draw the GUI in order for you to follow along!
-KeepassXC (the product page has installation instructions that vary by distribution. Additionally, they also offer an "AppImage" file that works similar to the virtualbox ".run" file to make it hassle-free): https://keepassxc.org/download/#linux
 
Now, in addition to that, I recommend doing the following:
-Since this class will be using Splunk and Splunk Products, at an absolute minimum, you wil want to visit the Splunk website, and register: https://www.splunk.com/page/sign_up
-This is entirely optional, but once you get your Splunk account, you may want to request access to a developer license. You'll need to log in to your Splunk account and go here to request a dev license: https://splunkbase.splunk.com/develop/
-This lab gives you a choice between Snort or Suricata as your IDS/IPS system of choice. If you plan on using Snort for your lab environment, register for an account at: https://snort.org/users/sign_up
-After signing up, you will want to collect your "oinkcode".

* **SPEAKER** [Tony Robinson](/bios/tony_robinson)
