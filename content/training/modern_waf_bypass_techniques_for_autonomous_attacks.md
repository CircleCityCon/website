---
title: "Modern WAF Bypass Techniques for Autonomous Attacks"

---

Scripting and automation are absolutely critical to many aspects of an attacker’s effectiveness, penetration tester or otherwise. Modern WAFs and “bot detections” often add a small layer of intelligence to their monitoring, attempting to determine whether or not an attack is being automated, and shut the bot/botnet down. This class will cover how common forms of WAF & bot detections work and how you can modify your scripting to fly under the radar.

**Class Structure:**

Instruction will be extremely hands-on, targetting a live website with common protections in place. Students are expected to have enough knowledge in Python and/or Javascript (both are preferred, JS is absolutely required) to be able to write basic scripts for accessing data via HTTP, as this will be a "we all teach each other" style of course. Students will be tasked with writing their own scripts using the recommended techniques and demonstrate their methodologies to the rest of the class.

**Syllabus:**

Goal: To teach how common forms of WAF & bot detections work and subsequently, how you can modify your scripting to fly under the radar.

Time: 4 hours

1. Overview ( 45 min )

 1. WAF Bypass Talk, geared towards class goals
 
 2. Syllabus review
 
 3. Describe Target Site and Goals
 
 4. BREAK
 
2. Hands On

 1. Goals: Scrape data, test credentials, evade capture
 
  1. How to scrape with Python (Requests)
  
  2. How to scrape with JS Evasion Techniques (1.5 hours)
  
 2. Basic Evasion techniques
 
  1. Randomized Request timing
  
  2. IP rotation via proxy (scrape from didsoft.com) Headers
  
  3. Headers
  
   1. rotation
   
    1. User Agents
    
     1. Scrape UA list from 
     http://useragentstring.com/pages/useragentstring.php?name=All
     
    2. Other Headers 
    
   2. Case sensitive headers
   
  4. Cookies
  
   1. Session Cookies
   
 3. BREAK (10 min)
 
 4. Advanced Evasion (1.5 hours)
 
  1. REQUIREMENTS:​ Puppeteer, NodeJS, Chromium, NPM, IDE
  
  2. Understanding the opposition
  
   1. Identifying bot detection tools
   
    1. Attempt to load the site a number of times with:
    
     1. Non-JS executing script
     
     2. Selenium / Puppeteer
     
   2. Understanding what they're looking for
   
    1. Reverse Engineering JavaScript
    
     1. Take a piece of obfuscated JS
     
     2. Understand what checks are being run
     
     3. JSNice.org
     
     4. Basic reversing techniques
     
  3. Headless / Headful chrome w/ Puppeteer
  
    1. Pass some of the following, key checks
    
      1. https://bot.sannysoft.com/

Requirements:
 
* Windows. MacOS or Linux laptop & permission/ability to install software (i.e. Python, node.js, Webstorm or other IDE(if desired)) and create new network interfaces (VPN, etc).

* Basic ability to write Python and Javascript for the purposes of automating HTTP requests

* General knowledge of the HTTP protocol (basic webapp functionality, how headers work)

* Ability and desire to present and explain one’s own work to a small group


* **SPEAKER** [Sam Crowther](/bios/sam_crowther)

* **SPEAKER** [Johnny Xmas](/bios/johnny_xmas)
