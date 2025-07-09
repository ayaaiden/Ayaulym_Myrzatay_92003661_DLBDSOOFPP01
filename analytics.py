# This file is part of Habit Tracker Project.
# It provides analytics functions to analyze habits.
from habit_tracker import Habit

# Analytics functions for Habit Tracker Project
def get_all_habit_names(habits):
    """Returns a list of all habit names"""
    return list(map(lambda h: h.name, habits))

def get_habits_by_frequency(habits, frequency):
    """Returns a list of all habit frequencies"""
    return list(filter(lambda h: h.frequency == frequency, habits))

def get_longest_streak_for_habit(habits, habit_name):
    """Returns the longest streak for a habit with given name"""
    target = next(filter(lambda h: h.name == habit_name, habits), None)
    return target.get_longest_streak_for_habit() if target else 0

def get_longest_streak_overall(habits):
    """Returns the longest streak among all habits"""
    return max([h.get_longest_streak_for_habit() for h in habits], default=0)
