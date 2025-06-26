import unittest
from habit_tracker import Habit
from tracker import HabitTracker

class TestHabitTracker(unittest.TestCase):
    def test_create_habit(self):
        habit = Habit("Exercise", "Daily")
        self.assertEqual(habit.name, "Exercise")
        self.assertEqual(habit.frequency, "Daily")
        self.assertEqual(len(habit.completions), 0)

    def test_mark_complete(self):
        habit = Habit("Exercise", "Daily")
        habit.mark_complete()
        self.assertEqual(len(habit.completions), 1)

    def test_add_and_find_habit(self):
        tracker = HabitTracker()
        habit = Habit ("Exercise", "Daily")
        tracker.add_habit(habit)

        found = tracker.find_habit("Exercise")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Exercise")