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

See the <a href="{{ site.baseurl }}/calendar">Calendar</a> to see the scheduling of our weekly events. Also, see the <a href="{{ site.baseurl }}/syllabus">Syllabus</a> for a detailed explanation of how each course component will work this summer, given that the course is being taught entirely online. 

<br><br>

{% for module in site.modules %}
{{ module }}
{% endfor %}
