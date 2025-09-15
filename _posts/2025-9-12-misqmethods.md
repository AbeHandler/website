---
layout: post
title:  'How do you write a "Methods Article" for MIS Quarterly?' 
date:   2025-09-12 12:00:53-0400
categories: MISQ
---


How do you write a "Methods Article" for MIS Quarterly?

To investigate, I wrote a script to find all the methods papers which have ever been published at the journal. These are listed under the heading "Methods Articles" in the MISQ archive online.

My search turned up 10 papers, dating back to 2015. That means that MISQ publishes methods articles at a rate of roughly 1 per year. These papers are pretty rare.

Beyond their frequency, I noticed that many papers in the set follow a basic structure, which could serve as a template for would-be submissions.

The papers (1) lay out a fundamental methodological problem (2) propose some solution to that problem and then (3) somehow evaluate or demonstrate the solution. I'm going to analyze each step [1].

<style>
  table {
    border-collapse: collapse;
    width: 100%;
  }

  th, td {
    border: 1px solid #000;
    padding: 12px !important;
    text-align: left;
    vertical-align: top;
  }

  th.paper-column, td.paper-column {
    width: 250px;
  }

  tbody tr:nth-child(even) {
    background-color: #f9f9f9; /* optional for readability */
  }
</style>

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th style="width: 180px;; padding: 10px;">Paper</th>
      <th style="padding: 10px;">Problem</th>
      <th style="padding: 10px;">Solution</th>
      <th style="padding: 10px;">Evaluations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Goodhue et al. (2017)</td>
      <td>Multicollinearity and measurement error lead to false positives in multiple regression</td>
      <td>A correction procedure</td>
      <td>Monte Carlo simulation</td>
    </tr>
    <tr>
      <td>Schecter et al. (2022)</td>
      <td>A gap between objective social network traces and subjective perceptions of a social network leads to measurement error in network analysis</td>
      <td>An improved estimator</td>
      <td>Monte Carlo simulation, lab study, case study</td>
    </tr>
    <tr>
      <td>Larsen & Bong (2016)</td>
      <td>Different constructs have different names in the literature which makes it hard to build cumulative knowledge</td>
      <td>NLP to identify overlapping constructs</td>
      <td>Controlled experiment with researchers, ML metrics</td>
    </tr>
    <tr>
      <td>Tuunanen et al. (2024)</td>
      <td>DSR projects are complex, they evolve through time, and they may involve multiple artifacts</td>
      <td>The eDSR method for design science</td>
      <td>Controlled experiments with researchers, interviews, expert panel</td>
    </tr>
    <tr>
      <td>Benjamin et al. (2019)</td>
      <td>Conducting research from Darknet forums introduces special research challenges </td>
      <td>The DICE-E framework for Darknet research</td>
      <td>Case studies</td>
    </tr>
    <tr>
      <td>Shin et al. (2020)</td>
      <td>Analyzing content on social media requires domain knowledge, manual coding, and methodological expertise</td>
      <td>Diverse ML methods such as word embeddings and CNNs</td>
      <td>ML metrics, case studies</td>
    </tr>
    <tr>
      <td>Park et al. (2020)</td>
      <td>In QCA, multiple theories can explain the same phenomenon, and a single theory can apply in different situations</td>
      <td>A framework for applying QCA</td>
      <td>Case studies</td>
    </tr>
    <tr>
      <td>Compeau et al. (2022)</td>
      <td>Technology changes quickly. IS should strive for a cumulative tradition, but IS constructs from the past may not be appropriate for current tech.</td>
      <td>A process to update constructs</td>
      <td>Case studies</td>
    </tr>
  </tbody>
</table>


<h3 style="margin-top: 15px;">Lay out a fundamental problem</h3>

MISQ methods papers begin by establishing some issue. For Larsen & Bong (2015), the problem is that the same construct may have different names across different studies, which makes it hard to build cumulative knowledge. For Shin et al. (2020), the problem is that analyzing content on social media requires domain knowledge, manual coding, and methodological expertise. See the table with this post.

Note that many of the proposed problems apply to research outside of IS and that the problems are also widely applicable to broad swathes of IS research. MISQ methods papers may pinpoint very specific methodological issues but the issues are relevant to broad sets of IS papers, like all DSR papers (Tuunanen et al., 2024) or all IS papers that may have correlated inputs to a linear model (Goodhue et al., 2017).

<h3 style="margin-top: 15px;">Propose some solution to the problem</h3>

Nearly all papers all propose some tool or approach for solving their problem. For example, Schecter et al. (2022) propose an estimator to address measurement error in network analysis and Compeau et al. (2022) propose a procedure for updating constructs amid technological change.

Additionally, note that the papers present techniques which are more or less fully-developed and ready to go. Many papers achieve this by extending established research streams from outside IS. For example, Shin et al. (2020) extend established work on ConvNets while Larsen & Bong (2015) extend on established work on LSA. This is a little different from CS where methods papers may make incremental progress towards a long-term goal (e.g. 2010s-era CS papers in natural language understanding). MISQ methods articles present techniques which can be usefully applied right now.

<h3 style="margin-top: 15px;">Evaluate or demonstrate the solution</h3>

Having introduced the problem and solution, MISQ methods articles proceed to some sort of evaluation or demonstration. You see a lot of different things here including Monte Carlo simulations, ML benchmark comparisons, case studies, and controlled experiments with real researchers. See the table for details.

<h3 style="margin-top: 15px;">Notes</h3>
[1] A few methods papers don't fit this framework. For example, Wiesche et al. (2017) is more like a literature review. But the bulk of MISQ methods papers fit this broad template.

