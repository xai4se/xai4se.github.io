#!/usr/bin/env python
# coding: utf-8

# # Using a Non-Parametric Scott-Knott ESD Test For Multiple Comparison

# The Non-Parametric ScottKnott ESD (NPSK) test is a multiple comparison approach that leverages a hierarchical clustering to partition the set of median values of techniques (e.g., medians of variable importance scores, medians of model performance) into statistically distinct groups with non-negligible difference. The Non-Parametric ScottKnott ESD (NPSK) does not require the assumptions of normal distributions, homogeneous distributions, and the minimum sample size. The mechanism of the Non-Parametric Scott-Knott ESD test is made up of 2 steps:
# 
# * **(Step 1) Find a partition that maximizes treatment medians between groups.** We begin by sorting the median value of the distributions. Then, we compute the Kruskal Chisq statistics to identify a partition that maximizes the median values between groups. The Kruskal Chisq test is a non-parametric test, which does not require data normality and data heterogeneity assumptions.
# 
# * **(Step 2) Splitting into two groups or merging into one group.** We analyze the magnitude of the difference for each pair for all of the treatment medians of the two groups. If there is any one pair of treatment medians of two groups are non-negligible, we split into two groups. Otherwise, we merge into one group. We use the Cliff $|\delta|$ effect size to estimate the effect size of the difference between the two medians.

# ```{note}
# Parts of this chapter have been published by Chakkrit Tantithamthavorn, Shane McIntosh, Ahmed E. Hassan, Kenichi Matsumoto:
# An Empirical Comparison of Model Validation Techniques for Defect Prediction Models. IEEE Trans. Software Eng. 43(1): 1-18 (2017).
# ```
# 
# ### Suggested Readings
# 
# [1] Chakkrit Tantithamthavorn, Shane McIntosh, Ahmed E. Hassan, Kenichi Matsumoto:
# An Empirical Comparison of Model Validation Techniques for Defect Prediction Models. IEEE Trans. Software Eng. 43(1): 1-18 (2017)
# 
# 
# [2] Chakkrit Tantithamthavorn, Shane McIntosh, Ahmed E. Hassan, Kenichi Matsumoto:
# The Impact of Automated Parameter Optimization on Defect Prediction Models. IEEE Trans. Software Eng. 45(7): 683-711 (2019)
# 

# In[ ]:




