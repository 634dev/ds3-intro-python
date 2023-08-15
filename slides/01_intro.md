---
title: "Introduction to Python"
author: "Dr Musashi Jacobs-Harukawa"
institute: "DDSS @ Princeton University"
date: "15 Aug 2023"
revealjs-url: "../reveal.js"
section-titles: false
aspectratio: 1610
mainfont: "IBM Plex Sans-Light"
theme: "white"
css: "minimal-theme.css"
---

# First Things

## Ground Rules

- Asking questions
- Contacting me

## Tech Check

- Open the following link and follow the instructions.
- Once you have run the command in the notebook, come back to me.

## Format

- Lecture
- Notebooks with same material as slides
- Additional exercises in repo


## About Me 

- Postdoc Data-Driven Social Science Initiative, Princeton University
- Research: Applied ML/Social Science Methodology (primarily NLP)
- Previously: DPhil University of Oxford
- Previously previously: Data Scientist in Finance


## Learning Objectives

- How is Python used in (social science) research?
- Basic base Python programming
- Basic data analysis in Python


# Python for Research

## For Beginners: A Description

Python is an _open-source, general-purpose scripting language_.

## Open-Source

- Built by a community
- Maintained by a community
- Free to use for all

## General-Purpose

- If you're doing it on a computer and there's some repetitive element, then you can automate it in Python.
- Python isn't limited to Data Science, but it's very popular with data scientists!


## Scripting

- No strict definition for what a "script" is.
- Series of commands to automate some task.
- Like a pipeline: takes some inputs, does some things to these inputs, and gives back some outputs.


## Language

- Python is a language, and not an application.
- Practical difference for you:
    - most applications provide you options to select from.
    - languages require to generate commands from accepted rules.
- Upshot is that you can do nearly anything with Python!


## For Researchers: what can we use Python for?

- Generally: _any repetitive task done on a computer can be automated with Python_.
- Ways I use it:
    - Data collection (web scraping)
    - Data cleaning/analysis
    - Data visualization
    - Machine learning
    - Deep learning

## For Engineers: how is research different from development?

- Research:
  - Usage: scripting, interactive usage
  - Concerns: ease of use, time-efficiency
- Development:
  - Use: application development
  - Concerns: portability, deployment, resource efficiency


## Python vs Alternatives

- `Python` and `R` popular languages for data analysis
- My observations on differences in:
    - Functionality
    - Contribution
    - Standards
    - Robustness
- Open source or nothing

## Python Research Tools

Suggestions:

- IDE: VSCode, Jupyter
- Package Management: Conda/Mamba


# Before we start coding

## Why Automate?

- Advantage of automation cost, scale, and scope.
- To harness computational methods, need to represent our observations in a way that algorithms and programs can utilise.
- Process of quantifying and structuring our observations usually entails loss of some information.

::: .notes
- As social scientists, our goal when automating 
- This automation is not limited to collecting data. Running a regression or sorting your responses by data is the automation of doing this by hand.
- Some qualitative scholars I speak to **contend** that the validity of the quantitative endeavour ends there.
    - Are there unquantifiable things?
- I'm more optimistic about what is possible, and think that the key to having valid quantitative inferences is to be extremely clear on the connection between the data in your analysis and the actual events you are measuring.
:::

## Representing Information

- Choosing a representation of your information that retains relevant properties is key.
- To read more about this particular debate, a good starting point is [Stevens (1946)](https://pdfs.semanticscholar.org/2680/6102a45a6104489872dd3241b6e8030bbc40.pdf).

## Data Types

Data types are concerned with the representation of individual data points, or observations.

- Logical
- Numerical
- Categorical
- Text
- Date and time

## Data Structures

Data structures are concerned with the relations between observations.

- Are the data points members of the same set?
- Are the data points members of the same sequence?
- Are the data points different features of single empirical unit?

## Representing Data on a Computer

- _Good news:_ Python, like most modern programming languages, has ways to represent each of the data types listed above.
- _Bad news:_ At a fundamental level, this is being stored as 0's and 1's.
- _Take away:_ Take the time to understand the relationship between:
    -  your empirical observations,
    -  the abstracted representation of them in your mathematical model,
    -  the approximation of this in your computational model.
