#!/usr/bin/env python
# coding: utf-8

# # Explainability in Software Engineering
# 
# Software engineering is by nature a collaborative social practice.
# Collaboration among different stakeholders (e.g., users, developers, and
# managers) is essential in modern software engineering. As a part of the
# collaboration, individuals are often expected to explain decisions made
# throughout software development processes to develop appropriate trust
# and enable effective communication. Since tool support in software
# development processes is an integral part of this collaborative process,
# similar expectations are also applied. Such tools should not only
# provide insights or generate predictions for recommendation, but also be
# able to explain such insights and recommendations.
# 
# Recent automated and advanced software development tools heavily rely on
# Artificial Intelligence and Machine Learning (AI/ML) capabilities to
# predict software defects, estimate development effort, and recommend API
# choices. However, such AI/ML algorithms are often "black-box", which
# makes it hard for practitioners to understand how the models arrive at a
# decision. A lack of explainability of the black-box algorithms leads to
# a lack of trust in the predictions or recommendations produced by such
# algorithms.
# 
# 
# ## Explainable AI for SE: A Way Forward
# 
# Explainable AI is a suite of AI/ML techniques that produce accurate
# predictions, while being able to explain such predictions. The purpose
# of increasing the explainability of software analytics (XAI4SE) is to
# make its behavior more intelligible to humans by providing explanations.
# The explainability of software analytics can be achieved by:
# 
# -   **"Global Explanability\":** Using interpretable machine learning
#     techniques (e.g., decision tree, decision rules or logistic
#     regression techniques) or intrinsic model-specific techniques (e.g.,
#     ANOVA, variable importance) so the entire predictions and
#     recommendations process are transparent and comprehensible. Such
#     intrinsic model-specific techniques aim to provide the global
#     explainability. Thus, users can only understand how the model works
#     globally (e.g., by inspecting a branch of decision trees). However,
#     users often do not understand why the model makes that prediction.
# 
# -   **"Local Explanability\":** Using model-agnostic techniques (e.g.,
#     LIME {cite}`ribeiro2016should`) to explain the predictions of the
#     software analytics models (e.g., neural network, random forest).
#     Such post-hoc model-agnostic techniques can provide an explanation
#     for each prediction (i.e., an instance to be explained). Users can
#     then understand why the prediction is made by the software analytics
#     models.
#     
#     
# ## A Theory of Explainability
# 
# According to philosophy, social science, and psychology theories, a
# common definition of *explainability or interpretability* is *the degree
# to which a human can understand the reasons behind a decision or an
# action* {cite}`Miller19`. The explainability of AI/ML algorithms can be
# achieved by (1) making the entire decision-making process transparent
# and comprehensible and (2) explicitly providing an explanation for each
# decision {cite}`lipton2018mythos` (since an explanation is not likely applicable to
# all decisions {cite}`leake2014evaluating`. Hence, research has emerged to
# explore how to explain decisions made by complex, black-box models and
# how explanations are presented in a form that would be easily understood
# (and hence, accepted) by humans.
# 
# ## A Theory of Explanations
# 
# 
# According to a philosophical and psychological theory of explanations,
# Salmon  {cite}`Salmon84` argue that explanations can be presented as a causal
# chain of causes that lead to the decision. Causal chains can be
# classified into five categories {cite}`Hilton2005`: temporal, coincidental,
# unfolding, opportunity chains and pre-emptive. Each type of causal chain
# is thus associated with an explanation type. However, identifying the
# complete causal chain of causes is challenging, since most AI/ML
# techniques produce only correlations instead of causations.
# 
# In contrast, Miller {cite}`Miller19` argue that explanations can be presented
# as answers to why-questions. Similarly, Lipton {cite}`lipton1990contrastive` also share
# a similar view of explanations as being *contrastive*. There are three
# components of why-questions {cite}`van1980scientific`: (1) the event to be explained,
# also called the *explanandum* (e.g., file A is defective); (2) a set of
# similar events that are similar to the explanandum but did not occur
# (e.g., file A is clean); and (3) a request for information that can
# distinguish the occurrence of the explanandum from the non-occurrence of
# the other similar events (e.g., a large number of changes made to file
# A). Below, we describe four types of why-questions:
# 
# -   **Plain-fact** is the properties of the object. *Why does object $a$ have property $P$?*
#     \
#     Example: Why is file $A$ defective?
# -   **Property-contrast** is the differences in the Properties within an object. *Why does object $a$ have property $P$, rather than property $P'$?*
#     \
#     Example:
# ```{figure} /xai4se/images/p-contrast.png
# ---
# name: p-contrast
# ---
# An illustrative example of P-contrast explanation.
# ``` 
# -   **Object-contrast** is the differences between two Objects. *Why does object $a$ have property $P$, while object $b$ has property $P'$?*
#     \
#     Example:
#     
# ```{figure} /xai4se/images/o-contrast.png
# ---
# name: o-contrast
# ---
# An illustrative example of O-contrast explanation.
# ``` 
#  
# -   **Time-contrast** is the differences within an object over Time. *Why does object $a$ have property $P$ at time $t$, but property $P'$ at
#     time $t'$?*
#     \
#     Example:
#     
# ```{figure} /xai4se/images/t-contrast.png
# ---
# name: t-contrast
# ---
# An illustrative example of T-contrast explanation.
# ``` 
#  
# Answers to the P-contrast, O-contrast and T-contrast why-questions form
# an explanation. *Contrastive explanations focus on only the differences
# on **Properties within an object** (Property-contrast), between **two
# Objects** (Object-contrast), and **within an object over Time**
# (Time-contrast)* {cite}`VanBouwel2002`. Answering a plain fact question is
# generally more difficult than generating answers to the contrastive
# questions {cite}`lipton1990contrastive`. For example, we could answer the
# Property-contrast question (e.g., "Why is file $A$ classified as being
# defective instead of being clean?") by citing that there are a
# substantial number of defect-fixing commits that involve with the file.
# Information about the size, complexity, owner of the file, and so on are
# not required to answer this question. On the other hand, explaining why
# file $A$ is defective in a non-contrastive manner would require us to
# use all causes. In addition, humans tend to be cognitively attached to
# digest contrastive explanations {cite}`Miller19`. Thus, contrastive
# explanations may be more valuable and more intuitive to humans. These
# important factors from both social and computational perspectives should
# be considered when providing explainable models or tool support for
# software engineering.
# 
# Explanation is not only a *product*, as discussed above, but also a
# *process* {cite}`Lombrozo2006`. In fact, generating explanations is a
# *cognitive process* which essentially involves four cognitive systems:
# (1) attention, (2) long-term memory, (3) working memory, and (4)
# metacognition {cite}`Horne2019`{cite}`leake2014evaluating`. Recent
# work {cite}`Miller19` further recognised the importance of considering
# explanation as being not only a cognitive process but also a *social
# process*, in which an explainer communicates knowledge to an explainee.
# Using this view, explanations should be considered as part of a
# conversation between the explainer and explainee. The theories, models,
# and processes of how humans explain decisions to one another are
# important to the work on explainable software analytics and the
# development of explainable tool support for software engineering in
# general.

# ```{note}
# Parts of this chapter have been published by Jirayus Jiarpakdee, Chakkrit Tantithamthavorn, Hoa Khanh Dam, John Grundy: An Empirical Study of Model-Agnostic Techniques for Defect Prediction Models. IEEE Trans. Software Eng. (2020) https://doi.org/10.1109/TSE.2020.2982385"
# ```

# In[ ]:




