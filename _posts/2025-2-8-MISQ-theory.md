---
layout: post
title:  "What goes in an MISQ theory and hypothesis section?"
date:   2025-02-08 13:40:53-0400
categories: MISQ
---

<style>
  .responsive-image {
    width: 100%; /* Make the image responsive: It will never be larger than its container */
    max-height: 500px; /* Maximum size for larger screens */
  }

  @media (max-width: 768px) {
    .responsive-image {
      max-width: 320px; /* Smaller size for mobile devices */
    }
  }
</style>


This post introduces a two-step visual approach to breaking down traditional theory sections in MISQ papers, which often contain numbered hypotheses (e.g., H1).[^types]
I hope the procedure will help those learning to read and write for MISQ.
The two steps are:

- <u>Step 1</u>: Skip to the first hypothesis statement (H1). The statement will often answer two questions:
	- **What** constructs do the authors include in their model (e.g., X and Y)?
	- **How** are those constructs empirically related (e.g., X increases Y)?

   <div style="margin-top: 3px; margin-bottom: 10px;">Visually, you can represent the answers to what and how using a diagram known as a DAG (see below).</div>
- <u>Step 2</u>: Flip to the start of the theory section. The text leading up to H1 will often answer:
	- **Why** do the authors hypothesize an empirical relationship between the constructs? Often, authors will answer why using <a href="https://en.wikipedia.org/wiki/Deductive_reasoning">deductive reasoning</a>.

  <div style="margin-top: 3px">Visually, you can color-code text that supports or justifies different edges on the DAG.</div>

Together, these two steps provide a visual overview of traditional theory and hypothesis sections in MISQ papers. These sections typically build to a **what/how** hypothesis statement by deductively explaining **why** the authors hypothesize a given empirical relationship.[^jekyll]

  <i>If you find this useful, check out my other posts on MISQ <a href="https://www.abehandler.com/blog/2024/MISQ-intros/">intros</a>, <a href="https://www.abehandler.com/blog/2024/MISQ-abstracts/">abstracts</a>, and 
 <a href="https://www.abehandler.com/blog/2025/MISQ-discussion/">discussion</a> sections.</i>


[^jekyll]: The approach is based on a well-known article from David Whetten, who [breaks down management theories](https://www.cci.drexel.edu/faculty/sgasson/Readings/Whetten%5B1989%5D-WhatConstitutesATheoreticalContribution.pdf) in terms of these kinds of wh words. Also, sometimes papers have multiple hypotheses. I focus on H1.

## Step 1: Outline the first hypothesis statement using a DAG


Hypothesis statements in MISQ papers often propose empirical relationships between constructs. To make sense of these statements, I think it helps to use a diagram known as a directed acyclic graph or DAG. A DAG is a [graph](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)) (i.e. network) with nodes and edges. Nodes represent constructs. Edges represent causal relationships. Computer science and social science have a lot to say about [DAGs](https://en.wikipedia.org/wiki/Causality_(book)). But for this post, I use them as a kind of visual outline (see also [TheoryOn](https://misq.umn.edu/theoryon-a-design-framework-and-system-for-unlocking-behavioral-knowledge-through-ontology-learning.html)).

Let's look at how DAGs can help make sense of hypothesis statements using a paper from the September 2024 edition of the journal. Towards the end of their theory section, [Wilson et al.](https://misq.umn.edu/behaviorally-measuring-usability-by-analyzing-users-mouse-movement-efficiency.html) write: _"H1: Users of interfaces with lower usability will have lower mouse movement efficiency than users with higher usability."_ 
 This description of what and how can be concisely represented as a DAG, which shows that usability affects mouse movement efficiency.


<p align="center">
<img src="https://s3.us-west-2.amazonaws.com/www.abehandler.com/images/blogimages/dag1.png" alt="Example Image" class="responsive-image">
</p>




On their own, DAGs (aka hypotheses) are not full-fledged management theories. They simply assert proposed causal relationships between constructs, which is [insufficient](https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Doctoral_Resources/Sutton_Staw_What%20theory%20is%20not.pdf) for theory. Theoretically-grounded management researchers also need to explain [why](https://www.cci.drexel.edu/faculty/sgasson/Readings/Whetten%5B1989%5D-WhatConstitutesATheoreticalContribution.pdf) they express a particular hypothesis. Which brings us to Step 2.

## Step 2: Read the theory section to understand why the authors assert H1

*"Everyone who publishes in professional journals in the social sciences knows that [you are supposed to start your article with a theory, then make deductions from it](https://statmodeling.stat.columbia.edu/wp-content/uploads/2013/05/locke.pdf)."* - [Edwin Locke](https://en.wikipedia.org/wiki/Edwin_Locke)[^bb]

[^bb]:After making this declaration, Locke tries to build a case for inductive rather than deductive theorizing. He traces the [hypothetico-deductive](https://en.wikipedia.org/wiki/Hypothetico-deductive_model) model in management back to [Karl Popper](https://en.wikipedia.org/wiki/Karl_Popper). I have thoughts. But in this post, we are not arguing about scientific methods or philosophy of science. We are trying to understand what is written in MISQ.

Hypothesis statements come towards the end of a theory section. After reading the hypothesis statement, I find it helps to flip back to the start of a theory section and then read forward to H1. Often, the text will lay out some form of deductive reasoning which explains or justifies the first hypothesis. 

Deductive reasoning describes the process of drawing specific conclusions using general principles. When MISQ authors apply deductive reasoning, they assert things which are thought to be true in general, based on broader theoretical perspectives. Then they reason on the basis of these more general principles or findings to make predictions about outcomes in a specific study context. 

For example, in their theory section Wilson et al. explain H1 by introducing Biased Competition Theory. As I understand it, biased competition theory proposes that different cognitive processes compete for limited attention. When people perceive distracting or confusing stimuli, it causes a form of competition known as attentional interference. 

Note that Biased Competition Theory describes a relationship between stimuli and attention in general. But the authors specifically hypothesize about computer system usability in particular. In other words, they use general principles from Biased Competition Theory to hypothesize about the specific case of usability.

To make this point, let's formally lay out their deductive argument which has a [fancy latin name](https://en.wikipedia.org/wiki/Modus_ponens). It goes:

- If people are presented with distracting stimuli it causes attentional interference ($$P → Q$$)
- Interfaces with poor usability present distracting stimuli ($$P$$)
- Therefore, poor usability causes attentional interference (therefore $$Q$$)

Notice that this argument introduces a new construct, attentional interference. I am going to add the new construct to our DAG below. To show this connection visually, I'm also going to use purple to highlight the portion of the theory section that deduces the relationship between usability and attentional interference.

<p align="center">
<img src="https://s3.us-west-2.amazonaws.com/www.abehandler.com/images/blogimages/dag2.png" alt="Example Image"  class="responsive-image">
</p>

So far the authors have explained how usability affects attentional interference. They still have to explain what attentional interference has to do with mouse movement efficiency. (Notice the DAG above is missing an arrow). If you keep reading through the section, the authors use a theory called "RAM" ([response activation model](https://www.tandfonline.com/doi/abs/10.1080/02724980343000666)) to explain this connection.

As I understand it, RAM proposes that stimuli will prime muscle movements (e.g. hand motions) towards or away from a stimulus. When people pay attention to different things, they have to use [top-down processing](https://en.wikipedia.org/wiki/Pattern_recognition_(psychology)) to select the target stimulus from among different options. For brevity, I am not going to outline the deductive argument like I did above. It's pretty similar, and I suggest outlining it on your own. This line deductive reasoning (shown in green) introduces and justifies a new edge in the DAG. 

<p align="center">
<img src="https://s3.us-west-2.amazonaws.com/www.abehandler.com/images/blogimages/dag3.png" alt="Example Image"  class="responsive-image">
</p>


In total, the text of the theory section explains why poor usability should reduce mouse movement efficiency. We can concisely represent this in a final DAG, like this.

<p align="center">
<img src="https://s3.us-west-2.amazonaws.com/www.abehandler.com/images/blogimages/dag5.png"  class="responsive-image">
</p>

## Recap

OK. So hopefully at this point I have convinced you that this is a good way to parse theory and hypothesis sections. I think there are a few key takeaways. 
- A typical MISQ hypothesis statement often explains **what** constructs are in a theory, and **how** they are empirically related.
	- These what and how relationships can be outlined visually with a DAG.
- The text of a theory and hypothesis section explains the **why** behind the hypothesis.
	- Often authors explain why using deductive reasoning. They reason about expected outcomes in specific circumstances by appealing to general principles or theoretical frameworks.
  - To show this visually, you can highlight the text that justifies a given edge on the DAG.
- Together, this means that H1 and the text of the theory section are tightly integrated. The text of a theory section builds to H1.


## A few more examples


In an effort to convince you that this approach explains more than one paper, I will review a few more DAGs from the <a href="https://misq.umn.edu/contents-48-3">September 2024 edition of MISQ</a>. The analysis will be shorter than what I did for Wilson because this post is already pretty long. But you can check my work by looking at the underlying articles in the September 2024 edition of the journal.


#### Kim et al.

**Step 1**: The initial DAG from H1 looks like this

<p align="center">
<img src="https://s3.us-west-2.amazonaws.com/www.abehandler.com/images/blogimages/3a.png" alt="Example Image" class="responsive-image">
</p>


**Step 2**: Early in the theory section, the authors explain that notification legislation provides information which triggers institutional pressures which lead to reduced security breaches. This can be represented as a DAG like this.

<p align="center">
<img src="https://s3.us-west-2.amazonaws.com/www.abehandler.com/images/blogimages/3b.png" alt="Example Image"  class="responsive-image">
</p>

If you look closely at this paper, you will notice that the authors sometimes use a slightly different form of deductive reasoning than what we saw in Wilson. They use prior work (i.e., citations) to argue that a general class of empirical antecedents tends to lead to similar consequences. This flavor of deductive reasoning is a topic for another post. But by the end of the section, the authors use several different deductive strategies to lay out a DAG like this.


<p align="center">
<img src="https://s3.us-west-2.amazonaws.com/www.abehandler.com/images/blogimages/3c.png" alt="Example Image"  class="responsive-image">
</p>


#### Lee et al.


**Step 1**: The initial DAG from H1 looks like this


<p align="center">
<img src="https://s3.us-west-2.amazonaws.com/www.abehandler.com/images/blogimages/daglee.png" alt="Example Image" class="responsive-image">
</p>


**Step 2**: In this case, the text of the theory section uses a purely deductive argument to justify H1. It goes:

1. Media affects audiences by directing their attention (i.e. agenda setting theory)
2. Disinformation actors distort media through fake social engagement
3. Therefore fake social engagement affects public attention to news


#### Try it yourself
Ok this is a long post. If you are still with me, I suggest writing out more DAGs by reading theory sections in MISQ papers. If you notice other broad patterns in MISQ theory, please send me a comment or email. I am keeping track. 


[^types]: The term "theory" sometimes has [different](https://pubsonline.informs.org/doi/10.1287/isre.2024.editorial.v35.n2) [meanings](https://pubsonline.informs.org/doi/10.1287/isre.2024.editorial.v35.n3) in Information Systems. This two-step approach is most suited to traditional theory sections with numbered hypotheses (e.g. H1).



