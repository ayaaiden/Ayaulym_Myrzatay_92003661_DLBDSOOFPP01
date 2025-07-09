import pytest
from datetime import date
from habit_tracker import Habit
# Test cases for Habit Tracker Project
# These tests cover the functionality of the Habit class
# and its methods, including creation, streak calculation, and frequency handling.

# Test case for creating a habit with a name, frequency, and start date
def test_create_habit():
    habit = Habit("Exercise", "daily", date(2025, 6, 1))
    assert habit.name == "Exercise"
    assert habit.frequency == "daily"
    assert habit.completions == []

# Test case for creating a habit with a specific start date
def test_streak_daily():
    completions = [
        date(2025, 6, 1),
        date(2025, 6, 2),
        date(2025, 6, 3),
        date(2025, 6, 5)
    ]
    habit = Habit("Exercise", "daily", date(2025, 6, 1), completions)
    assert habit.get_longest_streak() == 3

# Test case for creating a habit with weekly frequency
def test_streak_weekly():
    completions = [
        date(2025, 6, 1),
        date(2025, 6, 8),
        date(2025, 6, 15),
        date(2025, 6, 29)  # skipped one week
    ]
    habit = Habit("Journal", "weekly", date(2025, 6, 1), completions)
    assert habit.get_longest_streak() == 3

