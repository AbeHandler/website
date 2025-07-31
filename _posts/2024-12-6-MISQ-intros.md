---
layout: post
title:  "What goes in an MISQ intro?"
date:   2024-12-06 13:40:53-0400
categories: MISQ
---

In this post, I break down 11 MISQ introductions paragraph-by-paragraph to understand their [rhetorical structure](https://aclanthology.org/P19-4003/). This follows a [similar post](https://www.abehandler.com/blog/2024/MISQ-abstracts/) which focuses on abstracts.

To gain a better feel for this format, I analyzed all 11 introductions from the [September 2024](https://misq.umn.edu/contents-48-3) edition of MISQ to create a small taxonomy of seven basic paragraph types. I then created a visualization to show each paragraph from each intro, color-coded by type. Each row in the visualization represents a single paper. Each dot represents a single paragraph. On desktop, hovering reveals short snippets to help give a sense for what is happening in the underlying text. <b>If you are reading on a phone, tap the dots (instead of hover).</b>

<p><div id="d3-visualization"></div></p>

<!-- Include CSS -->

<link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap" rel="stylesheet">
<link rel="stylesheet" href='https://s3.us-west-2.amazonaws.com/www.abehandler.com/css/misqstyle.css'>

<!-- Include JS -->
<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://s3.us-west-2.amazonaws.com/www.abehandler.com/js/misqintros.js"></script>

I found this kind of paragraph-by-paragraph analysis quite helpful because it reduces the complex process of writing a MISQ intro to a sort of tetris problem. You need to write and arrange paragraphs to make a coherent argument, in a format that looks like MISQ.

I also think the visualization shows some common rhetorical patterns. In general, MISQ intros tend to introduce the domain, propose a research gap, offer a [theoretical perspective](https://www.abehandler.com/blog/2023/theory-in-is/), explain what the researchers did, explain what the researchers found, and then comment on the contributions or ramifications of the work. Each of these steps usually takes somewhere from one to three paragraphs, and not all papers include each step.

Here are the seven paragraph types.


# Type 1: The Domain
MISQ intros start by introducing the domain (brown). Every single intro starts with one or more domain paragraphs. You can see this very clearly in the visualization.

Note that there is some variation in how long it takes to introduce the domain. Sometimes it takes 1 paragraph, like the impressively concise intro from Wilson et al. But sometimes it takes a few paragraphs, especially for more specialized topics. For instance, Li et al. use 4 brown paragraphs to explain the specific phenomenon of overfunding in crowd investing.

# Type 2: The Gap
After introducing the domain, many MISQ intros include paragraphs describing a research gap (pink). A research gap paragraph explains what is missing from the existing literature in the domain. Notice they tend to come early in the intro, right after domain paragraphs. Many rows go from brown to pink.

Note: computational papers like Kitchens et al. often describe "baseline" methods for solving problems early in the intro. I initially assigned these paragraphs with their own "baseline" code. But arguably "baselines" are actually a special (computational) case of the broader phenomenon of gaps. So I re-coded baselines as gaps.

# Type 3: The question
Sometimes MISQ intros contain a paragraph that directly states the research question (purple). For example, X. Chen et al. have a paragraph that asks "When should a decentralized P2P platform adopt BRS?" Not all intros have state the research question this directly. Look for the ones with purple dots. If the authors directly state a research question this tends to come midway through the intro.

# Type 4: The theoretical perspective
Theory is a [big part](https://www.abehandler.com/blog/2023/theory-in-is/) of IS. After introducing the domain, describing a gap, and sometimes stating a research question, many papers start to detail a theoretical perspective (dark green). Notice that introducing theory typically only takes one or two paragraphs, and usually comes somewhere in the middle of the introduction. Many papers will expand this short description with a longer "theory" section later on in the paper. The authors are signaling: we have theory ✔, keep reading for more.

# Type 5 and 6: What they did / what they found

These paragraph types are the most straightforward. I think they are common to most academic intros. The paragraphs describe what was done in the paper (yellow) and what the authors learned from the analysis (brown). For example, X. Chen et al. have a paragraph that explains development of an analytical model, and then a paragraph that describes what they learn about buyers and sellers from this analysis. Obviously, in the visualization, yellow tends to come before brown.

# Type 7: Contributions or insights
Many papers end by listing the contributions and insights of the paper (light green), often for managers and practitioners. These paragraphs basically say: here are the broader takeaways from our study. Many intros end this way. Notice that most rows end with a light green dot.

