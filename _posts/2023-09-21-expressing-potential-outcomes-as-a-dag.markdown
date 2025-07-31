---
layout: post
title:  "Expressing potential outcomes as a DAG"
date:   2023-09-21 00:40:53 -0400
categories: math 
---

Textbooks which cover causal inference such as [Wasserman](https://www.stat.cmu.edu/~larry/all-of-statistics/), [Cunningham](https://mixtape.scunning.com/) and [Morgan and Winship](https://www.cambridge.org/core/books/counterfactuals-and-causal-inference/5CC81E6DF63C5E5A8B88F79D45E1D1B7) present two formalisms for analyzing causal relationships from observational data: [potential outcomes](https://en.wikipedia.org/wiki/Rubin_causal_model) notation and [directed acyclic graphs](https://en.wikipedia.org/wiki/Directed_acyclic_graph).
These books state that the formalisms can be shown to be equivalent.  But the connection between potential outcomes and DAGs is pretty counterintuitive,  as DAGs and potential outcomes appear quite different.  

So I was excited when I found an exercise from Wasserman which gives a nice example of a how to express a binary treatment and binary outcome using both formalisms. This blog post reviews the example, which I found very eye-opening. I assume you already know a little bit about DAGs and potential outcomes, and want to gain intuition for why they are equivalent. See the end of Chapter 17 in Wasserman for the original exercise.

### Potential outcomes

Potential outcomes notation introduces a variable $$C_0$$ to show the outcome $$Y$$ when a subject is treated and a variable $$C_1$$ to show the outcome when a subject is not treated. In a real observational experiment, you only get to see one outcome $$Y$$ for a given subject (e.g. the value of $$C_1$$ if the subject is treated). But potential outcomes gives a way to express what _would_ have happened if a treated subject had not been treated (and vice versa). 

In this problem, we will assume a binary treatment and binary outcome. So $$X \in \{0, 1\}$$ and $$Y \in \{0, 1\}$$. $$X=1$$ indicates treatment and $$Y=1$$ indicates a positive outcome. For example, $$X$$ might represent a medical procedure and $$Y$$ may represent patient survival. 

Using potential outcomes, we have the following expression for $$Y$$:

$$
Y = 
\begin{cases}
C_0, & \text{if } X=0 \\
C_1, & \text{if } X=1.
\end{cases}.
$$

For example, $$Y$$ gets $$C_1$$ if $$X=1$$. 

Wasserman then defines the following four groups, based on how members of different groups respond to treatment. For instance, survivors will be OK regardless of if they are treated and antiresponders will get _worse_ when treated. 
<table style="border-collapse: separate; border-spacing: 1em 0.1em; margin: auto;">
    <tr>
        <th style="padding: 0.1em ;"> </th>
        <th style="padding: 0.1em ;">$$C_0$$</th>
        <th style="padding: 0.1em ;">$$C_1$$</th>
        <th style="padding: 0.1em ;">$$Z$$</th>
        <th style="padding: 0.1em ;">$$p(z)$$</th>
    </tr>
    <tr>
        <td style="padding: 0.1em ;">Survivors</td>
        <td style="padding: 0.1em ;">1</td>
        <td style="padding: 0.1em ;">1</td>
        <td style="padding: 0.1em ;">1</td>
        <td style="padding: 0.1em ;">$$a$$</td>
    </tr>
    <tr>
        <td style="padding: 0.1em ;">Responders</td>
        <td style="padding: 0.1em ;">0</td>
        <td style="padding: 0.1em ;">1</td>
        <td style="padding: 0.1em ;">2</td>
        <td style="padding: 0.1em ;">$$b$$</td>
    </tr>
    <tr>
        <td style="padding: 0.1em ;">Antiresponders</td>
        <td style="padding: 0.1em ;">1</td>
        <td style="padding: 0.1em ;">0</td>
        <td style="padding: 0.1em ;">3</td>
        <td style="padding: 0.1em ;">$$c$$</td>
    </tr>
    <tr>
        <td style="padding: 0.1em ;">Doomed</td>
        <td style="padding: 0.1em ;">0</td>
        <td style="padding: 0.1em ;">0</td>
        <td style="padding: 0.1em ;">4</td>
        <td style="padding: 0.1em ;">$$d$$</td>
    </tr>
</table>



I added the last 2 columns to this table, which will help when we get to DAGs.  The last column $$p(z)$$ is just the probability that a member of the population is in each of the groups, the second to last column shows a number $$Z$$ which assigns each region of the same space (e.g., survivors or responders) to a number from 1 to 4.

Wasserman defines the average treatment effect ATE as 

$$ATE = E[C_1] - E[C_0]$$

which is the expected value of the outcome when a person is treated minus the expected value of the outcome when they are not treated.

If we use the $$p(z)$$ notation introduced above, then $$E[C_1]$$ and $$E[C_0]$$ have nice interpretations which will help when we get to DAGs. Remember that formally a r.v. is a mapping from a region of a sample space to real number (e.g., $$C_1(1)=1$$, where 1 represents the survivor region. Thus we have:

$$
\begin{align}
E[C_1] &\stackrel{1}{=}  \Sigma_{z \in Z}  C_1(z) p(z) \\
E[C_1] &\stackrel{2}{=}   \Sigma_{z \in {\{1, 2\}}}  C_1(z) p(z) \\
E[C_1] &\stackrel{}{=}  \Sigma_{z \in {\{1, 2\}}} 1 * p(z) \\
E[C_1]  &\stackrel{}{=}  a + b 
\end{align}
$$

where equality 1 follows from the definition of expected value (defined over the population) and 2 reflects the fact $$C_1=0$$  for anti responders and doomed (so we can just drop them from the summation). The final steps follow from substituting in the values of $$C_1$$ and $$p(z)$$.

By the same logic, $$E[C_0]  =  c + d$$ and so  $$ATE= (a+b) - (c+d)$$. In other words, for a binary outcome and binary treatment, the ATE is the fraction of responders and survivors in the population, minus the the fraction of anti-responders and doomed.

### DAGs

Wasserman suggests constructing the following DAG to reflect the same observational experiment. In this DAG, $$X$$ is a binary treatment variable and $$Y$$ is a binary outcome variable and $$Z$$ is a confounder that is set to a number from 1 to 4, corresponding to the 4 regions in the table above. 

<div style="display: flex; justify-content: center; align-items: center; height: auto">
    <img src="https://i.ibb.co/hCGjYJy/dag.png" alt="Directed Acyclic Graph (DAG)" width="200"/>
</div>

Formally, a DAG represents a way to factor the joint distribution of random variables. The joint distribution of variables in a DAG factors as the product of each variable in the DAG conditioned on its parents (see Wasserman Chapter 17). In this case, let $$p(x,y,z)$$ be the joint distribution between $$X,Y$$ and $$Z$$. This DAG represents a joint distrubution $$p(x,y,z) = p(z)p(x\vert z)p(y \vert x, z)$$.

In this example, the value of $$Z$$ corresponds to one of the 4 groups in the population (e.g., survivors or doomed). This means that $$Z$$ serves to set the probability of a given configuration of the 3 variables to 1 in certain cases, and to 0 otherwise. For example, when $$Z$$ is 4, then the probability that $$X$$ and $$Y$$ are zero is 1 because $$Z$$ corresponds to the doomed region of the probability space (where $$X=Y=0$$). We write this $$p(X=0,Y=0,Z=4)=1$$ (and zero for all other values of $$X$$ and $$Y$$).

Recall that Pearl defines an operator $$do(X=x)$$ which intervenes to fix the value of a r.v. $$X$$. By definition, this intervention modifies a DAG by removing all incoming parents of $$X$$.
I find this modification very intuitive, because after the intevention the value of $$X$$ is now fixed (and no longer depends on its parents). 
Because a DAG represents the factorization of the joint distribution, this means that we can now delete all terms $$p(X \vert \pi (X)$$ from the joint, because now $$X=x$$ with probability one. 

Thus, if we intervene to set $$X=x$$ the DAG factors $$p(x,y,z)$$ as $$p(z)p(y \vert do(X=x), z)$$ because by definition when we intervene we (1) remove all incoming arrows to $$x$$ and (2) remove all corresponding terms from the factorization. Thus $$p(do(X=x), y, z)$$ is equal to $$p(z)p(y \vert do(X=x), z)$$, which is equal to the joint distribution $$p(z)p(x \vert z)p(y \vert x, z)$$ after intervening fix $$X=x$$ and removing $$p(x \vert z)$$. 

Thus when we take the expectation we get:

$$
\begin{align}
E[Y \vert do(X=x)] &\stackrel{1}{=} \Sigma_Y Y f(do(X=x),y,z) \\
E[Y \vert do(X=x)] &\stackrel{2}{=} \Sigma_Y Y * \Sigma_z p(z)p(y \vert do(X=x), z) \\
E[Y \vert do(X=x)] &\stackrel{3}{=} \Sigma_z p(Y=1 \vert do(X=x), z)p(z)
\end{align}
$$

where equality 1 is the definition of the expected value of  discrete r.v.,  equality 2 is the definition of the joint distribution corresponding to a DAG after intervening to set $$X=x$$ and equality 3 reflects the fact that $$Y * \Sigma_z p(z)p(y \vert do(X=x), y)=0$$ when the binary r.v. $$Y=0$$ (so we can drop it from the outer sum).

Say we intervene and set $$X=1$$. The term $$p(Y = 1 \vert do(X=1), Z=z)$$ will be equal to 1 if and only if $$z \in \{0, 1\}$$. Similarly,  $$p(Y = 1 \vert do(X=1), Z=z) = 0$$ if and only if $$z \in \{3, 4\}$$. 

Thus if we intervene to set $$X=1$$. we have $$E[Y \vert do(X=1)] = \Sigma_z p(Y=1 \vert x, z)p(z)$$. Additionally, because the probability $$p(Y=1 \vert x, z)$$ is 0 when $$z \in \{3, 4\}$$, we have  $$E[Y \vert do(X=1)] = \Sigma_{z\in \{1, 2\}} 1 * p(z) = a + b$$. By the same logic, $$E[Y \vert do(X=0)] = c +d$$.

Hence the ATE from our potential outcomes notation is equivalent to the expectation of $$Y$$ after intervening to fix $$X$$ to 1 minus the expectation of $$Y$$ after intervening to fix $$X$$ to 0. 

In symbols: 

$$\begin{align*} ATE &= E[Y \vert do(X=1)] - E[Y \vert do(X=0)] \\ &= a+b - (c +d) \\ &= E[C_1] - E[C_0] \end{align*}$$

This shows how to construct a DAG that represents a binary treatment and outcome. It also shows that we get the same ATE when we express the intervention using potential outcomes or using a DAG. For this example at least, the DAG and potential outcomes are equivalent.

To make this more concrete, we can imagine that $$Z$$ reflects factors that govern how a person responds to a treatment. For example, if $$X$$ is a medical intervention in an observational study then $$Z$$ might be the factors which cause them to seek out the treatment, and which also cause the outcome. For example, to use Wasserman's example, suppose healthy people take vitamin C. $$Z$$ in the DAG might govern if a person is healthy (i.e., $$Y$$) and takes vitamin C (i.e., $$X$$). The effect of the intervention will be the same if expressed using potential outcomes or a DAG.

_Thanks to Javier Burroni for pointing out some errors and suggesting better notation for the do intervention._
