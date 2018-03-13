---
title: "Designing Linux Rootkits"
trainers:
  - "bios/himanshu.khokhar.md"
show_title: true
---
Rootkits are one of the most misunderstood topic in information security, mainly because they are very complex and not well understood. This course aims to provide a foundation in understanding and designing Linux based kernel mode rootkits so that they can be understood properly and if the need arises, can be written at will. 

Designing Linux Rootkits is an intense,fast paced, 3 day course on designing Linux kernel mode rootkits from scratch. In this course, the attendees would gain proper understanding of rootkits, how they work, how they are designed (in general), techniques used by rootkits to hide themselves and much more. Then this course advances to teaching Linux kernel architecture, virtual file system, system call table and important data structures. Once the foundations are laid, we move to actual meat of the course, the hijacking. Hijacking file system, keylogging, Privilege Escalation, covert channels and much more. 

This course is an intense yet fun course with lots and lots of kernel manipulation.

# Syllabus

1. Understanding Rootkits
        - What rootkits are (and what not)
        - Distinction from other malwares
        - User mode vs kernel mode
        - Rootkit components

2. Linux Kernel Internals
        - Linux kernel architecture
        - System call table
        - Interrupt Descriptor table
        - Virtual File System
        - In-memory process representation

3. Loadable Kernel Modules (LKMs)
        - Introduction to LKM
        - Understanding Kernel Modules
        - Writing LKMs
        - Loading LKMs into kernel

4. Hail Hooking
        - Hooks and type of Hooking
        - Patching the Syscall table
        - Inline Hooks
        - A different approach to Inline Hooking

5. File System Hooking
        - Locating syscalls to Hook
        - Hiding files and directories
        - Bypassing stat family

6. All your keys belong to us
        - Introduction
        - Diversion from regular hooking
        - Designing a kernel mode keylogger
        - Adding functionality

7. Communication with outside world
        - Setting up covert channels
        - Receiving and executing commands
        - Receiving commands without a connection!
        - No open ports, no problem!

8. Privilege Escalation and Hiding
        - Introduction
        - Elevation of Privilege from Linux Kernel
        - Doing it covertly!
        - Hiding the rootkit

9. Communication with Rootkit
        - Multiple ways to communicate
        - Communication via device drivers
        - Communication via syscalls
        - Other options?

The Road ahead