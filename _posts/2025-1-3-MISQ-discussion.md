---
layout: post
title:  "What goes in an MISQ discussion section?"
date:   2025-01-03 13:40:53-0400
categories: MISQ
---

I wanted to understand how MISQ authors end their papers. So I analyzed each "Discussion" section in the September 2024 edition of the journal. From this analysis, I found that nearly every group of authors touched on the following topics, often in the following order:

1. **Recap**: Quickly review the paper.
2. **Research Contributions**: What are the main scholarly takeaways?
3. **Implications for Practice**: What does the paper mean for practitioners?
4. **Limitations and Future Work**: How can scholars build on the paper?

To help show these commonalities across abstracts, I coded each paragraph in each discussion using this 4-part taxonomy. Then I used that coding process to create the following visualization. I also describe each of the four paragraph types in detail below.

_Note: this analysis follows similar analysis of MISQ [intros](https://www.abehandler.com/blog/2024/MISQ-intros/) and [abstracts](https://www.abehandler.com/blog/2024/MISQ-abstracts/)._

<!-- Include CSS -->


<!-- Include JS -->
<script src="https://d3js.org/d3.v7.min.js"></script>
<p><div id="d3-visualization"></div></p>

<link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap" rel="stylesheet">
<link rel="stylesheet" href='https://s3.us-west-2.amazonaws.com/www.abehandler.com/css/misqconclusionsstyle.css'>

<script src="https://s3.us-west-2.amazonaws.com/www.abehandler.com/js/misqconclusions.js"></script>



# Recap
Many MISQ discussion sections start with a few recap paragraphs which summarize the work. Notice how each row begins with one or more purple dots. Recaps also tend to mention theoretical perspectives, connections with prior literature, experimental details, research gaps, core research questions, and motivations for the work itself. For these reasons, recaps tend to look a lot like MISQ [abstracts](https://www.abehandler.com/blog/2024/MISQ-abstracts/), which tend to cover similar material. I think the differences between abstracts and recaps are a little subtle, and really digging into those differences could be the topic of its own post. But my sense is that recaps tend to focus a little more on the findings of the paper ("what we found") and a little less on the formal procedures of the work ("what we did"). 

I also noticed that very often the first sentence of the recap starts with something like "Our study" or "This study." It gives a 1-line summary of the work. Here are a few examples.
- "Our study investigates how sharing electronic health data via health information exchanges (HIEs) affects hospitals’ data breach risk … "
- "This study examines the spillover effect of bot-assisted fake social engagement (FSE) … "
- "Our research developed a behavioral measure … "

# Research contributions
After providing a recap, nearly all discussion sections list a study's research contributions (orange dots). Some authors divide these into empirical, theoretical, and methodological contributions. But for simplicity, I lump these different types of research contributions together under one code.

One very common pattern is to enumerate contributions across paragraphs, with one contribution per paragraph. For example, Kitchens et al., list four research contributions across four paragraphs (P1-P4). They write: 

- **P1**: First, we show that theory-guided social listening artifacts can seamlessly combine relevance, credibility, and cross-channel landscape …
- **P2**: Second, through our design process, we develop and propose an extension to existing activity theory literature … 
- **P3**: Third, in designing our artifact, we contribute to the knowledge on graph neural networks through two novel extensions to this methodology …
- **P4**: Fourth, we show that in dynamic environments involving machine learning applied to complex user-generated content …

# Implications for practice
Many MISQ papers list implications for practitioners (pink dots). This material tends to come after research contributions.
For example, Wilson et al. develop a way to measure usability based on mouse movements. In their section on implications for practice, they emphasize that their new measure can be collected unobtrusively without making users take a survey. Similarly, Kitchens et al. describe their deployment of their system with a pharmaceutical manufacturer. They highlight how their work shows quantifiable gains in precision and recall.
As with research contributions, many authors tend to enumerate implications for practice paragraph-by-paragraph. See Q. Chen et al. or X. Chen et al. for examples of this pattern.

# Limitations and future work.
Finally, many studies list limitations and future work at the end of a discussion section (green dots). It is very common for authors to first describe a limitation, and then explain how it might be addressed in future work. Here are some examples:

- X. Chen et al. say they focus only on Airbnb and Fiverr. They call for more research on other platforms.
- Y. Li et al. say they study the impact of "confidence cues" at a group level. They call for more research at an individual level.
- In a computational paper, Kitchens et al. say they only focus on text. They call for research on audio and video.

Note that this tendency to list limitations and future research together is not universal. Gomez and Palomas list these two things separately.

# Generalization
A few papers discuss possible ways to generalize the contributions from their study. For example, Kitchens et al. explain how their work on a social media listening system for public health might extend to other contexts such as marketing or crisis management. Similarly, D. Zhang et al. explain how their proposed model might be applied to other kinds of online forums. 

Mentioning generalization is not that common in MISQ discussion sections, so I did not assign it a color code. But it seems like a nice thing to include. How does this study apply to other contexts?

# Conclusion

Discussion sections usually come at the conclusion of an MISQ article and sometimes go under the heading "Discussion and conclusion." So a few discussion sections end with a concluding paragraph that sums the work using a sub-heading like "Conclusion." Having a conclusion sub-section seems to be optional. I did not assign it a code. Most discussion sections already start with a recap. So including an additional conclusion may not be needed. See Lee et al. and Wilson et al. for examples of papers that include a short conclusion.
