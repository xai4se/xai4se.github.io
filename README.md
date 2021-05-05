[![Website xai4se.github.io/book](https://img.shields.io/website-up-down-green-red/https/xai4se.github.io.svg)](https://xai4se.github.io/book)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
&nbsp;
[![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange.svg)](https://www.jupyter.org/)
&nbsp;
[![License: MIT (Code), CC BY-NC-SA (Book)](https://img.shields.io/badge/License-MIT_(Code),_CC_BY--NC--SA_4.0_(Book)-blue.svg)](https://github.com/xai4se/xai4se.github.io/blob/master/LICENSE.md)

# Explainable AI for Software Engineering: 

A Hands-on Guide on How to Make Software Analytics More Practical, Explainable, and Actionable

## About this Book

The success of software engineering projects largely depends on complex decision-making. For example, which tasks should a developer do first, who should perform this task, is the software of high quality, is a software system reliable and resilient enough to deploy, etc. However, erroneous decision-making for these complex questions is costly in terms of money and reputation. Thus, Artificial Intelligence/Machine Learning (AI/ML) techniques have been widely used in software engineering for developing software analytics tools and techniques to improve decision-makings, developer productivity, and software quality. However, the predictions of such AI/ML models for software engineering are still not practical (i.e., fine-grained), not explainable, and not actionable. These concerns often hinder the adoption of AI/ML models in software engineering practices. Are we moving to the right direction? How can we improve the SE community (both research and education)? In this book, we first provide a recipe to avoid building unsound software analytics. Then, we introduce the fundamental knowledge of Explainable AI for Software Engineering. Finally, we demonstrate three successful case studies on how Explainable AI techniques can be used to address the aforementioned challenges by making the predictions of software defect predction models more practical, explainable, and actionable.

## Contributing

1. Create a conda environment ```conda env create -f environment.yml```, then activate the environment ```conda activate xaitools```

2. Add kernel to jupyter ```python -m ipykernel install --name xaitools --display-name "xaitools"```

3. Build the book ```jupyter-book build docs```
