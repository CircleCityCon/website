---
title: "Schedule"
menu: "main"
featured_image: "/images/minox.jpg"
html_description: "yes"
description: >
  <div class="items-center center">
    <ul class="pl0">
      <li class="list f4 f5-m fw4 dib-ns pr5 font-spy">
        <a class="dim no-underline white-90 baffle" href="/socio">socio</a>
      </li>
      <li class="list f4 f5-m fw4 dib-ns pr5 font-spy">
        <a class="dim no-underline white-90 baffle" href="/bios/">bios</a>
      </li>
      <li class="list f4 f5-m fw4 dib-ns pr5 font-spy">
        <a class="dim no-underline white-90 baffle" href="/talks/">talks</a>
      </li>
      <li class="list f4 f5-m fw4 dib-ns font-spy">
        <a class="dim no-underline white-90 baffle" href="/training/">training</a>
      </li>


---

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
    src="https://ccc2018.busyconf.com/schedule"
    ></iframe>
</div>