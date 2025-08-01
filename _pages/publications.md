---
layout: page
permalink: /publications/
title: Publications
description: Conference and workshop papers.
years: [2025,2024,2022,2019,2018,2017,2016]
nav: true
---

<div class="publications">

{% for y in page.years %}
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
