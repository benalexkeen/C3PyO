---
layout: page
title: Archive
desc: Find an archive of all our posts here. Every year I try to write more and more useful content on WebJeda. So this is where you can see what all the things I wrote on every single year!
permalink: /archive/
adallow: 0
---

<section id="archive">
<h2>Articles from this year</h2>
{% for post in site.posts %}
  {% unless post.next %}

  <ul class="this">
  {% else %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% capture nyear %}{{ post.next.date | date: '%Y' }}{% endcapture %}
  {% if year != nyear %}
  </ul>
  <h2>{{ post.date | date: '%Y' }}</h2>

  <ul class="past">
  {% endif %}
  {% endunless %}
 <li class="arch-list"><a href="{{site.baseurl}}{{ post.url }}">{{ post.title }}</a>&nbsp;<time>{{ post.date | date:"%d %b" }}</time></li>
{% endfor %}
  </ul>
</section>