#!/usr/bin/env python
# coding: utf-8

# # Software Quality Assurance
# 
# Our society is now driven by software. But, one software defect could have an ultimate impact on our society, financial economy, and human lives, ranging from IT services disruption, massive overdose of radiotherapy of Therac-25, to an explosion of the Ariane 5 rocket. These failures are often due to the discovery of the majority of software defects after release, while they are often introduced in the early development life cycle like the requirements, design, release planning. Since the cost of fixing software defects is exponentially increased (Brooks 1995), finding and fixing software defects prior to releasing software is usually much cheaper and faster. 
# 
# **Software Quality Assurance (SQA)** is neither a process nor a phase but a must-need systematic practice to ensure that the product meets the quality standards, especially for the development of any life-impacting and safety-critical software systems. Thus, QA practices must be embedded as a quality culture throughout the life cycles from planning to release so teams can follow best practices to prevent defects, rather than wasting time detecting them.
# 
# However, modern software development practices like Agile pose several challenges to the current SQA practices. In modern practices, everyone is accountable and quality is everyone’s responsibility. Thus, developers are encouraged to test their own code and to write sufficient and effective unit tests to ensure the new code has no obvious errors and to get notified quickly as soon as something is broken. Several defect detection tools are used during the software development life cycle. For example, automation testing (e.g., CI/CD) can be used to enable the automation of test execution where the code coverage is used to infer a certain level of quality in the meaningful test cases. Static analysis is used to detect bugs, but produce too many false positives or false alarms. Code review can be used to review all code changes prior to integrating a pull request into the main branch repository. 
# 
# Despite these SQA tools being invested and adopted, software defects might still occur since these tools do not guarantee a defect-free software product. They also neither identify the problematic areas that may lead to software defects after release (i.e., post-release software defects) nor provide any actionable guidance how to mitigate risks. As a result, it could lead to ineffective and inefficient software quality assurance practices. Teams may release poor quality of software products to customers, causing slow project progress and high costs of software development, unsatisfactory software products, unhappy end-users, and serious monetary and reputation losses for that software organization. 
# 
# 

# {numref}`Figure {number} <sqa-overview>` illustrates a simplified software engineering workflow that includes SQA activities.
# 
# ```{figure} /start/images/sqa-overview.jpeg
# ---
# name: sqa-overview
# ---
# An overview of the software quality assurance activities.
# ```
# 
# ## SQA activities during the development stage
# 
# During the development stage, new features and other code changes are implemented by developers.
# Such code changes (or commits) must undergo rigorous SQA activities (e.g., Continuous Integration tests and code review) prior to merge into the main branch (e.g., a master branch) {cite}`gousios2014exploratory`.
# Since these commit-level SQA activities are time-consuming, Just-In-Time defect prediction has been proposed to support developers by prioritizing their limited SQA effort on the most risky code changes that will introduce software defects during the development cycle (i.e., pre-release defects) {cite}`Kamei2013` {cite}`pascarella2019fine`.
# Nevertheless, JIT defect prediction only early detects defect-inducing changes, rather than post-release defects (i.e., the areas of code that are likely to be defective after a release).
# Despite the SQA activities during the development cycle (e.g., code reviews), it is still possible that software defects still slip through to the official release of software products {cite}`ThongtanunamMSR2015` {cite}`thongtanunam2016revisiting`.
# Thus, SQA activities are still needed during the release preparation.
# 
# ## SQA activities during the release preparation
# 
# During the release preparation, intensive SQA activities must be performed to ensure that the software product is of high quality and is ready for release, i.e., reducing the likelihood that a software product will have post-release defects {cite}`adams2016modern` {cite}`Nagappan2005`.
# In other words, the files that are changed during the software development need to be checked and stabilized to ensure that these changes will not impact the overall quality of the software systems {cite}`lucidchart` {cite}`herzig2014using` {cite}`rahman2015release`.
# Hence, several SQA activities (e.g., regression tests, manual tests) are performed {cite}`adams2016modern`.
# However, given thousands of files that need to be checked and stabilized before release, it is intuitively infeasible to exhaustively perform SQA activities for all of the files of the codebase with the limited SQA resources (e.g., time constraints), especially in rapid-release development practices.
# To help practitioners effectively prioritize their limited SQA resources, it is of importance to identify **what are the most defect-prone areas of source code that are likely to have post-release defects**.
# 
# Prior work also argued that it is beneficial to obtain early estimates of defect-proneness for areas of source code to help software development teams develop the most effective SQA resource management {cite}`Nagappan2005b` {cite}`Nagappan2005`.
# Menzies et al. mentioned that software contractors tend to prioritize their effort on reviewing software modules tend to be fault-prone {cite}`menzies2007data`.
# A case study at ST-Ericsson in Lund, Sweden by Engstr{\"{o}}m et al. {cite}`Engstrom2010` found that the selection of regression test cases guided by the defect-proneness of files is more efficient than the manual selection approaches.
# At the Tizen-wearable project by Samsung Electronics {cite}`Kim2015`, they found that prioritizing APIs based on their defect-proneness increases the number of discovered defects and reduces the cost required for executing test cases.
# 
# 
# 

# In[ ]:




