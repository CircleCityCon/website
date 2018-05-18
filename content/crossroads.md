---
title: "Crossroads"
menu: "main"
featured_image: "/images/minox.jpg"
linktitle: "Crossroads"
html_description: "yes"
description: >
  <img src="/images/crossroads.jpg" style="width:100%;height:auto">/>
  <div class="items-center center">

  <div class="items-center center">
    <ul class="pl0">
      <li class="list f4 f5-m fw4 dib-ns pr5 font-spy">
        <a class="dim no-underline white-90 baffle" href="/schedulecr">Crossroads Schedule</a>
      </li>
      <li class="list f4 f5-m fw4 dib-ns pr5 font-spy">
        <a class="dim no-underline white-90 baffle" href="/sponsorscr">Crossroads Sponsors</a>
      </li>
---

This year marks the launch of our inaugural CircleCityCrossroads. This is an executive summit, which is a joint partnership between CircleCityCon, Infragard, and ISSA.The summit will occur the day before the regular CircleCityCon conference.


If you are a C-level, Vice-President, or Executive Director with IT or Information Security as your domain, we welcome you to join us for a day of networking, talks, panels, and executive round table discussions about topics that matter most to you!


{{< button name="Get tickets" href="https://www.eventbrite.com/e/circlecity-crossroads-tickets-43491785100" faicon="ticket" >}}

[{{<figure src="/images/bios/crossroad.keynotes.jpg" class="center w-50-ns">}}][tic]

### Sponsors



### Agenda

<script>
  function getDocHeight(doc) {
    doc = doc || document;
    // stackoverflow.com/questions/1145850/
    var body = doc.body, html = doc.documentElement;
    var height = Math.max( body.scrollHeight, body.offsetHeight, 
        html.clientHeight, html.scrollHeight, html.offsetHeight );
    return height;
  }

  function setIframeHeight(id) {
    var ifrm = document.getElementById(id);
    var doc = ifrm.contentDocument? ifrm.contentDocument: 
        ifrm.contentWindow.document;
    ifrm.style.visibility = 'hidden';
    ifrm.style.height = "10px"; // reset to minimal height ...
    // IE opt. for bing/msn needs a bit added or scrollbar appears
    ifrm.style.height = getDocHeight( doc ) + 4 + "px";
    ifrm.style.visibility = 'visible';
  }
</script>

<div class="min-vh-100">
  <iframe
    id="scheduleFrame"
    class="db ma0 flex flex-wrap min-vh-100 absolute right-2"
    style="width: calc(100% - 70px)"
    frameborder="0"
    onload="setIframeHeight(this.id)"
    src="https://circlecitycrossroads2018.busyconf.com/schedule"
    ></iframe>
</div>
