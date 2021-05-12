[![Website xai4se.github.io/book](https://img.shields.io/website-up-down-green-red/https/xai4se.github.io/book.svg)](https://xai4se.github.io/book)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
&nbsp;
[![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange.svg)](https://www.jupyter.org/)
&nbsp;
[![License: MIT (Code), CC BY-NC-SA (Book)](https://img.shields.io/badge/License-MIT_(Code),_CC_BY--NC--SA_4.0_(Book)-blue.svg)](https://github.com/xai4se/xai4se.github.io/blob/master/LICENSE.md)

# Explainable AI for Software Engineering: 

A Hands-on Guide on How to Make Software Analytics More Practical, Explainable, and Actionable


![Alt text](https://xai4se.github.io/book/_images/front-banner.png?raw=true "Book Cover")


## About this Book

The success of software engineering projects largely depends on complex decision-making. For example, which tasks should a developer do first, who should perform this task, is the software of high quality, is a software system reliable and resilient enough to deploy, etc. However, erroneous decision-making for these complex questions is costly in terms of money and reputation. Thus, Artificial Intelligence/Machine Learning (AI/ML) techniques have been widely used in software engineering for developing software analytics tools and techniques to improve decision-makings, developer productivity, and software quality. However, the predictions of such AI/ML models for software engineering are still not practical (i.e., fine-grained), not explainable, and not actionable. These concerns often hinder the adoption of AI/ML models in software engineering practices. Are we moving to the right direction? How can we improve the SE community (both research and education)? In this book, we first provide a recipe to avoid building unsound software analytics. Then, we introduce the fundamental knowledge of Explainable AI for Software Engineering. Finally, we demonstrate three successful case studies on how Explainable AI techniques can be used to address the aforementioned challenges by making the predictions of software defect predction models more practical, explainable, and actionable.

### What you will learn

In this book, we:

* Present a concise yet essential introduction to the most important aspects of software analytics.
* Introduce hands-on approaches to implementing software analytics.
* Demonstrate tools and techniques to make software analytics explainable and actionable.
* Provide examples case studies.

### Who this book is for

Some of the potential readers of this book include:

1. Software practitioners who already use Python for as data science, machine learning, research, and analysis and wish to apply their data science knowledge to software data.

2. Software analysts and data scientists who want to understand and avoid pitfalls when desigining software analytics.

3. Project managers who involve high-stakes decision-making and need software analytics to make smarter data-driven busineess decisions.

**Caution:** This book is not an introduction to data science, machine learning, or artifcial intelligence concepts. You must have some foundational knowledge and/or experience with machine learning libraries such as scikit-learn to make the most out of this book.

### About the authors

**Dr. Chakkrit (Kla) Tantithamthavorn** is a Senior Lecturer in Software Engineering and a 2020 ARC DECRA Fellow in the Faculty of Information Technology, Monash University, Australia. He is leading a new research area of Explaianble AI for Software Engineering. His current fellowship is focusing on the development of Practical and Explainable Analytics to Prevent Future Software Defects. His work has been published at several top-tier software engineering venues, such as TSE, ICSE, EMSE, MSR, IST. Contact him at chakkrit@monash.edu.

**Dr. Jirayus Jiarpakdee** is graduated from Monash University, Australia. His research interests include empirical software engineering and mining software repositories (MSR). The goal of his Ph.D. is to apply the knowledge of statistical modelling, experimental design, and software engineering to improve the explainability of defect prediction models. Contact him at jirayus.jiarpakdee@monash.edu.


### Cite this book:

```
@incollection{analyticscookbook,
    author = {Chakkrit Tantithamthavorn and Jirayus Jiarpakdee},
    booktitle = {Explainable AI for Software Engineering},
    year = {2021},
    publisher = {Monash University},
    howpublished = {\url{http://xai4se.github.io/book}},
    note = {Retrieved 2021-04-09},
    url = {http://xai4se.github.io/book},
    urldate = {2021-04-09}
}
```

### Contributing

1. Create a conda environment ```conda env create -f environment.yml```, then activate the environment ```conda activate xaitools```

2. Add kernel to jupyter ```python -m ipykernel install --name xaitools --display-name "xaitools"```

3. Build the book ```jupyter-book build docs```
