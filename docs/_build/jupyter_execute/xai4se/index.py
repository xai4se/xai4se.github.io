#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# ## Stop Telling Me What It Is!
# 
# While the adoption of software analytics enables software organisations
# to distill actionable insights and support decision-making, there are
# still many barriers to the successful adoption of such software
# analytics in software organizations {cite}`dam2018explainable`.
# 
# First, most software practitioners do not understand the reason behind
# the predictions from software analytics systems {cite}`dam2018explainable`.
# They often ask the following questions:
# 
# -   Why is this person best suited for this task?
# 
# -   Why is this file predicted as defective?
# 
# -   Why is this task required the highest development effort?
# 
# -   Why should this task be done first?
# 
# -   Why is this developer predicted to have low productivity?
# 
# -   How can we improve the quality of software systems in following
#     iterations?
# 
# These concerns about a lack of explanation often leads to a lack of
# trust and transparency, hindering the adoption of software analytics in
# practice.
# 
# Second, software practitioners are often affected by the decision-making
# from software analytics. Our recent work also found that practitioners
# are very concerned about their privacy and fairness if defect prediction
# models were deployed in practice. Practitioners even asked \"Would
# developers be laid-off due to the use of defect prediction models for
# identifying who are most likely to introduce software
# defects?\" {cite}`jiarpakdee2021perception`. Article 22 of the European
# Union's General Data Protection Regulation (GDPR) states that the use of
# data in decision-making that affects an individual or group requires an
# **explanation** for any decision made by an algorithm. Unfortunately,
# current software analytics still often do not uphold privacy
# laws {cite}`jiarpakdee2020modelagnostic`. Thus, the risks of unjustified
# decision-making of software analytics systems can be catastrophic,
# leading to potentially erroneous and costly business
# decisions {cite}`dam2018explainable`.
# 
# 
# ```{figure} /xai4se/images/xai-concept.png
# ---
# name: xai-concept
# ---
# Most software analytics (i.e., defect prediction) studies  have three main goals: (1) predictions; (2) model explanation; and (3) instance explanation. We found that 82% of our study respondents perceived the explanability goal (generating model explanations and instance explanations) is equally useful as the prediction goal. However, we found that 91% (81/96) of defect prediction studies only focus on the prediction goal, and as few as 4% of defect prediction studies focus on the explainability goal.
# ```
# 
# 
# ## Is the Community Moving to the Right Direction?
# 
# ### Researchers' Focuses
# 
# We conducted a literature analysis to better understand what researchers
# are currently focusing on for defect explanation. We collected 96
# primary defect prediction studies that were published in top-tier
# Software Engineering venues (i.e., TSE, ICSE, EMSE, FSE, and MSR) during
# 2015-2020 (as of 11 January 2021). We then characterized the key goals
# of each defect prediction study into three main goals: (1) predictions;
# (2) model explanation; and (3) instance
# explanation {cite}`jiarpakdee2021perception` (see {numref}`xai-concept`). We found that 91% (81/96) of the defect
# prediction studies only focus on making predictions, without considering
# explaining the predictions. As few as 4% of the defect prediction
# studies focus on explaining the predictions of defect prediction models. This indicates that the explainability and
# actionability of software analytics is still very under researched.
# 
# ### Practitioners' Needs
# 
# We conducted a qualitative survey to better understand what
# practitioners perceive as the usefulness of each goal of defect
# prediction models. We found that practitioners perceive that the
# explainability and actionability of software analytics are as **equally
# useful** as the predictions {cite}`jiarpakdee2021perception`. 82% of our
# respondents said that the explanability goal (generating model
# explanations and instance explanations) is as useful as the prediction
# goal (see {numref}`xai-concept`). Thus, we argue that **explainable and actionable software
# analytics is urgently and critically needed**. The research and practice
# communities should thus start answering the key question: *\"How can we
# make software analytics more explainable and actionable?\"*.
# 

# In[ ]:




