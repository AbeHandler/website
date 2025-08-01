---
layout: default
permalink: /blog/
title: Blog
nav: true
nav_order: 1
---

<div class="post">
  
  <ul class="post-list">
    {% for post in site.posts %}
    <li>
      <h3>
        {% if post.redirect == blank %}
          <a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a>
        {% elsif post.redirect contains '://' %}
          <a class="post-title" href="{{ post.redirect }}" target="_blank">{{ post.title }}</a>
        {% else %}
          <a class="post-title" href="{{ post.redirect | relative_url }}">{{ post.title }}</a>
        {% endif %}
      </h3>
      <p>{{ post.description }}</p>
      <p class="post-meta">
        {{ post.date | date: '%B %d, %Y' }}
      </p>
    </li>
    {% endfor %}
  </ul>
</div>