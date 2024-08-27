# Premodule Assignment

## Installation

1. Go to the venv you want to use.
2. Install the application using <br> 
`pip install .` <br>
The program will be installed with name `cleaner`
3. If other dependencies are needed, run the following<br>
`pip install -r requirements.txt`

## Running Instruction

Before running, please put the target csv file in `./data/raw folder`.

This tool has following functions with example command line input:
1. Print general information about the raw csv data to the terminal. <br>
example: `cleaner data/raw/<filename> --info`

2. Print first n rows in the raw csv data to the terminal.<br>
example: `cleaner data/raw/<filename> --view 5`

3. (Core function) Do a automatic cleaning to remove NAN data (first drop columns with NAN then rows)and store the modified data in `./data/processed/cleaned_file.csv`.<br>
example: `cleaner data/raw/<filename> --clean`


(you can add multiple flags at the same time)

## Reference and Requirement
Following is assignment info copied from https://canvas.duke.edu/courses/40118/assignments/129918?module_item_id=263474

### Instructions
Create a Python script that does some specific task (i.e. process a csv file in some way), write unit tests for it, and package it into a command line tool.

### Submission
Submit a link to a GitHub repository. Ensure the README contains all necessary instructions for running your tool. If we cannot run it, we cannot grade it. 

### Rubric
- Code is a tool that runs in the command line/terminal
- Code is clean and well organized
- Code is documented with docstrings and comments
- Code is free of commented out code (ie debug print statements)
- Appropriate unit tests are included
- Branching and PRs were done appropriately in the GitHub repository
- Requirements are included in the text of the PR and are correct and versioned
- The README includes necessary instructions for running tool
- The code runs as documented