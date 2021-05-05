#!/usr/bin/env python
# coding: utf-8

# # Always handle class imbalance
# 
# ## Class Rebalancing Techniques for Software Analytics
# 
# A plethora of class rebalancing techniques exist {cite}`he2009learning`,
# e.g., (1) sampling methods for imbalanced learning, (2) cost-sensitive
# methods for imbalanced learning, (3) kernel-based methods for imbalanced
# learning, and (4) active learning for imbalanced learning. Since it is
# impractical to study all of these techniques, we select a manageable set
# of class rebalancing techniques for our study. As discussed by
# He {cite}`he2009learning`, we start from the four families of imbalance
# learning techniques. Based on a literature surveys by Hall *et al.* {cite}`hall2012systematic`,
# Shihab {cite}`Shihab2012`, and Nam {cite}`nam2014survey`, we then select only the
# family of sampling techniques for the context of defect prediction.
# 
# We first select the three commonly-used techniques (i.e., over-sampling,
# under-sampling, and Default SMOTE {cite}`chawla2002smote`) that were
# previously used in the literature {cite}`Kamei2007`{cite}`Khoshgoftaar2010`{cite}`Pelayo2007`{cite}`Seiffert2014`{cite}`tan2015online`{cite}`wang2013`{cite}`xia2015elblocker`{cite}`yang2016automated`{cite}`yang2017high`
# 
# 
# 
# ```{figure} /software-analytics/images/class-imbalance-overview.png
# ---
# name: class-imbalance-overview
# ---
# An illustrative overview of the 3 selected class rebalancing techniques.
# ```
# 
# Below, we provide a description and a discussion of the 3 selected class rebalancing techniques for our book with interactive python tutorials.
# 

# In[1]:


## Load Data and preparing datasets

# Import for Load Data
from os import listdir
from os.path import isfile, join
import pandas as pd
# Import for Split Data into Training and Testing Samples
from sklearn.model_selection import train_test_split
import numpy as np

# Import for Construct a black-box model (Regression and Random Forests)
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

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

# Compute class ratio
def get_class_ratio(input_data):
    n_data = len(input_data)
    n_defective = sum(input_data)
    n_clean = n_data - n_defective
    print('From the total of', n_data, 'files, there are:')
    print(n_defective, 'defective files', '('+str(np.round(n_defective*1.0/n_data*100, 2))+'%)')
    print(n_clean, 'clean files', '('+str(np.round(n_clean*1.0/n_data*100, 2))+'%)')
    


# In[2]:


# Find a class ratio of the original training dataset
get_class_ratio(y_train)


# ### Over-Sampling Technique (OVER)
# 
# The over-sampling technique (a.k.a. up-sampling) randomly samples with
# replacement (i.e., replicating) *the minority class* (e.g., defective
# class) to be the same size as the majority class (e.g., clean class).
# The advantage of an over-sampling technique is that it leads to no
# information loss. Since oversampling simply adds replicated modules from
# the original dataset, the disadvantage is that the training dataset ends
# up with multiple redundant modules, leading to an overfitting. Thus,
# when applying the over-sampling technique, the performance of with-in
# defect prediction models is likely higher than the performance of
# cross-project defect prediction models.
# 

# In[3]:


# Import for the Over-Sampling technique (OVER)
from imblearn.over_sampling import RandomOverSampler

# Apply the Over-Sampling technique
oversample = RandomOverSampler(sampling_strategy='minority')
X_OVER_train, y_OVER_train = oversample.fit_resample(X_train, y_train)

# Find a class ratio of the over-sampled training dataset
get_class_ratio(y_OVER_train)


# ### Under-Sampling Technique (UNDER)
# 
# The under-sampling technique (a.k.a. down-sampling) randomly samples
# (i.e., reducing) *the majority class* (e.g., clean class) in order to
# reduce the number of majority modules to be the same number as the
# minority class (e.g., defective class). The advantage of an
# under-sampling technique is that it reduces the size of the training
# data when the original data is relatively large. However, the
# disadvantage is that removing modules may cause the training data to
# lose important information pertaining to the majority class.
# 

# In[4]:


# Import for the Under-Sampling technique (UNDER)
from imblearn.under_sampling import RandomUnderSampler

# Apply the Under-Sampling technique
undersample = RandomUnderSampler(sampling_strategy='majority')
X_UNDER_train, y_UNDER_train = undersample.fit_resample(X_train, y_train)

# Find a class ratio of the under-sampled training dataset
get_class_ratio(y_UNDER_train)


# ### Synthetic Minority Oversampling Technique (SMOTE)
# 
# The SMOTE technique {cite}`chawla2002smote` was proposed to combat the
# disavantages of the simple over-sampling and under-sampling techniques.
# The SMOTE technique creates artificial data based on the feature space
# (rather than the data space) similarities from the minority modules. The
# SMOTE technique starts with a set of minority modules (i.e., defective
# modules). For each of the minority defective modules of the training
# datasets, SMOTE performs the following steps:
# 
# 1.  Calculate the $k$-nearest neighbors.
# 
# 2.  Select $N$ majority clean modules based on the smallest magnitude of
#     the euclidean distances that are obtained from the $k$-nearest
#     neighbors.
# 
# Finally, SMOTE combines the synthetic oversampling of the minority
# defective modules with the undersampling the majority clean modules.
# 

# In[5]:


# Import for the Synthetic Minority Oversampling Technique (SMOTE)
from imblearn.over_sampling import SMOTE

# Apply the SMOTE technique
oversample_SMOTE = SMOTE(sampling_strategy='minority')
X_SMOTE_train, y_SMOTE_train = oversample_SMOTE.fit_resample(X_train, y_train)

# Find a class ratio of the SMOTE-ed training dataset
get_class_ratio(y_SMOTE_train)


# ```{note}
# Parts of this chapter have been published by Chakkrit Tantithamthavorn, Ahmed E. Hassan, Kenichi Matsumoto: The Impact of Class Rebalancing Techniques on the Performance and Interpretation of Defect Prediction Models. IEEE Trans. Software Eng. 46(11): 1200-1219 (2020)"
# ```
# 
# 
# ### Suggested Readings
# 
# [1] Chakkrit Tantithamthavorn, Ahmed E. Hassan, Kenichi Matsumoto: The Impact of Class Rebalancing Techniques on the Performance and Interpretation of Defect Prediction Models. IEEE Trans. Software Eng. 46(11): 1200-1219 (2020)"
# 
# [2] Amritanshu Agrawal, Tim Menzies:
# Is "better data" better than "better data miners"?: on the benefits of tuning SMOTE for defect prediction. ICSE 2018: 1050-1061
# 

# In[ ]:




