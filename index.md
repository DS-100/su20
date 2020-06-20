---
layout: page
title: Home
nav_order: 1
description: A week-to-week description of the content covered in the course.
---

# Principles and Techniques of Data Science
{: .mb-2 }
UC Berkeley, Summer 2020
{: .mb-0 .fs-6 .text-grey-dk-000 }

<div>

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
<div class="role">
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %}

</div>

<ul>
<li>All announcements are on <a href="http://piazza.com/berkeley/summer2020/data100">Piazza</a>. Make sure you are enrolled and active there.</li>
<li>The <a href="{{ site.baseurl }}/syllabus">Syllabus</a> contains a detailed explanation of how each course component will work this summer, given that the course is being taught entirely online.</li>
<li>The scheduling of all weekly events is in the <a href="{{ site.baseurl }}/calendar">Calendar</a>.</li>
<li><b>Zoom links for live events:</b> <a href="https://piazza.com/class/kbe580u9fbd2d5?cid=11">@11 on Piazza</a>.</li>
</ul>

<br><br>

{% for module in site.modules %}
{{ module }}
{% endfor %}
