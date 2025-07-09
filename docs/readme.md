# Habit Tracker CLI Application

## Description

### The habit tracking application is a command line application that allows users to create, manage, and monitor personal habits with flexible frequency (f.e., daily, weekly). The application will support:

* Adding new habits
* Marking habits as complete
* Filtering by frequency
* Saving and loading all data via JSON
* Persistent data across sessions
* Basic unit testing with unittest

## Features

* ✅ Add and list habits
* ✅ Mark a habit as completed
* ✅ Track how many times each habit was completed
* ✅ Save/load data from `data/habits.json`
* ✅ Filtering habits by the frequency
* ✅ Robust CLI loop with error handling
* ✅ Unit tests for the core functionality

## The Project Strucutre

§ habit\_tracker\_project/
\|
\|\-\- data/
\|        \|\- habits\.json              \# JSON storage of user habits
\|
\|\-\- src/
\|        \|\- main\.py                  \# Main CLI interface
\|        \|\- habit\_tracker\.py       \# Habit class definition
\|        \|\- tracker\.py                 \# HabitTracker class
\|
\|\- tests/
\|        \|\- test\_main\.py                 \# Unit Tests

## How to Run the Application

1. Make sure that the Python 3.10+ is installed.
2. Run the following code in the terminal:
`cd habit_tracker_project/src`
`python3 main.py`
3. After running the code from the step 2 in the terminal: the following output:

![screenshot_of_menu.png](.media/img_1.png)

## Saving & Loading

1. All data is saved in `data/habits.json`
2. Each habit include:
2.1. `name`
2.2. `frequency`
2.3. `completions`

Example:
![json_example.png](.media/img_11.png)

## How to Run Tests

From the terminal and src directory run:
`python3 -m unittest discover -s tests `
This line of code will run unit tests that are located in `tests/test_main.py `

## What I have learned & Practiced 
- Object - Oriented Programming (OOP)
- File I/O and JSON serialization 
- Date/time handling with datetime 
- Exception handling 
- Unit testing with Python's unittest 
- CLI design and user input validation 
