#!/usr/bin/env python
# coding: utf-8

# # Techniques for Local Explanation
# 
# ## LIME
# 
# **LIME** (i.e., Local Interpretable Model-agnostic
# Explanations) {cite}`ribeiro2016should` is a model-agnostic technique that
# mimics the behaviour of the black-box model to generate the explanations
# of the predictions of the black-box model. Given a black-box model and
# an instance to explain, LIME performs 4 key steps to generate an
# instance explanation as follows:
# 
# -   First, LIME randomly generates instances surrounding the instance of
#     interest.
# 
# -   Second, LIME uses the black-box model to generate predictions of the
#     generated random instances.
# 
# -   Third, LIME constructs a local regression model using the generated
#     random instances and their generated predictions from the black-box
#     model.
# 
# -   Finally, the coefficients of the regression model indicate the
#     contribution of each metric on the prediction of the instance of
#     interest according to the black-box model.
#     
# ### A tutorial of LIME

# In[1]:


## Load Data and preparing datasets

# Import for Load Data
from os import listdir
from os.path import isfile, join
import pandas as pd

# Import for Split Data into Training and Testing Samples
from sklearn.model_selection import train_test_split

# Import for Construct a black-box model (Random Forests)
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.ensemble import RandomForestClassifier

# Import for LIME
import lime
import lime.lime_tabular

train_dataset = pd.read_csv(("../../../datasets/lucene-2.9.0.csv"), index_col = 'File')
test_dataset = pd.read_csv(("../../../datasets/lucene-3.0.0.csv"), index_col = 'File')

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

## Construct a black-box model (Random Forests)

# random forests
rf_model = RandomForestClassifier(random_state=1234, n_jobs = 10)
rf_model.fit(X_train, y_train)  

# construct a lime explainer
lime_explainer = lime.lime_tabular.LimeTabularExplainer(
                            training_data = X_train.values,  
                            mode='classification',
                            training_labels=y_train,
                            feature_names=features,
                            class_names = ['Clean', 'Defective'],
                            discretize_continuous=True,
                            random_state = 1234)


# random an instance that is predicted as defective for generating a visual example
# src/java/org/apache/lucene/index/DocumentsWriter.java
print('src/java/org/apache/lucene/index/DocumentsWriter.java is likely to be defective with the probability of', rf_model.predict_proba(X_test.loc['src/java/org/apache/lucene/index/DocumentsWriter.java':, :].iloc[0:1,:])[0][1])

# generate a LIME local explanation of the instance
lime_local_explanation = lime_explainer.explain_instance(
                            data_row = X_test.loc['src/java/org/apache/lucene/index/DocumentsWriter.java',:], 
                            predict_fn = rf_model.predict_proba, 
                            num_features=5,
                            top_labels=1)

# textual explanation
print(lime_local_explanation.as_list(label= lime_local_explanation.available_labels()[0]))

# visual LIME
lime_local_explanation.show_in_notebook()


# ## SHAP
# 
# **SHAP** (Shapley values) {cite}`ribeiro2016should` is a model-agnostic technique that generate the explanations of the black-box model based on game theory.
# 
# ### A tutorial of SHAP

# In[2]:


## Load Data and preparing datasets

# Import for Load Data
from os import listdir
from os.path import isfile, join
import pandas as pd

# Import for Split Data into Training and Testing Samples
from sklearn.model_selection import train_test_split

# Import for Construct a black-box model (Regression and Random Forests)
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# Import libraries for SHAP
import subprocess
import sys
import importlib
import numpy
import shap

train_dataset = pd.read_csv(("../../../datasets/lucene-2.9.0.csv"), index_col = 'File')
test_dataset = pd.read_csv(("../../../datasets/lucene-3.0.0.csv"), index_col = 'File')

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

## Construct a black-box model (Regression and Random Forests)

# random forests
rf_model = RandomForestClassifier(random_state=1234, n_jobs = 10)
rf_model.fit(X_train, y_train)  

# select an instance to explain
explain_file = 'src/java/org/apache/lucene/index/DocumentsWriter.java'
explain_index = list(X_test.index).index(explain_file)
print(explain_file, 'is likely to be defective with a probability of', rf_model.predict_proba(X_test.loc[X_test.index == explain_file, :])[0][1])

# construct a SHAP explainer
explainer = shap.KernelExplainer(rf_model.predict, X_test)

# generate shap values of testing data
shap_values = explainer.shap_values(X_test.iloc[explain_index, :])

# generate textual explanation of SHAP
for i in range(0, len(features)):
    print(features[i], 'SHAP score =', shap_values[i])

# visualize a SHAP local explanation of the instance
shap.initjs()
shap.force_plot(explainer.expected_value, 
                shap_values, 
                X_test.iloc[explain_index,:])

