## Software Analytics


The success of software engineering projects largely depends on complex
decision-making. For example, which tasks should a developer do first,
who should perform this task, is the software of high quality, is a
software system reliable and resilient enough to deploy, etc. However,
erroneous decision-making for these complex questions is costly in terms
of money and reputation.

Today's software development processes depend on a variety of
development tools, such as issue tracking systems, version control
systems, code review, continuous integration, continuous deployment, and
Q&A websites. Such tools generate large quantities of unstructured
software artefacts at a high frequency (so-called Big Data) in many
forms like issue reports, source code, test cases, code reviews,
execution logs, app reviews, developer mailing lists, and discussion
threads.

Software Analytics is a sub-field in software engineering that focuses
on leveraging AI/ML and data *analytics* techniques to uncover
interesting and actionable knowledge from the unprecedented amount of
*software data* {cite}`menzies2013software` {cite}`tantithamthavorn2018pitfalls`.
Many software organisations (e.g., Microsoft, Facebook, and Google)
currently use powerful AI/ML techniques to make data-driven engineering
decisions and automate software engineering tasks. For example, software
defect prediction, effort estimation, task prioritization, task
recommendation, expert recommendation, code generation, developers'
productivity prediction, malware detection, and security vulnerability
detection.

## Stop Telling Me What Is


While the adoption of software analytics enables software organisations
to distill actionable insights and support decision-making, there are
still many barriers to the successful adoption of such software
analytics in software organizations {cite}`dam2018explainable`.

First, most software practitioners do not understand the reason behind
the predictions from software analytics systems {cite}`dam2018explainable`.
They often ask the following questions:

-   Why is this person best suited for this task?

-   Why is this file predicted as defective?

-   Why is this task required the highest development effort?

-   Why should this task be done first?

-   Why is this developer predicted to have low productivity?

-   How can we improve the quality of software systems in following
    iterations?

These concerns about a lack of explanation often leads to a lack of
trust and transparency, hindering the adoption of software analytics in
practice.

Second, software practitioners are often affected by the decision-making
from software analytics. Our recent work also found that practitioners
are very concerned about their privacy and fairness if defect prediction
models were deployed in practice. Practitioners even asked \"Would
developers be laid-off due to the use of defect prediction models for
identifying who are most likely to introduce software
defects?\" {cite}`jiarpakdee2021perception`. Article 22 of the European
Union's General Data Protection Regulation (GDPR) states that the use of
data in decision-making that affects an individual or group requires an
**explanation** for any decision made by an algorithm. Unfortunately,
current software analytics still often do not uphold privacy
laws {cite}`jiarpakdee2020modelagnostic`. Thus, the risks of unjustified
decision-making of software analytics systems can be catastrophic,
leading to potentially erroneous and costly business
decisions {cite}`dam2018explainable`.

## Is the Community Moving to the Right Direction?

### Researchers' Focuses


We conducted a literature analysis to better understand what researchers
are currently focusing on for defect explanation. We collected 96
primary defect prediction studies that were published in top-tier
Software Engineering venues (i.e., TSE, ICSE, EMSE, FSE, and MSR) during
2015-2020 (as of 11 January 2021). We then characterized the key goals
of each defect prediction study into three main goals: (1) predictions;
(2) model explanation; and (3) instance
explanation {cite}`jiarpakdee2021perception` **TODO (see
Figure**. We found that 91% (81/96) of the defect
prediction studies only focus on making predictions, without considering
explaining the predictions. As few as 4% of the defect prediction
studies focus on explaining the predictions of defect prediction models
**TODO (see Figure)**. This indicates that the explainability and
actionability of software analytics is still very under researched.

### Practitioners' Needs

We conducted a qualitative survey to better understand what
practitioners perceive as the usefulness of each goal of defect
prediction models. We found that practitioners perceive that the
explainability and actionability of software analytics are as **equally
useful** as the predictions {cite}`jiarpakdee2021perception`. 82% of our
respondents said that the explanability goal (generating model
explanations and instance explanations) is as useful as the prediction
goal. Thus, we argue that **explainable and actionable software
analytics is urgently and critically needed**. The research and practice
communities should thus start answering the key question: *\"How can we
make software analytics more explainable and actionable?\"*.

### Explainable AI for SE: A Way Forward


Explainable AI is a suite of AI/ML techniques that produce accurate
predictions, while being able to explain such predictions. The purpose
of increasing the explainability of software analytics (XAI4SE) is to
make its behavior more intelligible to humans by providing explanations.
The explainability of software analytics can be achieved by:

-   **"Global Explanability\":** Using interpretable machine learning
    techniques (e.g., decision tree, decision rules or logistic
    regression techniques) or intrinsic model-specific techniques (e.g.,
    ANOVA, variable importance) so the entire predictions and
    recommendations process are transparent and comprehensible. Such
    intrinsic model-specific techniques aim to provide the global
    explainability. Thus, users can only understand how the model works
    globally (e.g., by inspecting a branch of decision trees). However,
    users often do not understand why the model makes that prediction.

-   **"Local Explanability\":** Using model-agnostic techniques (e.g.,
    LIME {cite}`ribeiro2016should`) to explain the predictions of the
    software analytics models (e.g., neural network, random forest).
    Such post-hoc model-agnostic techniques can provide an explanation
    for each prediction (i.e., an instance to be explained). Users can
    then understand why the prediction is made by the software analytics
    models.
    
    
## Please Tell Me What To Do!

We discuss some initial evidence from a successful case study of using
Explainable AI for Software Engineering in the context of software
defect prediction {cite}`rajapaksha2021sqaplanner`.

**Background.** In today's increasingly digitalized world, software
defects are widespread and enormously expensive, but they are very hard
to detect, predict, and prevent. Thus, a failure to eliminate software
defects in safety-critical systems could result in serious injury to
people, threats to life, death, and disasters.

Traditionally, software quality assurance activities -- software testing
and code review -- are widely adopted to discover software defects in
software systems. However, ultra-large-scale systems, such as, Google,
can have more than two billion lines of code. Thus, exhaustively
reviewing and testing every single line of code is not feasible with
limited time and resources. Defect prediction---an AI/ML model trained
on historical data to predict if a file/commit will be defective in the
future---has been proposed to help developers prioritize their limited
software quality assurance resources on the most risky files/commits.

**Gaps.** However, developers often do not understand why a file is
being predicted as defective. In addition, such predictions and global
explanations are still often not
actionable {cite}`jiarpakdee2018impact`---i.e., developers do not know what
to actually do -- or what to avoid doing -- in order to improve the
quality of the software system. These limitations often lead to a lack
of trust in the predictions, hindering the adoption of defect prediction
models in practice.

Let's consider a scenario where a defect prediction model indicates that
*file size* is associated with defect-proneness i.e. code in bigger
files is likely to be more defective. This insight may help managers
develop quality improvement plans that, in the next development
iteration, developers should pay attention to the file size to mitigate
the risk of having defects. However, such insights do not provide a
concrete suggestion of what to do and what to avoid (i.e. does
increasing or decreasing size reduce or increase defects?). Thus, a lack
of such actionable guidance remains an extremely challenging problem,
often leading to ineffective software quality improvement plans.

**Approach.** To generate actionable guidance, we used a rule-based
model-agnostic technique to generate a rule-based explanation for each
prediction of defect prediction models {cite}`rajapaksha2021sqaplanner`. We
first build file-level defect prediction models that are trained using
traditional software features (e.g., lines of code, code complexity, the
number of developers who edited a file) with a random forest
classification technique. For each prediction, we applied a rule-based
model-agnostic technique to generate two types of actionable guidance
(i.e., what developers should do to mitigate the risk of having defects
and what developers should not do to avoid increasing the risk of having
defects).

**TODO Figure-Rules**

**Visualizing the actionable guidance.** For each guidance, we
translated a rule-based explanation into an actionable guidance. Then,
we developed a proof-of-concept to visualize the actionable guidance
using a bullet plot **(see
Figure)**. The visualization is designed to provide the
following key information: (1) the list of guidance that practitioners
should follow and should avoid; (2) the actual feature value of that
file; and (3) its threshold and range values for practitioners to follow
to mitigate the risk of having defects. The green shades indicate the
non-risky range values of features, while the red shades indicate the
risky range values of features. The vertical bars indicate the actual
values of features for a given file. The green arrows provide directions
of how a feature should be changed (i.e., increase or decrease). The
provided guidance is structured into two parts: (1) what to do to
*decrease the risk* of being defective; and (2) what to avoid to *not
increase the risk* of being defective.

**TODO Figure X** shows an example of such actionable guidance to
help managers develop their quality improvement plans. In this example,
to decrease the risk of having defects, developers should consider (1)
decrease the number of class and method declaration lines to less than
29 lines, (2) decrease the number of distinct developers to less than 2
developers, (3) increase the proportion of code ownership to more than
0.85, (4) decrease the number of blank lines to less than 8 lines, (5)
decrease the number of output variables to less than 2 variables.
Nevertheless, to not increase the risk of having defects, developers
should consider avoid decreasing the comment to code ratio and avoid
increasing the number of minor or junior developers.

**User Study Evaluation.** We conducted a qualitative survey to
investigate the practitioners' perceptions of our visualization
approach. We also used the visualization of Microsoft's Code Defect AI
as a baseline comparison.

**Results.** We found that 80% of our respondents agree that our
visualization is better for providing actionable guidance when compared
to the visualization of Microsoft's Code Defect AI. In addition, 63%-90%
of the respondents agree with the seven actionable guidance provided by
our approach.

## Lessons Learned

Based on these findings, we summarise our key lessons learned:

1.  Explainable AI is very important in software engineering, but is
    still under-researched {cite}`jiarpakdee2021perception`.

2.  Explainable AI techniques can be used in software engineering to
    provide explanations of the predictions and actionable guidance to
    support software engineering tasks {cite}`rajapaksha2021sqaplanner`.
    Other initial successful evidence can be found at {cite}`chen2018applications`{cite}`jiarpakdee2020modelagnostic`{cite}`krishna2020prediction`{cite}`peng2020defect`{cite}`wattanakriengkrai2020`.

However, there are several open research questions that remain largely
unexplored:

-   What is the best form of explanations for software engineering tasks
    that are most understandable to software developers?

-   Do different stakeholders need different forms of explanations in
    software engineering?

-   How can we measure the quality and value of explanations in software
    engineering?

-   How do explanations from explainable AI domains impact software
    engineering practices?

-   What are the other application areas in software engineering that
    need explanations?

-   How can we improve the explanations for other complex AI/ML
    algorithms (e.g., deep learning, optimization, natural language
    processing) to address other software engineering tasks?

We developed an interactive tutorial of Explainable AI tools for SE to
support future research. This can be found at <http://xai4se.github.io>.
We hope this article will motivate future work to address these
important questions, which require the SE community to work together
with other disciplines and communities (e.g., Explainable AI, Visual
Analytics, Natural Language Processing, Human-Centric Software
Engineering).