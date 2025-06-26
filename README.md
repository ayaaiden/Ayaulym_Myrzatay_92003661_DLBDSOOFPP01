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

<img width="588" alt="Screenshot 2025-06-26 at 20 50 07" src="https://github.com/user-attachments/assets/fdff1ead-1f64-4fd2-9413-275185978494" />

## How to Run the Application

1. Make sure that the Python 3.10+ is installed.
2. Run the following code in the terminal:
`cd habit_tracker_project/src`
`python3 main.py`
3. After running the code from the step 2 in the terminal: the following output:
<img width="244" alt="Screenshot 2025-06-26 at 04 35 53" src="https://github.com/user-attachments/assets/783176fd-e94d-46f5-ad11-0003890360c3" />

## Saving & Loading

1. All data is saved in `data/habits.json`
2. Each habit include:
   2.1. `name`
   2.2. `frequency`
   2.3. `completions`

Example:


<img width="335" alt="Screenshot 2025-06-26 at 04 43 06" src="https://github.com/user-attachments/assets/528ec4d1-e1be-4e89-9ad3-2514d66512c6" />

## How to Run Tests

From the terminal and src directory run:
`python3 -m unittest discover -s tests `
This line of code will run unit tests that are located in `tests/test_main.py `
