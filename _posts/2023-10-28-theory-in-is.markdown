---
layout: post
title:  "What counts as a theoretical contribution in IS?"
date:   2023-10-28 06:40:53-0400
categories: research
---


_This post is in progress, and was last updated on October 28, 2023. Please check back for updates._

IS research papers are expected to provide a *theoretical* contribution. For instance, the [ISR](https://pubsonline.informs.org/page/isre/submission-guidelines) editors state that submissions "should have a strong grounding in theory," meaning they offer "pure theory," tests or illustrations of theory or applications of existing theory. Similarly, the [MISQ](https://misq.umn.edu/categories-lengths) editors suggest that authors should "ground their work in theory," by advancing new theories or "testing an existing theory."  

There are [many](https://misq.umn.edu/skin/frontend/default/misq/pdf/TheoryReview/EdCommentsV22I2.pdf), [IS](https://misq.umn.edu/skin/frontend/default/misq/pdf/TheoryReview/WebsterWatson.pdf), [papers](https://misq.umn.edu/skin/frontend/default/misq/pdf/EdComments/edcommentsv38n2.pdf) on this, including a [canonical](https://misq.umn.edu/skin/frontend/default/misq/pdf/TheoryReview/Gregor.pdf) paper from Gregor. But I wanted to approach this more empirically, to gain a more systematic and empirical perspective on the current conventions in IS. What are the theoretical contributions in recent papers, published in MISQ and ISR? What do the authors and editors mean by theory? Note: I picked the papers in this post pretty haphazardly, based on what seemed interesting.

### Theory as literature review

One definition of theory seems to mean something like, doing a good job on your [literature review](https://sites.umiacs.umd.edu/elm/2019/02/22/writing-the-literature-review/). An example of a paper which matches this definition of theory is the recent econ-focused ISR paper ["Is a College Education Still Enough?"](https://pubsonline.informs.org/doi/epdf/10.1287/isre.2021.0391) This paper has a "Literature and Theory" section, which, from a CS perspective, reads like more or less like a literature review. The authors ground their investigation into how automation will affect workers with different skills by reviewing prior work on task on IT and labor, task routineness and artificial intelligence. The lit review then ends with a "research framework" which formalizes their research question along two dimensions (education and routineness); this is a slight deviation from a lit review in CS which would not include the author's work.

### Theory as quantitative model of behavior

A recent [ISR paper](https://pubsonline.informs.org/doi/abs/10.1287/isre.2021.0153) from Brynjolfsson et al. proposes a new quantitative model of how to measure the value of free goods on the Internet. The authors observe that people pay a fixed money cost for a home internet connection, but get utility from online leisure activities with no money cost such as playing (free) video games. They note that this utility would not be measured with traditional ways of computing the value of goods and services in an economy such as GDP. Thus the authors lay out seven underlying assumptions (e.g., the primary cost of Internet goods is time rather than money), and on the basis of these assumptions they propose a quantitative model of how to value free online goods. They describe this as a "Theoretical Framework" for "Measuring Welfare Gain from the Internet." In this case, the theory is a quantified new way to think about some phenomenon.

### Theory as term in an equation

Some machine learning or statistics-oriented IS papers appeal to theory to justify or contextualize a term in an equation. One example of a paper like this is ["Who's watching TV?"](https://pubsonline.informs.org/doi/abs/10.1287/isre.2023.1204) This paper presents a graphical model that tries to determine which members of a household are actually watching a TV program. This is a research problem because TV ratings agencies like Nielsen can only observe if a single TV in a house is tuned to a program; they can't observe which member of the household is actually watching a show. The authors propose modeling the household-level probability that a TV is turned to a given segment using a logistic function which accepts input parameters reflecting (1) the estimated influence of each household member over TV watching and (2) the estimated affinity of each household member for a given TV program. The authors justify the influence and affinity terms in this equation by appealing to theories of market segmentation (i.e., people with similar social roles like similar kinds of shows), and by appealing to prior work showing that TV watching is a social process (e.g., one spouse can influence another's viewing). In this case, theory is used to justify or contextualize particular mathematical choices in specific equations in a model.

### Extending a named theory

Another pattern is taking a theory with a name, and extending it. I will add examples on this soon.
