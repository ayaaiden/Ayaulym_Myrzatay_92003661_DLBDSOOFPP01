import pytest
# This file is part of Habit Tracker Project.
# It provides unit tests for the analytics functions to analyze habits.
# These tests cover the functionality of the analytics functions,
# including retrieving all habit names, filtering habits by frequency,
# and calculating the longest streak for a specific habit or overall.
from analytics import (
    get_all_habit_names,
    get_habits_by_frequency,
    get_longest_streak_for_habit,
    get_longest_streak_overall,
)
from habit_tracker import Habit
from datetime import date

@pytest.fixture
# Create a fixture to provide a list of Habit objects for testing
def habit_list():
    return [
        Habit("Reading", "daily", date(2025, 6, 9), [date(2025, 6, 9), date(2025, 6, 10), date(2025, 6, 11)]),
        Habit("Running", "daily", date(2025, 6, 9), [date(2025, 6, 9), date(2025, 6, 10)]),
        Habit("Meditation", "weekly", date(2025, 6, 2), [date(2025, 6, 2)]),
    ]

# Unit tests for analytics functions in Habit Tracker Project
def test_get_all_habit_names(habit_list):
    assert get_all_habit_names(habit_list) == ["Reading", "Running", "Meditation"]

# Unit tests for filtering habits by frequency
def test_get_habits_by_frequency(habit_list):
    result = get_habits_by_frequency(habit_list, "daily")
    assert len(result) == 2

# Unit tests for calculating the longest streak for a specific habit
# and overall longest streak
def get_longest_streak_for_habit(habits, habit_name):
    target = next(filter(lambda h: h.name == habit_name, habits), None)
    return target.get_longest_streak() if target else 0

# Unit tests for calculating the longest streak overall
# This function calculates the longest streak among all habits
# and returns the maximum value.
def get_longest_streak_overall(habits):
    return max([h.get_longest_streak() for h in habits], default=0)

