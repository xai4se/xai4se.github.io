#!/usr/bin/env python
# coding: utf-8

# # Help managers develop software quality improvement plans
# 
# ## Motivation
# Traditionally, software defect predictions can only generate predictions and provide an understanding at the global level through the use of ANOVA analysis or Random Forest's feature importance{cite}`jiarpakdee2018impact`. 
# However, such predictions and global insights are still not actionable---i.e., developers do not know what actions they should follow or should not follow to improve the quality of software systems.
# 
# Let's consider a scenario where a defect prediction model indicates that large file size is associated with defect-proneness.
# While this insight can help managers develop quality improvement plans that in the next development iteration, developers should maintain the lower file size to mitigate the risk of having defects.
# However, such insights do not provide a concrete suggestion of the optimal threshold of file size---i.e., what is the optimal file size that a file should be.
# Thus, a lack of such actionable guidance and a lack of optimal  thresholds often leads to ineffective software quality improvement plans.
# 
# ## Approach
# To generate actionable guidance, we propose to use a rule-based model-agnostic technique to generate a rule-based explanation for each  prediction of defect prediction models.
# In particular, we first build file-level defect prediction models that are trained using traditional software features (e.g., lines of code, code complexity, the number of developers who edited a file) with a random forest classification technique.
# For each prediction, we apply a rule-based model-agnostic technique called LoRMikA{cite}`rajapaksha2020lormika` to generate two types of actionable guidance (i.e., what developers should do to mitigate the risk of having defects and what developers should not do to avoid increasing the risk of having defects).
# 
# 
# ## Results
# 
# ```{figure} /xai4se/use-case/images/specific-sq-plan.png
# ---
# name: figure-specific-sq-plan
# ---
# An example of actionable guidance to help managers developing quality improvement plans.
# ``` 
# 
# {numref}`figure-specific-sq-plan` presents an example of actionable guidance to help managers developing quality improvement plans.
# To decrease the risk of having defects, developers should consider (1) decrease the number of class and method declaration lines to less than 29 lines, (2) decrease the number of distinct developers to less than 2 developers, (3) increase the proportion of code ownership to more than 0.85, (4) decrease the number of blank lines to less than 8 lines, (5) decrease the number of output variables to less than 2 variables.
# 
# Nevertheless, to not increase the risk of having defects, developers should consider avoid decreasing the comment to code ratio and avoid increasing the number of minor or junior developers.
# 

# In[ ]:




