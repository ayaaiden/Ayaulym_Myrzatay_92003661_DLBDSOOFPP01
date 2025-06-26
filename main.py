

from tracker import HabitTracker
from habit_tracker import Habit 

import json
import os

def load_habits_from_json(filepath):
    if not os.path.exists (filepath):
        print(" !!! NO HABIT DATA FILE FOUND !!!")
    return []
    with open(filepath, 'r') as file:
        return json.load(file)

def save_habits_to_json(filepath, habits):
    with open(filepath, 'w') as file:
        json.dump([habit.to_dict() for habit in habits], file, indent=4)

#Adding a new habit
def add_new_habit():
    name = input("Enter the habit name: ")
    frequency = input ("Enter the frequency(f.e., daily, weekly): ")
    return Habit(name=name, frequency=frequency, completions =[])

#Marking the habit as done
def mark_habit_done(habits):
    if not habits:
        print("No habit to mark as done. ")
        return
    print("Select the habit to mark down: ")
    for i, habit in enumerate(habits, 1 ):
        print(f"{i}. {habit.name}")
    try:
        choice = int(input("Enter the habit number: "))
        if 1<=choice <= len(habits):
            habits[choice -1].mark_complete()
            print(f"Marked '{habits[choice -1].name}' as done.")
        else: 
            print("Invalid choice!")
    except ValueError:
        print("Enter the valid number: ")

#filter the habits by the frequency 
def filter_habits_by_frequency(habits):
    freq = input ("Enter frequency to filter by (f.e., daily, weekly): ").lower()
    filtered = [habit for habit in habits if habit.frequency.lower() == freq.lower]
    if not filtered:
        print(f"No habits found with frequency: {freq}")
    else:
        for habit in filtered: 
            print(habit)

# The main loop   
def main():
    tracker = HabitTracker()

    #Example habits 
    #habit1 = Habit ("Exercise", "daily")
    #habit2 = Habit ("Read 10 pages of the book", "daily")
    
    #tracker.add_habit(habit1)
    #tracker.add_habit(habit2)

    #Replaced the manual call to Json
    filepath = "data/habits.json"
    data = load_habits_from_json(filepath)
    #json_data = load_habits_from_json("../../data/habits.json")

    for item in data:
        habit = Habit(item["name"], item ["frequency"])
        habit.completions = item.get ("completions",[])
        tracker.add_habit(habit)

    while True:
        print("\n Habit Tracker Menu")
        print("1. View all Habits")
        print("2. Add a New Habit")
        print("3. Mark Habit as Done")
        print("4. Filter Habits by frequency")
        print("5. Exit")

        choice = input (" Enter the choice from 1 to 5:")

        if choice == '1':
            if not tracker.habits:
                print("No habits found.")
            else:
                for habit in tracker.habits:
                    print(habit)
        
        elif choice == '2':
            new_habit = add_new_habit()
            tracker.add_habit(new_habit)
            save_habits_to_json(filepath, tracker.habits)
        
        elif choice == '3':
            mark_habit_done(tracker.habits)
            save_habits_to_json(filepath, tracker.habits)

        elif choice == '4':
            filter_habits_by_frequency(tracker.habits)

        elif choice == '5': 
            print("Goodbye!")
            break

        else:
            print("!!! Invalid choice. Please enter from 1 to 5 !!!")
    print("🎯 Current Habits: ")
    #tracker.list_habits()

    #tracker.list_habit_names()
    
    #print("\n🔎 Filtering for daily habits:")
    #tracker.filter_by_frequency("daily")

    #print("\n🔔 Mark 'Exercise' done: ")
    #tracker.complete_habit("Exercise")

    #print("\n📋 Update Habits: ")
    #tracker.list_habits()

#def load_habits_from_json(filepath):
   # if not os.path.exists(filepath):
   #    print("ERROR: No habit data file is found!")

    #with open(filepath, 'r') as file:
     #   data = json.load(file)
      #  return data

if __name__ == "__main__":
    main()