---
layout: page
title: Lecture 20 – Decision Trees
nav_exclude: true
---

# Lecture 20 – Decision Trees

by Josh Hug (Fall 2019)

- [slides](https://docs.google.com/presentation/d/1xX7pgDP4e4c77LiKQ_tqDDmxwQA0Q2cAlECxRGXqGFE/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfrUv0_xuQJ3k7yySAQzcyDz)
- [code](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/su20&subPath=lecture/lec20/)
- [code HTML](../../resources/assets/lectures/lec20/lec20.html)

**Important:** This lecture is taken from the Fall 2019 semester.
- The reference to Lecture 22 in 20.1 should be a reference to Lecture 19.
- The references to lec25-decision-trees.ipynb in 20.1 should be references to lec20-decision-trees.ipynb.
- The slides in 20.4 should say: "Bagging often isn’t enough to **reduce** model variance!" Without selecting a random subset of features at each split, the decision trees fitted on bagged data often look very similar to one another; this means that they make similar predictions. As a result, the ensemble of decision trees would still have low bias and high model variance. Selecting a random subset of features at each split helps reduce model variance by making the decision trees in the ensemble different from one another.

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
<td><strong>20.1</strong> <br>Decision tree basics. Decision trees in scikit-learn.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/nqcEANdM7cs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/7WuDLnpAVo2SCb9JA" target="\_blank">20.1</a></td>
</tr>
<tr>
<td><strong>20.2</strong> <br>Overfitting and decision trees.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/JIsgfg5yYg4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/7osYjEQzgMnri73aA" target="\_blank">20.2</a></td>
</tr>
<tr>
<td><strong>20.3</strong> <br>Decision tree generation. Finding the best split. Entropy and weighted entropy.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/YnIF85z8VpU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/xRsf1vPzfVcSEyyaA" target="\_blank">20.3</a></td>
</tr>
<tr>
<td><strong>20.4</strong> <br>Restricting decision tree complexity. Preventing growth and pruning. Random forests and bagging.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/qSek1nevadY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/2KWofVqn5oqwGPPdA" target="\_blank">20.4</a></td>
</tr>
<tr>
<td><strong>20.5</strong> <br>Regression trees. Summary of decision trees, classification, and regression.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/8mi5NZAOgXI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/oJHhPt1wCJTNmgVb8" target="\_blank">20.5</a></td>
</tr>
