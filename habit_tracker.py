from datetime import datetime 

class Habit: 
    
    def __init__ (self, name, frequency, completions = None):
        self.name = name
        self.frequency = frequency # example., "daily", "weekly"
        self.created_at = datetime.now()
        self.completions = [datetime.fromisoformat(dt) if isinstance(dt, str) else dt for dt in (completions or [])]
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