#!/usr/bin/env python
# coding: utf-8

# # Always evaluate using business-driven measures
# 
# TODO
# <!-- 
# First, we use the *Brier score* [@Brier1950; @Rufibach2010] to measure
# the distance between the predicted probabilities and the outcome. The
# Brier score is calculated as
# $\text{B} = \frac{1}{N}\sum\limits _{i=1}^{N}(f_t-o_t)^2$, where $f_t$
# is the predicted probability, $o_t$ is the outcome for module $t$
# encoded as 0 if module $t$ is clean and 1 if it is defective, and $N$ is
# the total number of modules. The Brier score ranges from 0 (best
# classifier performance) to 1 (worst classifier performance), where a
# Brier score of 0.25 is a random-guessing performance.
# 
# Second, we use the *calibration slope* to measure the direction and
# spread of the predicted
# probabilities [@Miller1991; @Jr1996; @Steyerberg2000; @DenBoer2005; @Steyerberg2013; @frank; @Cox1958].
# The calibration slope is the slope of a logistic regression model that
# is trained using the predicted probabilities of our original defect
# prediction model to predict whether a module will be defective or
# not [@Cox1958]. A calibration slope of 1 indicates the best classifier
# performance (i.e., the predicted probabilities are consistent with
# module's labels) and a calibration slope of 0 (or less) indicates the
# worst classifier performance (i.e., the predicted probabilities are
# inconsistent with module's labels)
# 
# Third, we use the *Area Under the receiver operator characteristic Curve
# (AUC)* to measure the discriminatory power of our models, as suggested
# by recent research
# [@Lessmann2008; @frank; @huang2005using; @DenBoer2005; @Steyerberg2008; @Steyerberg2013].
# The AUC is a threshold-independent performance metric that measures a
# classifier's ability to discriminate between defective and clean modules
# (i.e., do the defective modules tend to have higher predicted
# probabilities than clean modules?). AUC is computed by measuring the
# area under the curve that plots the true positive rate against the false
# positive rate, while varying the threshold that is used to determine
# whether a file is classified as defective or not. Values of AUC range
# between 0 (worst performance), 0.5 (random guessing performance), and 1
# (best performance). We use the `val.prob` function of the `rms` R
# package [@rms] to calculate the Brier score, calibration slope, and AUC.
# 
#  -->

# In[ ]:




