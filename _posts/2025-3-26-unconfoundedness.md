---
layout: post
title:  'Building visual intuition for unconfoundedness' 
date:   2025-03-26 12:00:53-0400
categories: MISQ
---
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


If you have been exploring the <a href="https://mixtape.scunning.com/04-potential_outcomes">causal inference</a> literature you have likely seen the equation for unconfoundedness, which reads 

$$ \left(Y^0, Y^1\right)  \perp  T \; \vert \; X  $$

and which formally asserts that the potential outcomes $$(Y^0, Y^1)$$ are independent of the treatment $$T$$ given some covariate $$X$$.

This equation is pretty mathy. But I think it can be shown in a very simple and intuitive visual form.

The tuple on the left $$ \left(Y^0, Y^1\right)$$ represents the joint distribution of the potential outcomes $$Y^0$$ and $$Y^1$$. For example, $$y_i^0$$ might represent the total annual compensation for person $$i$$ in a given year if they do not obtain an MBA degree, and $$y_i^1$$ might represent the compensation for the same person $$i$$ in the same year if they do obtain an MBA degree (see <a href="https://pubsonline.informs.org/doi/10.1287/isre.1080.0184">Mithas and Krishnan, 2008</a>). 

If we simulate points $$ \left(y_i^0, y_i^1\right)$$ from that joint distribution we will get observations in 2-D, which we can show on an ordinary 2-D scatter plot.
In our simulated data, each point represents (1) someone's salary in a world where they <u>did</u> get an MBA along the y-axis and (2) someone's salary in a world where they <u>did not</u> get an MBA along the x-axis.
This way of thinking is kind of weird. 
It takes a second to wrap your mind around it.
So please read the paragraph above and stare at the plot below until you feel OK with what it represents.


<div style="display: flex; justify-content: center; align-items: center;">
<img src="https://i.ibb.co/whqSS827/download.png" alt="Example Image" width="300">
</div>

Of course, in reality, we will only get to observe one of these potential outcomes. For example, in real life, a person will either get an MBA or not. 
We can add that extra binary information to the plot by showing people who actually get an MBA in red.
In this case, the binary treatment variable $$T$$ is exposure to an MBA program.
In the plot below we add this additional treatment information to the scatterplot.

<div style="display: flex; justify-content: center; align-items: center;">
<img src="https://i.ibb.co/gF3kDK0d/Screen-Shot-2025-03-25-at-10-06-22-PM.png" width="300">
</div>


Now unconfoundedness says that 
$$ \left(Y^0, Y^1\right)  \perp  T $$, which again means that the distribution of potential outcomes $$ \left(Y^0, Y^1\right)$$ is independent of the treatment $$T$$.
From the plot, it is pretty clear that the simulated data does <u>not</u> satisfy unconfoundedness. The 2-D distribition of treated invididuals who get an MBA in real life (red points) is different from the distribution of untreated individuals who do not get an MBA in real life (blue points).
Red points are pushed up and to the right, compared to the blue ones.
This means the potential salaries of people who choose to get an MBA are higher, regardless of whether they end up in business school.
This might happen, for example, if people who get MBAs tend to seek out work in higher-earning <a href="https://pubsonline.informs.org/doi/10.1287/isre.1080.0184">sectors</a> in the first place.


In this case, differences between potential salaries arise from how I <a href="https://colab.research.google.com/drive/1lqqjvU-RlJvQP3iGBqm0xhMtLs9UYxAq?usp=sharing">simulated data</a>, where I included a random bit to indicate if a person works in the non-profit sector. In my simulation, if a person works in the non-profit sector, they will tend to both <a href="https://pubsonline.informs.org/doi/10.1287/isre.1080.0184">earn a lower salary overall and have a lower propensity to earn an MBA</a>.
In other words, sector of employment is a confound for future earnings from an MBA.

Thus, in our simulation, if we condition on sector of employment $$X$$ the data satisfy unconfoundedness; the distribution of potential outcomes is independent of the treatment. For example, here is the same plot if we condition on people who work in the non-profit sector. Once we condition on sector, the distribution of potential salaries among those who get MBAs or don't get MBAs is the same.

<div style="display: flex; justify-content: center; align-items: center;">
<img src="https://i.ibb.co/VWqdTpTY/Screen-Shot-2025-03-25-at-10-10-49-PM.png" width="300">
</div>

In reality of course we do not really get to see the joint distribution of potential outcomes. This is just a way of building intution for unconfoundedness in simulation. In real life, we need to try different conditioning methods like matching or propensity scoring to (at <a href="https://pubsonline.informs.org/doi/10.1287/mksc.2022.1413">least</a> <a href="https://www.jstor.org/stable/1806062?seq=1">ideally</a>) approximate unconfoundedness.

Note: The code to generate this example is located <a href="https://colab.research.google.com/drive/1lqqjvU-RlJvQP3iGBqm0xhMtLs9UYxAq?usp=sharing">here</a>.


_Thanks to Nick Eubank and Adriane Fresh for providing feedback on an early version of this blog post._
