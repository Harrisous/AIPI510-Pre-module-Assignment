# Premodule Assignment

## Installation

Go to proper env.
run `pip install -r requirements.txt`

## Running Instruction

Before running, please put the original csv file is placed in ./data/raw folder.

This tool has following functions with example command line input:
1. Print general information about the raw csv data to the terminal. <br>
`python src/main.py data/raw/<filename> --info`

2. Print first n rows in the raw csv data to the terminal.<br>
`python src/main.py data/raw/<filename> --view 5`

3. Do a automatic cleaning to remove NAN data (first drop columns with NAN then rows)and store the modified data in ./data/processed.<br>
`python src/main.py data/raw/<filename> --clean`

Run the main script: python src/main.py

## Reference and Requirement
Following is assignment info copied from https://canvas.duke.edu/courses/40118/assignments/129918?module_item_id=263474

### Instructions
Create a Python script that does some specific task (i.e. process a csv file in some way), write unit tests for it, and package it into a command line tool.

### Submission
Submit a link to a GitHub repository. Ensure the README contains all necessary instructions for running your tool. If we cannot run it, we cannot grade it. 

### Rubric
v Code is a tool that runs in the command line/terminal
v Code is clean and well organized
v Code is documented with docstrings and comments
v Code is free of commented out code (ie debug print statements)
x Appropriate unit tests are included
x Branching and PRs were done appropriately in the GitHub repository
x Requirements are included in the text of the PR and are correct and versioned
v The README includes necessary instructions for running tool
v The code runs as documented