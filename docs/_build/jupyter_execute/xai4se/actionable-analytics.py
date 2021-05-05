#!/usr/bin/env python
# coding: utf-8

# # Please Tell Me What To Do!
# 
# TODO - merge with PyExplainer
# 
# We discuss some initial evidence from a successful case study of using
# Explainable AI for Software Engineering in the context of software
# defect prediction {cite}`rajapaksha2021sqaplanner`.
# 
# **Background.** In today's increasingly digitalized world, software
# defects are widespread and enormously expensive, but they are very hard
# to detect, predict, and prevent. Thus, a failure to eliminate software
# defects in safety-critical systems could result in serious injury to
# people, threats to life, death, and disasters.
# 
# Traditionally, software quality assurance activities -- software testing
# and code review -- are widely adopted to discover software defects in
# software systems. However, ultra-large-scale systems, such as, Google,
# can have more than two billion lines of code. Thus, exhaustively
# reviewing and testing every single line of code is not feasible with
# limited time and resources. Defect prediction---an AI/ML model trained
# on historical data to predict if a file/commit will be defective in the
# future---has been proposed to help developers prioritize their limited
# software quality assurance resources on the most risky files/commits.
# 
# **Gaps.** However, developers often do not understand why a file is
# being predicted as defective. In addition, such predictions and global
# explanations are still often not
# actionable {cite}`jiarpakdee2018impact`---i.e., developers do not know what
# to actually do -- or what to avoid doing -- in order to improve the
# quality of the software system. These limitations often lead to a lack
# of trust in the predictions, hindering the adoption of defect prediction
# models in practice.
# 
# Let's consider a scenario where a defect prediction model indicates that
# *file size* is associated with defect-proneness i.e. code in bigger
# files is likely to be more defective. This insight may help managers
# develop quality improvement plans that, in the next development
# iteration, developers should pay attention to the file size to mitigate
# the risk of having defects. However, such insights do not provide a
# concrete suggestion of what to do and what to avoid (i.e. does
# increasing or decreasing size reduce or increase defects?). Thus, a lack
# of such actionable guidance remains an extremely challenging problem,
# often leading to ineffective software quality improvement plans.
# 
# **Approach.** To generate actionable guidance, we used a rule-based
# model-agnostic technique to generate a rule-based explanation for each
# prediction of defect prediction models {cite}`rajapaksha2021sqaplanner`. We
# first build file-level defect prediction models that are trained using
# traditional software features (e.g., lines of code, code complexity, the
# number of developers who edited a file) with a random forest
# classification technique. For each prediction, we applied a rule-based
# model-agnostic technique to generate two types of actionable guidance
# (i.e., what developers should do to mitigate the risk of having defects
# and what developers should not do to avoid increasing the risk of having
# defects).
# 
# **TODO Figure-Rules**
# 
# **Visualizing the actionable guidance.** For each guidance, we
# translated a rule-based explanation into an actionable guidance. Then,
# we developed a proof-of-concept to visualize the actionable guidance
# using a bullet plot **(see
# Figure)**. The visualization is designed to provide the
# following key information: (1) the list of guidance that practitioners
# should follow and should avoid; (2) the actual feature value of that
# file; and (3) its threshold and range values for practitioners to follow
# to mitigate the risk of having defects. The green shades indicate the
# non-risky range values of features, while the red shades indicate the
# risky range values of features. The vertical bars indicate the actual
# values of features for a given file. The green arrows provide directions
# of how a feature should be changed (i.e., increase or decrease). The
# provided guidance is structured into two parts: (1) what to do to
# *decrease the risk* of being defective; and (2) what to avoid to *not
# increase the risk* of being defective.
# 
# **TODO Figure X** shows an example of such actionable guidance to
# help managers develop their quality improvement plans. In this example,
# to decrease the risk of having defects, developers should consider (1)
# decrease the number of class and method declaration lines to less than
# 29 lines, (2) decrease the number of distinct developers to less than 2
# developers, (3) increase the proportion of code ownership to more than
# 0.85, (4) decrease the number of blank lines to less than 8 lines, (5)
# decrease the number of output variables to less than 2 variables.
# Nevertheless, to not increase the risk of having defects, developers
# should consider avoid decreasing the comment to code ratio and avoid
# increasing the number of minor or junior developers.
# 
# **User Study Evaluation.** We conducted a qualitative survey to
# investigate the practitioners' perceptions of our visualization
# approach. We also used the visualization of Microsoft's Code Defect AI
# as a baseline comparison.
# 
# **Results.** We found that 80% of our respondents agree that our
# visualization is better for providing actionable guidance when compared
# to the visualization of Microsoft's Code Defect AI. In addition, 63%-90%
# of the respondents agree with the seven actionable guidance provided by
# our approach.
# 
# ## Lessons Learned
# 
# Based on these findings, we summarise our key lessons learned:
# 
# 1.  Explainable AI is very important in software engineering, but is
#     still under-researched {cite}`jiarpakdee2021perception`.
# 
# 2.  Explainable AI techniques can be used in software engineering to
#     provide explanations of the predictions and actionable guidance to
#     support software engineering tasks {cite}`rajapaksha2021sqaplanner`.
#     Other initial successful evidence can be found at {cite}`chen2018applications`{cite}`jiarpakdee2020modelagnostic`{cite}`krishna2020prediction`{cite}`peng2020defect`{cite}`wattanakriengkrai2020`.
# 
# However, there are several open research questions that remain largely
# unexplored:
# 
# -   What is the best form of explanations for software engineering tasks
#     that are most understandable to software developers?
# 
# -   Do different stakeholders need different forms of explanations in
#     software engineering?
# 
# -   How can we measure the quality and value of explanations in software
#     engineering?
# 
# -   How do explanations from explainable AI domains impact software
#     engineering practices?
# 
# -   What are the other application areas in software engineering that
#     need explanations?
# 
# -   How can we improve the explanations for other complex AI/ML
#     algorithms (e.g., deep learning, optimization, natural language
#     processing) to address other software engineering tasks?
# 
# We developed an interactive tutorial of Explainable AI tools for SE to
# support future research. This can be found at <http://xai4se.github.io>.
# We hope this article will motivate future work to address these
# important questions, which require the SE community to work together
# with other disciplines and communities (e.g., Explainable AI, Visual
# Analytics, Natural Language Processing, Human-Centric Software
# Engineering).

# In[ ]:




