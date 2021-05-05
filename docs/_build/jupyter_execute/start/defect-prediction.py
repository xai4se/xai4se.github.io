#!/usr/bin/env python
# coding: utf-8

# # Defect Prediction
# Defect prediction models have been proposed to predict the most risky areas of source code that are likely to have post-release defects {cite}`menzies2007data` {cite}`nagappan2010change` {cite}`d2010extensive` {cite}`tantithamthavorn2018optimization` {cite}`tantithamthavorn2016automated` {cite}`wang2016automatically` {cite}`wang2018deep`.
# A defect prediction model is a classification model that estimates the likelihood that a file will have post-release defects.
# One of the main purposes is to help practitioners effectively spend their limited SQA resources on the most risky areas of code in a cost-effective manner.
# s
# ## The modelling pipeline of defect prediction models
# 
# The predictive accuracy of the defect prediction model heavily relies on the modelling pipelines of defect prediction models
# {cite}`tantithamthavorn2015icse`{cite}`tantithamthavorn2016comments`{cite}`tantithamthavorn2018pitfalls`{cite}`menzies2019`{cite}`ghotra2015revisiting`{cite}`agrawal2018better`{cite}`tantithamthavorn2016icseds`.
# To accurately predicting defective areas of code, prior studies conducted a comprehensive evaluation to identify the best technique of the modelling pipelines for defect models.
# For example, feature selection techniques {cite}`ghotra2017large`{cite}`jiarpakdee2018autospearman`{cite}`jiarpakdee2020featureselection`,
# collinearity analysis
# {cite}`jiarpakdee2018autospearman`{cite}`jiarpakdee2016study`{cite}`jiarpakdee2018impact`,
# class rebalancing techniques {cite}`tantithamthavorn2018impact`,
# classification techniques {cite}`ghotra2015revisiting`,
# parameter optimization {cite}`tantithamthavorn2016automated`{cite}`fu2016tuning`{cite}`tantithamthavorn2018optimization`{cite}`agrawal2018better`,
# model validation {cite}`tantithamthavorn2017empirical`, and model interpretation {cite}`jiarpakdee2018impact`{cite}`jiarpakdee2020empirical`.
# Despite the recent advances in the modelling pipelines for defect prediction models, the cost-effectiveness of the SQA resource prioritization still relies on the granularity of the predictions.
# 
# ## The granularity levels of defect predictions models
# 
# The cost-effectiveness of the SQA resource prioritization heavily relies on the granularity levels of defect prediction.
# Prior studies argued that prioritizing software modules at the finer granularity is more cost-effective {cite}`pascarella2019fine` {cite}`kamei2010revisiting` {cite}`hata2012bug`.
# For example, Kamei et al. {cite}`kamei2010revisiting` found that the file-level defect prediction is more effective than the package-level defect prediction.
# Hata et al. {cite}`hata2012bug` found that the method-level defect prediction is more effective than file-level defect prediction.
# Defect models at various granularity levels have been proposed, e.g., packages {cite}`kamei2010revisiting`, components {cite}`thongtanunam2016revisiting`, modules {cite}`kamei2007effects`, files {cite}`kamei2010revisiting` {cite}`mende2010effort`, methods {cite}`hata2012bug`.
# However, developers could still waste an SQA effort on manually identifying the most risky lines, since the current prediction granularity is still perceived as coarse-grained {cite}`wan2018perceptions`. 
# Hence, the line-level defect prediction should be beneficial to SQA teams to spend optimal effort on identifying and analyzing defects.
# 
# 
# ```{figure} /start/images/predictive-modelling.png
# ---
# name: predictive-modelling
# ---
# TITLE?
# ```
# 
# 
# 
# 

# 

# In[ ]:





# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# mining-software-defects.ipynb
# software-metrics.ipynb
# ```
# 
