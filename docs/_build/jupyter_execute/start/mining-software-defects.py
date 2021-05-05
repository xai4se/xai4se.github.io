#!/usr/bin/env python
# coding: utf-8

# 
# 
# ## Mining Software Defects
# 
# Defect data preparation involves several key steps.
# Figure~\ref{fig:defect-data-preparation} provides an overview of defect data preparation steps.
# First, one must extract issue reports, which describe defects, feature requests, or general maintenance tasks from an Issue Tracking System (ITS, e.g., JIRA).
# Second, one must extract commit logs, code snapshots, and historical code changes that are recorded in a Version Control System (VCS, e.g., Git).
# Third, one must extract software metrics of each module (e.g., size, and complexity) from the VCS.
# To extract such software metrics, one must focus on development activities that occur prior to a release of interest that corresponds to the release branch of a studied system to ensure that activities that we study correspond to the development and maintenance of the official software releases. 
# Finally, one must identify and label modules as defective if they have been affected by code changes that address issue reports that were classified as defects after the software is released (i.e., post-release defects).
# On the other hand, modules that are not changed to address any issue reports are labelled as clean.
# 
# ```{figure} /start/images/data-preparation.png
# ---
# name: data-preparation
# ---
# An overview of defect data preparation steps.
# ```
# 
# Prior studies proposed several approaches to identify post-release defects, which we describe below.
# 
# 
# ```{figure} /start/images/defect-labelling.png
# ---
# name: defect-labelling
# ---
# An illustrative example of defect identification approaches, where ID indicates an issue report ID, v indicates affected release(s), C indicates a commit hash, indicates changed file(s), and the grey area indicates the 6-month period after a release of interest (i.e., Release 1.0).
# ```
# 
# ### The heuristic approach
# 
# Post-release defects are defined as modules that are changed to address a defect report within a post-release window period (e.g., 6 months) {cite}`zimmermann2007predicting,fischer2003populating,d2010extensive,d2012evaluating,Kamei2013,sliwerski2005changes`.
# The commonly-used approach is to infer the relationship between the defect-fixing commits that are referred in commit logs and their associated defect reports.
# To identify defect-fixing commits, Fischer et al. {cite}`fischer2003populating` are among the first to introduce a heuristic approach by using regular expression to search for specific keywords (e.g., \texttt{fix(e[ds])?}, \texttt{bugs?}, \texttt{defects?}) and issue IDs (e.g., \texttt{[0-9]+}) in commit logs after the release of interest.
# 
# To illustration, we use Figure X to provide an example of defect identification of the heuristic approach for the release \texttt{v1.0}.
# First, the heuristic approach will apply a collection of regular expression patterns to search through the commit logs to find defect-fixing commits within a specific window period (i.e., 6 months).
# According to Figure X, the heuristic approach will label commits \texttt{C1}, \texttt{C2}, and \texttt{C3} as defect-fixing commits, since their commit logs match with the collection of regular expression patterns that contain specific keywords and issue IDs.
# Then, the heuristic approach will label modules \texttt{A.java}, \texttt{B.java}, and \texttt{C.java} as defective modules.
# The remaining module (i.e., \texttt{D.java}) will be labelled as clean.
# 
# Unfortunately, such the heuristic approach has several limitations.
# First, the heuristic approach assumes that all defect-fixing commits that are identified within the post-release window period of the release of interest (i.e., \texttt{v1.0}) are the defect-fixing commits that affect the release of interest.
# However, Figure~\ref{fig:defect-identification} shows that the commit \texttt{C2} was changed to address the issue report \texttt{ID-2} where the release \texttt{v0.9} was affected.
# Thus, the module \texttt{B.java} that was labelled as defective by the heuristic approach is actually clean.
# Second, the heuristic approach assumes that all defect-fixing commits that affect the release of interest (i.e., \texttt{v1.0}) only occur within the post-release window period of the release of interest.
# Figure~\ref{fig:defect-identification} shows that the commit \texttt{C4} was made to address the issue report \texttt{ID-4} where the release \texttt{v1.0} was affected, however the commit \texttt{C4} was made outside the post-release window period.
# Thus, the module \texttt{D.java} that was labelled as clean by the heuristic approach is actually defective.
# 
# ### The realistic approach
# 
# Recently, da Costa et al. {cite}`da2017framework` suggest that the affected-release field in an ITS should be considered when identifying defect-introducing changes.
# To address the limitations of the heuristic approach, one should use the realistic approach, i.e., the use of the earliest affected release that is realistically estimated by a software development team for a given defect to generate post-release defects.
# The affected-release field in an ITS allows developers to record the actual releases of the system that are affected by a given defect.
# To identify defect-fixing commits, the realistic approach retrieves defect reports that affect a release of interest in the ITS.
# Since modern ITSs, like JIRA, provide traceable links between defect reports and code commits in VCS, the realistic approach can identify modules that are changed to address those defect reports.
# Then, the modules that are changed to address those defect reports are then identified as defective, otherwise clean.
# 
# To illustration, Figure~\ref{fig:defect-identification} shows that there are three issue reports (i.e., \texttt{ID-1}, \texttt{ID-3}, and \texttt{ID-4}) that affect the studied release \texttt{v1.0}.
# Then, commits \texttt{C1}, \texttt{C3}, and \texttt{C4} which are linked to those three issue reports are identified as defect-fixing commits by the realistic approach.
# Finally, modules \texttt{A.java}, \texttt{C.java}, and \texttt{D.java} which are impacted by commits \texttt{C1}, \texttt{C3}, and \texttt{C4} are labelled as defective modules.
# 
# 
# ### Challenges of mining software defects 
# 
# Software repositories are often noisy (e.g., incorrect, missing information) {cite}`liebchen2008data,bird2009promises`.
# For example, Aranda and Venolia {cite}`Aranda2009` point out that ITS and VCS repositories are noisy sources of data.
# Thus, the usage of such noisy data may pose a critical threat to the validity in many empirical studies.
# 
# Prior studies show that noise may creep into defect datasets and impact defect models if care is not taken when collecting data from software repositories.
# The first line of studies includes an investigation of the impact of noises that are generated by issue report misclassification.
# For example, Antoniol {cite}`Antoniol` and Herzig {cite}`Herzig2013` find that many issue reports are misclassified.
# However, recent work shows that issue report mislabelling rarely impacts the precision of defect models or the interpretation of the most important software metrics {cite}`Tantithamthavorn`.
# The second line of studies includes studies an investigation of the impact of noises that are generated by defect identification approaches.
# For example, Bachmann et al. {cite}`Bachmann2010` find that the defect reports are not recorded in the commit logs and thus are not visible to the automated linking tools used to extract defect datasets, which generate many missing links between code changes and defect reports.
# Bird et al. {cite}`Bird2009` point out that more experienced developers are more likely to explicitly link issue reports to the corresponding code changes.
# Nguyen et al. {cite}`Nguyen2010` show that such noises also exist in commercial datasets.
# Furthermore, Rahman et al. {cite}`rahman2013and` argue that the size of the defect datasets matters more than the dataset quality.
# To address this challenge, prior studies {cite}`Wu2011,Nguyen2012` introduce the textual similarity approaches between issue reports and commit messages to automatically recover the missing links between issue reports to the corresponding code changes.
# 
