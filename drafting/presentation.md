---
title: "Introduction to Python"
author: "Dr Musashi Jacobs-Harukawa"
institute: "DDSS @ Princeton University"
date: "15 Aug 2023"
section-titles: false
aspectratio: 1610
mainfont: "IBM Plex Sans-Light"
css: "minimal-theme.css"
---

# Preface

- About me
- Learning objectives
    - What I included
    - What I left out
- Python for research
    - For researchers: what do we use Python for?
    - For coders: how do the objectives differ in research?
- Tools/terms of the trade
    - Script
    - Interactive coding
    - Libraries, environments
    - IDEs

## Ground Rules

- Asking questions
- Contacting me


## About Me 

- Postdoc Data-Driven Social Science Initiative, Princeton University
- Research: Applied ML/Social Science Methodology (primarily NLP)
- Previously: DPhil University of Oxford
- Previously previously: Data Scientist in Finance


## Tech Check

- Open the following link and follow the instructions.
- Once you have run the command in the notebook, come back to me.
- If you have issues, directly message Johannes.


## Learning Objectives

- How is Python used in (social science) research?
- Basic Python operations and control structures
- Basic data analysis in Python


# Python for Research

## For Researchers: what do we use Python for?

- Generally: _any repetitive task done on a computer can be automated with Python_.
- Ways I use it:
    - Data collection (web scraping)
    - Data cleaning/analysis
    - Data visualization
    - Machine learning
    - Deep learning

## For Engineers: research vs development

- Research: scripting, interactive usage
- Development: application development

## Suggestions: Python Research Tools

- IDE: VSCode, Jupyter
- Package Management: Conda/Mamba


<!-- ## A Description:

Python is an _open-source, general-purpose scripting language_.

## Open-Source

- Built by a community
- Maintained by a community
- Free to use for all

## General-Purpose

- If you're doing it on a computer and there's some repetitive element, then you can automate it in Python.
- Python isn't limited to Data Science, but it's very popular with data scientists!

::: .notes
Large community means that a larger number of people create, contribute to, and maintain the data analysis tools that we all use.
:::

## Scripting

- No strict definition for what a "script" is.
- Series of commands to automate some task.
- Like a pipeline: takes some inputs, does some things to these inputs, and gives back some outputs.

::: .notes
> - It's good to keep the input-output framework in your head.
> - Also not strictly limited to scripting; Python is widely used for applications development.
> - For our purposes, however, its common usage for scripting is a big plus, as that's what we usually do.
:::

## Language

- Python is a language, and not an application.
- Practical difference for you:
    - most applications provide you options to select from.
    - languages require to generate commands from accepted rules.
- Upshot is that you can do nearly anything with Python!

## what can I use Python for?

I want to...

- Clean up my messy data!
- Run analyses with (hundreds of) millions of data points
    - it won't fit into an excel spreadsheet!
- I want to automate downloading several decades of newspaper articles!
- I want to create beautiful (interactive) visuals to accompany my analyses!
- I want to uncover hidden structures linking parliamentary committees!
- Again: _any repetitive task done on a computer can be automated with Python_.

## Python vs Alternatives

- `Python` and `R` popular languages for data analysis


# Tools of the Trade

## Development

- Writing Code
- Executing Code

## Jupyter

- Interactive code editor.
- Multiple options: console, notebook and lab

## Google Colab

- Google's cloud-based Jupyter notebooks
- Sufficient for this class

## Managing Libraries

For managing Python packages, I recommend Anaconda.

- Environment and software manager.
- Recommended solution for Python installation and management.
- Can be used from the command line (`cli`) or browser-like interface (anaconda-navigator).

::: .notes
> - Discuss briefly why Python requires a manager, and why you might want to use it locally.
:::

## Other Options

- I use Atom or VIM to write code
- PyCharm is popular with developers
- If you've spent a lot of time with RStudio, you may prefer Spyder. -->

# Before we start coding

## Data Types and Structures

- Two fundamental concepts in coding:
  - Data Types
  - Data Structures

## Why Automate?

- Advantage of automation cost, scale, and scope.
- To harness computational methods, need to represent our observations in a way that algorithms and programs can utilise.
- Process of quantifying and structuring our observations usually entails loss of some information.

::: .notes
> - As social scientists, our goal when automating 
- This automation is not limited to collecting data. Running a regression or sorting your responses by data is the automation of doing this by hand.
- Some qualitative scholars I speak to contend that the validity of the quantitative endeavour ends there.
    - Are there unquantifiable things?
- I'm more optimistic about what is possible, and think that the key to having valid quantitative inferences is to be extremely clear on the connection between the data in your analysis and the actual events you are measuring.
:::

## Bridging the Gap between Qualitative and Quantitative Methods

- Choosing a representation of your information that retains relevant properties is key.
- To read more about this particular debate, a good starting point is [Stevens (1946)](https://pdfs.semanticscholar.org/2680/6102a45a6104489872dd3241b6e8030bbc40.pdf).

::: .notes
- I would love to discuss this further, but this isn't really that kind of methods class.
:::

## Data Types

Some (statistical) data types:

- Logical
- Numerical
- Categorical
- Text
- Date and time


::: .notes
- What do I mean when I talk about different "types" of data?
- Small exercise: what are instances of each of these?
:::

## Representing Data on a Computer

- _Good news:_ Python, like most modern programming languages, has ways to represent each of the data types listed above.
- _Bad news:_ At a fundamental level, this is being stored as 0's and 1's.
- _Take away:_ Take the time to understand the relationship between:
    -  your empirical observations,
    -  the abstracted representation of them in your mathematical model,
    -  the approximation of this in your computational model.

::: .notes
- I'm making a bit of an assumption here about the theory-generating workflow, in that a stylised mathematical model is usually prior to a computational/empirical approach.
:::

## Data Structures

- Data types are concerned with the representation of individual data points, or observations.
- Data structures are concerned with the relations between observations.
    - Are the data points members of the same set?
    - Are the data points members of the same sequence?
    - Are the data points different features of single empirical unit?



# "Base" Python

## "Base"

- Like many languages, Python is enhanced by a great number of "libraries".
- Libraries extend the functionality of a language, e.g. for data analysis.
- "Base" Python refers to commands and functionality 
- First learn some base functionality that is common to most applications.


