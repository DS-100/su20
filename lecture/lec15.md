---
layout: page
title: Lecture 15 – Bias-Variance Tradeoff
nav_exclude: true
---

# Lecture 15 – Bias-Variance Tradeoff

by Ani Adhikari (Spring 2020)

- [slides](TODO)
- [video playlist](TODO)
- [code](TODO)
- [code HTML](TODO)

**Important:** This lecture is a combination of two lectures from Spring 2020 (this is why the video titles don't match our numbering). Read this before proceeding with the lectures, as it details which concepts you should focus on.

Sections 14.1 through 14.4 discuss the core techniques of feature engineering. Slides are linked above, and code is in "Part 1" and "Part 2".
- 14.1: Throughout this lecture, Radial Basis Functions are used as an example. For our purposes, they are purely an example, and are not in-scope.
- 14.2, 14.3: Entirely in scope.
- 14.4: Of the three techniques discussed, one-hot encoding is most important, though the others are still in scope.

Sections 14.5 through 14.7 discuss pitfalls to be aware of in feature engineering. There are no accompanying slides; these ideas are primarily explained in the lecture notebook "Part 3".
- 14.5: Focus on the numerical ideas here, not the syntax of model creation (though the code is linked above).
- 14.6: The focus of this video is about the content at the end where our design matrix has too many columns, not about the details of Radial Basis Functions.
- 14.7: See the above comment.


<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Video</th>
<th>Quick Check</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>14.1</strong> <br>A demonstration of how to use scikit-learn to fit linear models.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/lFzRiinHSzU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScKoxVcZBawfS7huMrIfguFDihAa8GOs6dFzjPMVFRHEbKtbA/viewform" target="\_blank">14.1</a></td>
</tr>
<tr>
<td><strong>14.2</strong> <br>Feature functions, as a method of transforming existing numerical data, and encoding non-numerical data for use in modeling.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/ET44iB169no" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScdIJF200dACeKi47uCOdtXpx9ZV8BawB03QHmVDwCUpHXcRw/viewform" target="\_blank">14.2</a></td>
</tr>
<tr>
<td><strong>14.3</strong> <br>Defining what it means for a model to be linear. The constant feature. More sophisticated numerical features.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/moL6aeW94Ps" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeKjj41pgvhV9lYJqQPf-_6P5oi5j1OU5CtWHnUQYWIdKUZuw/viewform" target="\_blank">14.3</a></td>
</tr>
<tr>
<td><strong>14.4</strong> <br>Numerically encoding categorical data using various encodings (one-hot, bag of words, n-gram).</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/y6mxtlWYo54" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSf72ZwGrseAT1C47zyO93HfgJUjCKGtMcgfHBdyMm87Hmnpig/viewform" target="\_blank">14.4</a></td>
</tr>
<tr>
<td><strong>14.5</strong> <br>Issues we may run into when our design matrix has redundant features.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/M11bB0Yd2is" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSe9A87MKY7IPQ1Se4U9T3j2J1XMWO3eVDfZqEStZm9D7v0Uww/viewform" target="\_blank">14.5</a></td>
</tr>
<tr>
<td><strong>14.6</strong> <br>Issues we may run into when our design matrix has more features than observations. Radial basis functions.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/iwbqbPg740I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdsXmKzKcZOqR5ezNf-5wb8My53BvSME7fhTw4hNqmc4Kjr3Q/viewform" target="\_blank">14.6</a></td>
</tr>
<td><strong>14.7</strong> <br>Overfitting our model to the data we used to train it leads to poor generalizability to unseen data, which is the goal of modeling.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/b6l9eVGERxY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScNQA-sJ8DIjiTagysbF_OCLts86pcdIz2TRRDGR4bPRSCLUw/viewform" target="\_blank">14.7</a></td>
