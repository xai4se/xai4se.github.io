#!/usr/bin/env python
# coding: utf-8

# # Always find the best subset of the most relevant software metrics
# 
# ## Feature Selection
# 
# 
# Feature selection is a data preprocessing technique for selecting a
# subset of the best software metrics prior to constructing a defect
# model. There is a plethora of feature selection techniques that can be
# applied {cite}`guyon2003introduction`, e.g., filter-based, wrapper-based, and
# embedded-based families. In this book, we would like to select a manageable set of feature
# selection techniques from filter-based and wrapper-based familites for preparing interactive tutorials.

# In[1]:


## Load Data and preparing datasets

# Import for Load Data
from os import listdir
from os.path import isfile, join
import pandas as pd
# Import for Split Data into Training and Testing Samples
from sklearn.model_selection import train_test_split

train_dataset = pd.read_csv(("../../datasets/lucene-2.9.0.csv"), index_col = 'File')
test_dataset = pd.read_csv(("../../datasets/lucene-3.0.0.csv"), index_col = 'File')

outcome = 'RealBug'
features = ['OWN_COMMIT', 'Added_lines', 'CountClassCoupled', 'AvgLine', 'RatioCommentToCode']

# process outcome to 0 and 1
train_dataset[outcome] = pd.Categorical(train_dataset[outcome])
train_dataset[outcome] = train_dataset[outcome].cat.codes

test_dataset[outcome] = pd.Categorical(test_dataset[outcome])
test_dataset[outcome] = test_dataset[outcome].cat.codes

X_train = train_dataset.loc[:, features]
X_test = test_dataset.loc[:, features]

y_train = train_dataset.loc[:, outcome]
y_test = test_dataset.loc[:, outcome]


# commits - # of commits that modify the file of interest
# Added lines - # of added lines of code
# Count class coupled - # of classes that interact or couple with the class of interest
# LOC - # of lines of code
# RatioCommentToCode - The ratio of lines of comments to lines of code
features = ['nCommit', 'AddedLOC', 'nCoupledClass', 'LOC', 'CommentToCodeRatio']

X_train.columns = features
X_test.columns = features
training_data = pd.concat([X_train, y_train], axis=1)
testing_data = pd.concat([X_test, y_test], axis=1)


# ## Filter-based Family
# 
# Filter-based feature selection techniques search for the best subset of
# metrics according to an evaluation criterion regardless of model
# construction. Since constructing models is not required, the use of
# filter-based feature selection techniques is considered low cost and
# widely used.
# 
# **Chi-Squared-based feature selection** {cite}`mchugh2013chi` assesses the
# importance of metrics with the $\chi^2$ statistic which is a
# non-parametric statistical test of independence.

# In[2]:


# Import for Chi-sqaured-based feature selection technique
from sklearn.feature_selection import SelectKBest, chi2

top_k = 3
chi2_fs = SelectKBest(chi2, k=top_k).fit(X_train, y_train)
dfscores = pd.DataFrame(chi2_fs.scores_)
dfcolumns = pd.DataFrame(features)
#concat two dataframes for better visualization 
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Feature','Score'] 
print('Top-k features ( k =', top_k, ') according to Chi-squared statistics are as follows:')
print(featureScores.nlargest(top_k,'Score')) 


# ## Wrapper-based Family
# 
# 
# Wrapper-based feature selection
# techniques {cite}`john1994irrelevant`{cite}`kohavi1997wrappers` use classification
# techniques to assess each subset of metrics and find the best subset of
# metrics according to an evaluation criterion. Wrapper-based feature
# selection is made up of three steps, which we described below.
# 
# *(Step 1) Generate a subset of metrics.* Since it is impossible to
# evaluate all possible subsets of metrics, wrapper-based feature
# selection often uses search techniques (e.g., best first, greedy hill
# climbing) to generate candidate subsets of metrics for evaluation.
# 
# *(Step 2) Construct a classifier using a subset of metrics with a
# predetermined classification technique.* Wrapper-based feature selection
# constructs a classification model using a candidate subset of metrics
# for a given classification technique (e.g., logistic regression and
# random forest).
# 
# *(Step 3) Evaluate the classifier according to a given evaluation
# criterion.* Once the classifier is constructed, wrapper-based feature
# selection evaluates the classifier using a given evaluation criterion
# (e.g., Akaike Information Criterion).
# 
# For each candidate subset of metrics, wrapper-based feature selection
# repeats Steps 2 and 3 in order to find the best subset of metrics
# according to the evaluation criterion. Finally, it provides the best
# subset of metrics that yields the highest performance according to the
# evaluation criterion.
# 
# **Recursive Feature Elimination** (RFE) {cite}`guyon2003introduction`
# searches for the best subset of metrics by recursively eliminating the
# least important metric. First, RFE constructs a model using all metrics
# and ranks metrics according to their importance score (e.g., Breiman's
# Variable Importance for random forest). In each iteration, RFE excludes
# the least important metric and reconstructs a model. Finally, RFE
# provides the subset of metrics which yields the best performance
# according to an evaluation criterion (e.g., AUC).

# In[3]:


# Feature Extraction with RFE
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from itertools import compress
top_k = 3
rf_model = RandomForestClassifier(random_state=1234, n_jobs = 10)
rfe = RFE(rf_model, n_features_to_select = top_k)
rfe_fit = rfe.fit(X_train, y_train)
rfe_features = list(compress(features, rfe_fit.support_))
print('Top-k (k =', top_k, ') according to the RFE teachnique are as follows:')
print(rfe_features)


# ```{note}
# Parts of this chapter have been published by Jirayus Jiarpakdee, Chakkrit Tantithamthavorn, Christoph Treude:
# The impact of automated feature selection techniques on the interpretation of defect models. Empir. Softw. Eng. 25(5): 3590-3638 (2020)"
# ```
# 
# ### Suggested Readings
# 
# [1] Jirayus Jiarpakdee, Chakkrit Tantithamthavorn, Christoph Treude:
# The impact of automated feature selection techniques on the interpretation of defect models. Empir. Softw. Eng. 25(5): 3590-3638 (2020)
# 
# [2] Jirayus Jiarpakdee, Chakkrit Tantithamthavorn, Christoph Treude:
# AutoSpearman: Automatically Mitigating Correlated Software Metrics for Interpreting Defect Models. ICSME 2018: 92-103
# 

# In[ ]:




