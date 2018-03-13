---
title: "Quick Retooling in .Net for Red Teams"
trainers:
  - "bios/dimitry.snezhkov.md"
show_title: true
---
Quick Retooling in .Net for Red Teams

PowerShell gave us a super-highway of convenient building blocks for offensive toolkits and operational automation. However, use of standalone .Net implants may be a desirable option in cases where PowerShell is heavily inspected and logged.

While there are great toolkits to invoke unmanaged PowerShell or directly interface with .Net CLR - they are also statically compiled, and therefore easier identified by the defense.

Red Teams are faced with specific challenges when they need to retool quickly in the field with .Net payloads. Can .Net toolkits accomplish their goals while maintaining flexibility, quick in-field retooling and operational security in the face of current detection mechanisms? We think so. 

This talk walks through some of the options present to the operators for .Net code compilation and presents ideas for extensibility of .Net tools at runtime, with the help of Dynamic Language Runtime (DLR).

We will dive deeper into operational security lessons learned from dynamic code compilation. We will attempt to move beyond static nature of .Net assemblies into reflective DLR, achieving on-the-fly access to native Windows API. We will also discuss some methods of hiding sensitive aspects of execution in managed code memory.

We will also touch on ways to help Defense fingerprint the attacks involving dynamic compilation of .Net assemblies, use of DLR and building blocks of offensive tooling involved in the process.

A concept tool built on these ideas will be presented and released. It will be used as basis for our discussion.