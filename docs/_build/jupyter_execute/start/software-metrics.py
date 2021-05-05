#!/usr/bin/env python
# coding: utf-8

# # Software Metrics
# 
# 
# To prepare a defect dataset, we first \textit{extract metrics} of software modules (e.g., size, complexity, process metrics) from a version control system (VCS).
# We focus on the development activity that occurs prior to a release that corresponds to the \texttt{release} branch of a studied system. 
# With this strictly controlled setting, we ensure that changes that we study correspond to the development and maintenance of official software releases.
# Since modern issue tracking systems, like JIRA, often provide traceable links between issue reports (i.e., a report described defects or feature requests) and code changes, we can identify the modules that are changed to address a particular issue report.
# Finally, we \textit{label defective modules} if they have been affected by a code change that addresses an issue report that is classified as a defect.
# Similar to prior studies {cite}`zimmermann2007predicting,Ambros,Kamei2013`, we define post-release defects as modules that are changed to address an issue report within the six-month period after the release date.
# 
# 
# 
# To understand the characteristics of defect-proneness, prior studies proposed a variety of metrics that are related to software quality.
# We provide a brief summary of software metrics below.
# 
# **Code metrics** describe the relationship between code properties and software quality.
# For example, in 1971, Akiyama {cite}`akiyama1971example` is among the first research to show that the size of modules (e.g., lines of code) shares a relationship with defect-proneness. 
# McCabe et al. {cite}`mccabe1976complexity` and Halstead also show that the high complexity of modules (e.g., the number of distinct operators and operands) are likely to be more defective.
# Chidamber and Kemerer {cite}`chidamber1994metrics` also propose CK metrics suites, a set of six metrics that describe the structure of a class (e.g., the number of methods defined in a class), that may share a relationship with defect-proneness.
# An independent evaluation by Basili et al. {cite}`basili1996validation` and Gyimothy et al. {cite}`gyimothy2005empirical` confirms that the CK metrics suites can be effectively used as software quality indicators.
# An in-depth investigation on the size-defect relationship by Syer {cite}`syer2014replicating` shows that defect density has an inverted "U" shaped pattern (i.e., defect density increases in smaller files, peaks in the largest small-sized files/smallest medium-sized files, then decreases in medium and larger files).
# Such code metrics are typically extracted from a code snapshot at a release using various available static analysis tools (e.g., SLOCcount (https://sourceforge.net/projects/sloccount/), Understand tool (https://scitools.com/), the *mccabe* python package\footnote{\url{https://pypi.python.org/pypi/mccabe}}, and the *radon* python package (https://pypi.python.org/pypi/radon).
# 
# **Process metrics** describe the relationship between change activities during software development process and software quality. 
# Prior work has shown that historical software development process can be used to describe the characteristics of defect-proneness.
# For example, Graves {cite}`Graves2000` find that the software defects may still exist in modules that were recently defective.
# Nagappan and Ball {cite}`Nagappan2005,nagappan2007using` find that modules that have undergone a lot of change are likely to be more defective.
# Hassan {cite}`hassan2009predicting` find that modules with a volatile change process, where changes are spread amongst several files are likely defective.
# Hassan and Holt {cite}`Hassan2005` find that modules that are recently changed are more likely to be defective.
# Zimmermann and Nagappan {cite}`Zimmermann2009,Zimmermann2008,zimmermann2007predicting` find that program dependency graphs share a relationship with software quality.
# Zimmermann et al. {cite}`zimmermann2007predicting` find that the number of defects that were reported in the last six months before release for a module shares a relationship with software quality.
# Such process metrics are typically extracted using code changes that are stored in VCSs.
# 
# 
# **Organization metrics** describe the relationship between organization structure and software quality {cite}`nagappan2008influence`.
# For example, Graves et al. {cite}`Graves2000` find that modules that are changed by a large number of developers are likely to be more defective.
# Despite of the organization structure, prior studies have shown that code ownership shares a relationship with software quality.
# Thus, we focus on the two dimensions for an approximation of code ownership.
# First, **authoring activity** has been widely used to approximate code ownership.
# For example, Mockus and Herbslerb {cite}`mockus2002expertise` identify developers who responsible for a module using the number of tasks that a developer has completed.
# Furthermore, Bird et al. {cite}`Bird2011a` find that modules that are written by many experts are less likely to be defect-prone.
# Second, **reviewing activity** has been also used to approximate code ownership.
# For example, Thongtanunam {cite}`thongtanunam2016revisiting` find that reviewing expertise also shares a relationship with defect-proneness (e.g., modules that are reviewed by experts are less likely to be defect-prone). 
# 
# ADD: Social Network, Geographical, Social, Human-Factor, Test
