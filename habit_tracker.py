from datetime import timedelta, datetime

class Habit: 
    
    def __init__(self, name, frequency, creation_date=None, completions=None):
        self.name = name
        self.frequency = frequency  # e.g., "daily" or "weekly"
        self.creation_date = creation_date if creation_date else datetime.now().date()
        self.completions = [
            datetime.fromisoformat(dt).date() if isinstance(dt, str) else dt
            for dt in (completions or [])
        ]

    def get_longest_streak(self):
        """Calculates the longest streak of completions for a habit"""
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
                current = 1  # Streak broken

        return longest
    
    def mark_complete (self): 
        self.completions.append(datetime.now())

    def get_last_completion (self):
        if not self.completions:
            return None
        return self.completions[-1]
    

    def __str__ (self):
        return f"Habit(name = {self.name}, frequency = {self.frequency}, completed ={len(self.completions)} times)"
    
    #Make sure that the habits are saved 

    def to_dict(self):
        return {
            "name": self.name,
            "frequency": self.frequency,
            "completions": [dt.isoformat() for dt in self.completions]
        }