[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/VtaH1Plp)
# Hangman Game

Python console app hangman game based on the [code](https://github.com/markpatterson27/hangman-game) by [Mark Patterson](https://github.com/markpatterson27)

## Install dependencies and run

1. `pip install poetry`
2. `poetry install`
3. `poetry run python app/hangman.py`

# Lab "Test Coverage" Assignment

### Important instructions
1. do not move/delete the source files from the folders
1. submission: _commit_ and _push_ your changes to the current project to GitHub
1. do not edit _autograding_ or _classroom_ files
> :warning: **Note:** the autograding is simplified on purpose, it will be overwritten after the submission deadline with additional tests and quiz grading

> :warning: **Note:** `app/hangman.py` should not be changed, anyways it will be overwritten in the post processing for the final autograding

> :warning: **Note:** `tests/test_hangman.py` All your tests should be in this file

> :warning: **Note:** `.github/workflows/main.yaml` Your CI pipeline should be in this file

> :warning: **Note:** For the coverage threashold, use the command line only in the pipeline.

## Basis path testing (1pt)

* Calculate the minimum number of the basis path test cases needed for the 'hangman.py::hangman'

* Add the number here between the brackets.

> _Your answer. For example (5):_
>
> **Q1** (4)

## Create test cases (3pt)

* Create test cases with the minimum *85% of combined coverage* (lines and branch coverage) for the whole `hangman.py`
* Place your tests under the `tests/test_hangman.py` folder

> :warning: **Note:** the `hangman.py` should not be modified. It will be overwriten for in the final autograding stage after the submission deadline.

## Calculate coverage (1pt)

* What is the line coverage of your test suite for the `hangman.py`?
> _Your answer in %. For example (86):_
>
> **Q2** (89)

* What is the current branch coverage of your test suite for the `hangman.py`?
> _Your answer in %. For example (86):_
>
> **Q3** (90)


## Add CI (1pt)
* Add `main.yaml` that runs your test suite from `tests/` and has the minimum coverage criteria for the whole `hangman.py` of **85%** for the **combined** coverage (**total** coverage including lines + branches)

> :warning: **Note:** For the coverage threashold, use the command line only in the pipeline. Do not use config files. 

# Hints
* Check the [basis path tutorial](https://www.tutorialspoint.com/path-testing-and-basis-path-testing-with-example)
* Check the [python testing tutorial](https://testdriven.io/blog/testing-python/)


## Spoilers
* you may need to recall the lab on metrics to get the answer to _Q1_
* you may need _pytest-cov_ module installed
* you may need to generate and check _coverage.json_ to get the raw data and calculate exact numbers for the coverage