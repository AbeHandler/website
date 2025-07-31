---
layout: post
title:  "What goes in an MISQ abstract?"
date:   2024-11-14 13:40:53-0400
categories: MISQ
---

This blog post is for people learning to write abstracts for MIS Quarterly papers, such as PhD students, assistant professors, and management faculty writing for a new audience (e.g., finance people trying to publish in IS). There are plenty of resources on how to write an academic abstract. This post focuses on the specific conventions at MISQ.

To better understand this genre, I performed a manual analysis of MISQ abstracts from the [September 2024 issue](https://misq.umn.edu/contents-48-3) of the journal.
From this review, I noticed that many MISQ abstracts tend to follow a somewhat standard structure, which can be broken down sentence-by-sentence.
In this post, I'm going to walk through that pattern.

_Note: I include the raw abstracts at the bottom of the post to show my work, along with some histograms to show how many words or sentences go in an MISQ abstract._

# The high-level structure of an MISQ abstract
Abstracts from the September issue seem to follow a common pattern or [discourse structure](https://aclanthology.org/P19-4003/). The pattern goes:

- Introduce a topic or question, and explain why it is important
- Introduce a theoretical or empirical gap in existing research
- Provide details of the paper, which should be contextualized with a theoretical perspective
- Conclude by mentioning the implications of the work, often for researchers and practitioners

This is fairly common to many kinds of academic writing[^1] but I found it pretty eye-opening to look at this structure sentence-by-sentence in MISQ.

## Sentence one of an MISQ abstract

Sentence one of an MISQ abstract often introduces the topic of the paper. Often the authors also motivate their work by explaining why the topic is worthy of study. Occasionally, the authors just state their research question. Examples include: 

- Every day, patients access and generate online health content through a variety of channels, creating an ever-expanding sea of digital data.
- This paper examines the information security implications of hospitals participating in health information exchanges (HIE).
- We study whether the early adoption of information technologies provides competitive advantages and examine the source of such advantages.

If you scroll to the full set of abstracts below, you will notice that every first sentence matches this pattern.

## Sentence two of an MISQ abstract

##### Often, the authors introduce a problem or gap in existing empirical or theoretical work on the topic

By my count, 9 of the 12 abstracts in this issue state a research gap in sentence two. Here are a few examples:

- Existing research in this area has failed to differentiate between the advantages arising from the timing of adoption (e.g., asset preemption) and those that are related to higher levels of adoption (e.g., organizational learning).
- In particular, the agentic nature of these technologies challenges prominent service theories.
- However, a novel theoretical lens is needed to comprehend funders’ enthusiasm in their support of such campaigns.

##### But sometimes the authors refine or expand upon the problem introduced in sentence one

Here are a few examples for this style of sentence two:

- One of the most widely used disinformation techniques is bot-assisted fake social engagement, which is used to falsely and quickly amplify the salience of information at scale.
- At the same time, proponents of public health have recently called for timely, granular, and actionable data to address a range of public health issues, stressing the need for social listening platforms that can identify and compile this valuable data.

# OK, now sentence three

The structure of sentence three depends on what happens in sentence two. 

#### Often, authors use sentence three to introduce the main substance of their paper

Papers which follow this pattern start off with a 3-sentence structure: (1) state the topic of the work and explain why it is worthy of study in sentence one, (2) introduce some gap in existing research on that topic in sentence two, and (3) explain how the paper fills the gap by sketching what happens in the study in sentence three. Examples of September 2024 papers which follow this structure include "Conceptualization and Measurement of Voice Interaction Usability" and "The Returns of Early Adoption of Information Technologies" (see below).

Here is one example. You can find more examples in the abstracts at the bottom.

- Sentence 1: We study whether the early adoption of information technologies provides competitive advantages and examine the source of such advantages. 
- Sentence 2: Existing research in this area has failed to differentiate between the advantages arising from the timing of adoption (e.g., asset preemption) and those that are related to higher levels of adoption (e.g., organizational learning). 
- Sentence 3: In this paper, we break down these advantages into two components: order of adoption (early vs. late adopters) and level of adoption (high vs. low internal diffusion levels).

That said, not all papers adopt this three-sentence starting pattern.

#### Some papers use the third sentence to describe a research gap

Here are some examples. They are similar to the kinds of things you see in sentence two.

- Yet previous attempts at social listening in healthcare have yielded mixed results, largely because they have failed to incorporate sufficient context to understand the communications they seek to analyze.
- Unsupervised topic modeling has been widely adopted to extract human-interpretable latent topics embedded in texts.


# Sentence four

By sentence four, many papers have begun to introduce the details of their study. Here are some examples:

- Leveraging a proven case of bot-assisted fake social engagement operation in a highly trafficked news portal, this study examines the impact of fake social engagement on the digital public’s news consumption, search activities, and political sentiment.
- Guided by activity theory to design HealthSense, we propose a platform for efficiently sensing and gathering data across the web for real-time analysis to support public health outcomes.
- We test our hypotheses in four studies.

# All the sentences up to the final one

After the first three or four sentences, most abstracts get into details from their work. There is some variation here by paper type. Econ-style papers will mention their identification strategy, and design science papers may mention tests on particular datasets. Papers which do controlled experiments will start to lay out each study. Here are few examples of the kinds of things you will find:

- For that purpose, we used ground-truth labels of the manipulator’s bot accounts, as well as real-time clickstream logs generated by ordinary public users. Results show that bot-assisted fake social engagement operations disproportionately increase the digital public’s attention to not only the topical domain of the manipulator’s interest (i.e., political news) but also to specific attributes of the topic (i.e., political keywords and sentiment) that align with the manipulator’s intention. 

- We compiled a panel dataset of more than 3,000 hospitals over six years. By leveraging different identification strategies, including difference-in-differences design, matching, and instrumental variables, we found that the likelihood of a hospital experiencing a data breach decreased by more than 35.37 % after joining an HIE.

# The final sentence

Authors usually conclude by discussing the implications of their work for researchers and practitioners. Here are a few examples.

- We discuss managerial and policy implications for increasingly cluttered online platforms.
- We discuss the implications for research and practice.
- The results have implications for facilitating more efficient and temporally precise usability research and mass-deployable usability testing.

# Note: Theory

[Theory](https://www.abehandler.com/blog/2023/theory-in-is/) is a requirement for publishing in IS, especially at MISQ. So it is not surprising that many papers use a named theory when introducing their work. (Theory is the T in the very useful [FIRST](https://pubsonline.informs.org/doi/10.1287/isre.2023.editorial.v34.n4) acronym from Sarker et al.) Authors don't tend to mention theory in a particular sentence. But many papers include a reference somewhere in their abstract. Examples include:

- **We use biased competition theory (BCT)** to explain how interfaces with low usability create attentional interference, which can be measured through mouse movement efficiency (MME).
- **Based on agenda-setting theory,** we hypothesize that bot-assisted fake social engagement boosts public attention in the manner intended by the manipulator.
- We first developed voice-interaction usability dimensions based on user reviews by using a coding technique ... with five dimensions and 13 subdimensions based on **cooperative principle theory.**
- Thus, from an interdisciplinary perspective, we draw upon **role theory** and propose ...

# How long should my abstract be?

Most abstracts are around 6 to 12 sentences or 150 to 300 words long. Here are some histograms for these abstracts:


<img src="https://i.ibb.co/fQbDcky/word-counts-histogram.png" alt="Word Counts Histogram" width="350">
<img src="https://i.ibb.co/hXG9804/sentence-counts-histograma.png" alt="Word Counts Histogram" width="350">

[^1]: This pattern is similar to other kinds of academic writing, but there things that are somewhat specific to IS. For instance, in ML-related areas of CS, abstracts often emphasize improvements over baselines; MISQ abstracts do not usually follow this CS-style pattern.

# The Raw Data: Abstracts from September 2024

Here are the abstracts I used to write this post.

[**Disinformation Spillover: Uncovering the Ripple Effect of Bot-Assisted Fake Social Engagement on Public Attention**](https://misq.umn.edu/disinformation-spillover-uncovering-the-ripple-effect-of-bot-assisted-fake-social-engagement-on-public-attention.html)

Disinformation activities that aim to manipulate public opinion pose serious challenges to managing online platforms. One of the most widely used disinformation techniques is bot-assisted fake social engagement, which is used to falsely and quickly amplify the salience of information at scale. Based on agenda-setting theory, we hypothesize that bot-assisted fake social engagement boosts public attention in the manner intended by the manipulator. Leveraging a proven case of bot-assisted fake social engagement operation in a highly trafficked news portal, this study examines the impact of fake social engagement on the digital public’s news consumption, search activities, and political sentiment. For that purpose, we used ground-truth labels of the manipulator’s bot accounts, as well as real-time clickstream logs generated by ordinary public users. Results show that bot-assisted fake social engagement operations disproportionately increase the digital public’s attention to not only the topical domain of the manipulator’s interest (i.e., political news) but also to specific attributes of the topic (i.e., political keywords and sentiment) that align with the manipulator’s intention. We discuss managerial and policy implications for increasingly cluttered online platforms.

[**Does Sharing Make My Data More Insecure? An Empirical Study on Health Information Exchange and Data Breaches**](https://misq.umn.edu/does-sharing-make-my-data-more-insecure-an-empirical-study-on-health-information-exchange-and-data-breaches.html)

This paper examines the information security implications of hospitals participating in health information exchanges (HIE). While data security threats may increase when hospitals join HIEs to share data across organizational boundaries, HIEs institute “secure exchange” and promote security practices among participants. Due to these countervailing effects, it is unclear how joining an HIE affects hospitals’ data breach risk. This study seeks to understand the security implications of HIEs from the lens of governance and coordination. We compiled a panel dataset of more than 3,000 hospitals over six years. By leveraging different identification strategies, including difference-in-differences design, matching, and instrumental variables, we found that the likelihood of a hospital experiencing a data breach decreased by more than 35.37 % after joining an HIE. We further show that the effect was more pronounced among HIE member hospitals with more sophisticated clinical IT systems or after HIE security laws were enacted. We discuss the implications for research and practice.

[**Timely, Granular, and Actionable: Designing a Social Listening Platform for Public Health 3.0**](https://misq.umn.edu/timely-granular-and-actionable-designing-a-social-listening-platform-for-public-health-3-0.html)

Every day, patients access and generate online health content through a variety of channels, creating an ever-expanding sea of digital data. At the same time, proponents of public health have recently called for timely, granular, and actionable data to address a range of public health issues, stressing the need for social listening platforms that can identify and compile this valuable data. Yet previous attempts at social listening in healthcare have yielded mixed results, largely because they have failed to incorporate sufficient context to understand the communications they seek to analyze. Guided by activity theory to design HealthSense, we propose a platform for efficiently sensing and gathering data across the web for real-time analysis to support public health outcomes. HealthSense couples theory-guided content analysis and graph propagation with graph neural networks (GNNs) to assess the relevance and credibility of information, as well as intelligently navigate the complex online channel landscape, leading to significant improvements over existing social listening tools. We demonstrate the value of our artifact in gathering information to support two exemplar public health tasks: (1) performing postmarket drug surveillance for adverse reactions and (2) addressing the opioid crisis by monitoring for potent synthetic opioids released into communities. Our results across data, user, and event experiments show that effective design artifacts can enable better outcomes across both automated and human decision-making contexts, making social listening for public health possible, practical, and valuable. Through our design process, we extend activity theory to address the complexities of modern online communication platforms, where information resides not only in the collection of individual communication activities but also in the complex network of interactions among them.

[**TM-OKC: An Unsupervised Topic Model for Text in Online Knowledge Communities**](https://misq.umn.edu/tm-okc-an-unsupervised-topic-model-for-text-in-online-knowledge-communities.html)

Online knowledge communities (OKCs), such as question-and-answer sites, have become increasingly popular venues for knowledge sharing. Accordingly, it is necessary for researchers and practitioners to develop effective and efficient text analysis tools to understand the massive amount of user-generated content (UGC) on OKCs. Unsupervised topic modeling has been widely adopted to extract human-interpretable latent topics embedded in texts. These identified topics can be further used in subsequent analysis and managerial practices. However, existing generic topic models that assume documents are independent are inappropriate for analyzing OKCs where structural relationships exist between questions and answers. Thus, a new method is needed to fill this research gap. In this study, we propose a new topic model specifically designed for the text in OKCs. We make three primary contributions to the research on topic modeling in this context. First, we build a general and flexible Bayesian framework to explicitly model structural and temporal dependencies among texts. Second, we statistically demonstrate the approximate model inference using mean-field and coordinate ascent algorithms. Third, we showcase the practical value and relative merit of our method via a specific downstream task (i.e., user profiling). The proposed model is illustrated using two real-world datasets from well-known OKCs (i.e., Stack Exchange and Quora), and extensive experiments demonstrate its superiority over several cutting-edge benchmarks.

[**Behaviorally Measuring Usability by Analyzing Users’ Mouse Movement Efficiency**](https://misq.umn.edu/behaviorally-measuring-usability-by-analyzing-users-mouse-movement-efficiency.html)

Usability—the extent to which a system can be operated to achieve specified goals with effectiveness, efficiency, and satisfaction—is a hallmark of many successful systems. Identifying usability concerns with existing measures, however, can be problematic. We use biased competition theory (BCT) to explain how interfaces with low usability create attentional interference, which can be measured through mouse movement efficiency (MME). We test our hypotheses in four studies. Study 1 manipulates attentional interference and examines its influence on MME using eye tracking to validate BCT as an appropriate theoretical lens for our research. Study 2 manipulates usability and shows similar markers of attentional interference in MME on a website with two different populations. Study 3 is a field test that compares the reliability of MME in ranking the usability of different components of a commercial web application to rankings produced by a common perceptual measure of usability: perceived ease of use. Collaborating with a Fortune 100 software vendor, Study 4 further demonstrates the efficacy of MME in ranking the usability of various system components compared to a standard industry measure of usability across three different products. The results consistently show that MME can help identify usability differences among parts of systems. The results have implications for facilitating more efficient and temporally precise usability research and mass-deployable usability testing.

[**Conceptualization and Measurement of Voice Interaction Usability: The Development of Cooperative Principle Theory for Smart Product Use**](https://misq.umn.edu/conceptualization-and-measurement-of-voice-interaction-usability-the-development-of-cooperative-principle-theory-for-smart-product-use.html)

The usability of voice interaction is critical for consumers to have a satisfactory experience when interacting with voice-controlled smart products. However, voice interaction from the user’s perspective is underresearched and there are no existing scales to measure voice-interaction usability. This study uses a mixed methods approach to explore the construct of voice-interaction usability and establish a scale that can be used for measuring it. We first developed voice-interaction usability dimensions based on user reviews by using a coding technique that stems from grounded theory and then set up a classification of voice-interaction usability with five dimensions and 13 subdimensions based on cooperative principle theory. After developing the multilevel dimensions, we collected and examined multiple rounds of survey data to develop and validate a voice-interaction usability scale. This study enhances cooperative principle theory by extending the four-principle framework, developing the subdimensions of the framework in the human-machine voice-interaction context, and operationalizing the dimension concepts by developing the associated scales. The voice-interaction usability scale not only contributes to research on users’ behavior and experience with voice-controlled smart products but also provides insights to improve the design of voice-interaction functions.

[**The Returns of Early Adoption of Information Technologies: Order of Adoption or Level of Adoption Advantages?**](https://misq.umn.edu/the-returns-of-early-adoption-of-information-technologies-order-of-adoption-or-level-of-adoption-advantages.html)

We study whether the early adoption of information technologies provides competitive advantages and examine the source of such advantages. Existing research in this area has failed to differentiate between the advantages arising from the timing of adoption (e.g., asset preemption) and those that are related to higher levels of adoption (e.g., organizational learning). In this paper, we break down these advantages into two components: order of adoption (early vs. late adopters) and level of adoption (high vs. low internal diffusion levels). The empirical analysis examines the adoption and subsequent intrafirm diffusion of the automated teller machine in a sample of Spanish savings banks using a long data panel extending from 1988 to 2004. The results show that the advantages associated with the order of adoption outweigh those associated with the level of adoption and have the potential to be long lasting. Our findings are consistent across various estimation methods, and we assess different performance dimensions (ROA, income, and efficiency). Our modeling and findings have implications for managers and can be applied to the study of the early adoption of modern technologies.

[**Techno-Service-Profit Chain: The Impacts of IoT-Enabled Algorithmic Customer Service Systems from an Interdisciplinary Perspective**](https://misq.umn.edu/techno-service-profit-chain-the-impacts-of-iot-enabled-algorithmic-customer-service-systems-from-an-interdisciplinary-perspective.html)

The infusion of emerging technologies (e.g., IoT-enabled algorithmic customer service systems [IACSs]) often brings disruptive changes to customer service. In particular, the agentic nature of these technologies challenges prominent service theories. Among these challenges, recent scholarly calls have pushed for more research on the infusion of emerging technologies into the service-profit chain (SPC) framework, advocating for the importance of extended knowledge to develop a techno-infused version of the SPC. Thus, from an interdisciplinary perspective, we draw upon role theory and propose a technoservice-profit chain (TSPC). Specifically, we contextualize the SPC in the technoservice context with different approaches, including decomposing context-specific constructs and theorizing IACS implementation as a contextual factor that moderates TSPC relationships. Using a sequential mixed methods design combining quantitative and qualitative approaches, we tested our research model by conducting multiwave surveys and follow-up interviews in a large business-to-business service firm with data from employees, supervisors, and customers before and after IACS implementation. This interdisciplinary study contributes to the information systems, service marketing, and management literatures by enriching the compositions of core SPC constructs, theorizing interactions between human agents and technology agents, and scrutinizing the impacts of technology agents on the linkages between internal employee management and external customer service. Our results further reveal the emerging issues of competing bosses (i.e., supervisors and IACSs), competing employees (i.e., employees and IACSs), and the unintended dehumanization effects of IACSs on supervisors and employees.

[**When Should a Sharing Platform Adopt the Bilateral Review System?**](https://misq.umn.edu/when-should-a-sharing-platform-adopt-the-bilateral-review-system.html)

The increasing popularity of sharing platforms is raising concerns about a lack of information on the demand side: the cost of serving specific buyers is typically unknown to sellers. To mitigate this concern, some platforms, such as Airbnb, have adopted the bilateral review system (BRS), allowing buyers and sellers to rate each other. This differs from the traditional unilateral review system (URS), which allows only buyers to rate sellers. In this study, we examine how these two review systems impact the operation of a peer-to-peer (P2P) sharing platform, where sellers with different qualities are matched with buyers with different serving costs. Our analysis reveals that under URS, even with perfect seller information, high-quality sellers can still be driven out of the market due to unknown information about the buyer and the “coproduction” nature of the serving cost. This differs from the adverse selection problem often observed in the used car market, for example, where sellers of high-quality products withdraw due to generally unknown product quality. Additionally, we highlight the critical role of the expected buyer cost: When this cost is high, BRS can benefit the platform by alleviating the adverse selection problem; however, when this cost is low, BRS becomes detrimental to the platform. Our analysis also shows that BRS helps buyers but can hurt sellers. However, BRS has the potential to generate a favorable outcome for all parties involved, resulting in a win-win-win situation benefiting the platform, buyers, and sellers. Our results not only shed light on review system design but also provide a plausible explanation for the widespread use of BRS by sharing platforms such as Airbnb, Fiverr, and Turo.

[**Connecting Customers and Merchants Offline: Experimental Evidence from the Commercialization of Last-mile Stations at Alibaba**](https://misq.umn.edu/connecting-customers-and-merchants-offline-experimental-evidence-from-the-commercialization-of-last-mile-stations-at-alibaba.html)

Many e-commerce platforms have established extensive networks of stations as their last-mile logistics infrastructure. This study investigates how this last-mile infrastructure may serve as an offline platform to connect customers and merchants in the physical world by leveraging walk-in traffic (organic interaction) and prompting interested customers through online intervention (induced interaction). Using free sample distribution as an example, we designed two large-scale studies in collaboration with Alibaba—an observational study across 1,032 stations and a randomized field experiment among 189,019 customers—to examine the causal effects of organic and induced interactions on customers’ subsequent online purchases from the focal brands, respectively. We found that induced interaction drives significantly more online sales than organic interaction. Under induced interaction, the online intervention effectively increases the number of free samples distributed. Nevertheless, the more significant increase in online sales for induced claimers is not simply due to more free samples distributed but because the induced customers are more interested and more likely to purchase. We identified this phenomenon as a screening mechanism that facilitates an advantageous selection of customers claiming the samples. Customers willing to pay the additional travel cost to claim samples are more likely to purchase the focal brands afterward. Finally, we developed a customized targeting framework using a generalized random forest model to enhance the effectiveness of induced interaction at the last-mile stations. Our study raises a key insight that the “foot-in-the-door” traffic in an omnichannel environment can be fundamentally different depending on whether the offline customers are driven from the online channel.

[**Infectious Confidence: Unraveling the Effects of Confidence Contagion on Overfunding in Equity Crowdfunding**](https://misq.umn.edu/infectious-confidence-unraveling-the-effects-of-confidence-contagion-on-overfunding-in-equity-crowdfunding.html)

Equity crowdfunding campaign overfunding occurs when a campaign generates funds in excess of the funding goal and has hence been touted as the mark of an extraordinarily successful campaign. However, a novel theoretical lens is needed to comprehend funders’ enthusiasm in their support of such campaigns. Building on the extant literature on contagion effect, we constructed a research model that posits confidence contagion invoked by confidence cues embedded in campaign materials as a key driver of overfunding. Our hypotheses were validated in two complementary empirical studies. In Study 1, we manipulated confidence cues in a controlled experiment to verify the activation of confidence contagion at the individual level. Analytical results indicate that individual funders detect self-confidence traits from confidence cues embedded in campaign materials and assimilate the fundraiser’s confidence via a spontaneous social appraisal mechanism. In turn, confidence contagion drives funders to congregate and invest in campaigns. In Study 2, we analyzed a secondary dataset collected from a leading equity crowdfunding platform to discern how confidence contagion drives overfunding at the collective level. By modeling funding activities as a Hawkes process, we derived three key metrics that govern the emergence and magnitude of funding surges. We demonstrated that these metrics of funding surges mediate the impact of confidence cues on the level of overfunding for equity crowdfunding campaigns. The findings from this study could inform future research seeking to untangle the interdependencies between individual and collective mechanisms underlying crowd phenomena, provide strategic guidance to fundraisers interested in promoting the overfunding of their campaigns, and help crowdfunding platforms predict the potential extent of overfunding and advise fundraisers accordingly.


_Thanks to Kai Larsen for reviewing an early version of this post_