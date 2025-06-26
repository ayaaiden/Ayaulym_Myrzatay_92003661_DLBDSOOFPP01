from habit_tracker import Habit

class HabitTracker:
    def __init__(self):
        self.habits = []
    
    def add_habit (self, habit):
        self.habits.append(habit)

    def list_habits (self):
        for i, habit in enumerate (self.habits,1):
            print (f"{i}.{habit}")
    
    def find_habit (self, name):
        for habit in self.habits:
            if habit.name.lower() == name.lower():
                return habit
            return None
        
    def complete_habit (self, name):
        habit = self.find_habit(name)
        if habit:
            habit.mark_complete()
            print(f"✅ Marked '{name}' as complete!")
        else: 
            print(f"❌ Habit '{name}' not found.")

    # Begining of the method to filter habits by the frequency 
    
    def filter_by_frequence (self, frequency) :
        filtered = list(filter(lambda h: h.frequency == frequency, self.habits))
        return filtered 
    
    #End of the method to filter habits by the frequency 

    # Begining of the print the frequency 

    def filter_by_frequency(self, frequency):
        filtered = list(filter(lambda h: h.frequency == frequency, self.habits))
        print(f"\n Habits with frequeny '{frequency}':")
        for i, habit in enumerate (filtered, 1):
            print(f"{i}. {habit}")
        return filtered
    
    #End of print the frequency 

    # Begining of the map() method to list only habit names 
    def list_habit_names(self):
        names = list (map(lambda h: h.name, self.habits))
        print ("\n Habit Names:")
        for name in names:
            print("-", name)
    
    #End of the map() method to list only habit names 
