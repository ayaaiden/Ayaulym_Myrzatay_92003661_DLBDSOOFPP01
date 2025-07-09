from datetime import datetime, timedelta

class Habit:
    def __init__(self, name, frequency, creation_date=None, completions=None):
        self.name = name
        self.frequency = frequency  # "daily" or "weekly"
        self.created_at = creation_date if creation_date else datetime.now()

        if completions is None:
            self.completions = []
        else:
            self.completions = [
                datetime.fromisoformat(dt).date() if isinstance(dt, str) else dt
                for dt in completions
            ]

    def get_longest_streak(self):
        if not self.completions:
            return 0

        sorted_dates = sorted(self.completions)
        longest = 1
        current = 1
        gap = timedelta(days=1) if self.frequency == "daily" else timedelta(weeks=1)

        for i in range(1, len(sorted_dates)):
            if sorted_dates[i] - sorted_dates[i - 1] == gap:
                current += 1
                longest = max(longest, current)
            else:
                current = 1  # streak broken

        return longest

    def __str__(self):
        return f"{self.name} ({self.frequency})"


class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, habit):
        self.habits.append(habit)

    def list_habits(self):
        return self.habits

