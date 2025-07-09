from tracker import Habit, HabitTracker
import json
import os
from datetime import datetime

def load_habits_from_json(filepath):
    print(f"Checking file at: {filepath}")  
    if not os.path.exists(filepath):
        print(" !!! NO HABIT DATA FILE FOUND !!!")
        return []
    with open(filepath, 'r') as file:
        return json.load(file)

def save_habits_to_json(filepath, habits):
    with open(filepath, 'w') as file:
        json.dump([habit.to_dict() for habit in habits], file, indent=4)

def add_new_habit():
    name = input("Enter the habit name: ")
    frequency = input("Enter the frequency (e.g., daily, weekly): ")
    return Habit(name=name, frequency=frequency, completions=[])

def mark_habit_done(habits):
    if not habits:
        print("No habit to mark as done.")
        return
    print("Select the habit to mark down:")
    for i, habit in enumerate(habits, 1):
        print(f"{i}. {habit.name}")
    try:
        choice = int(input("Enter the habit number: "))
        if 1 <= choice <= len(habits):
            habits[choice - 1].mark_complete()
            print(f"Marked '{habits[choice - 1].name}' as done.")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Enter a valid number.")

def filter_habits_by_frequency(habits):
    freq = input("Enter frequency to filter by (daily, weekly): ").lower()
    filtered = [habit for habit in habits if habit.frequency.lower() == freq]
    if not filtered:
        print(f"No habits found with frequency: {freq}")
    else:
        for habit in filtered:
            print(habit)

def main():
    tracker = HabitTracker()
    filepath = "../data/habits.json"
    data = load_habits_from_json(filepath)

    for item in data:
        habit = Habit(
            name=item["name"],
            frequency=item["frequency"],
            creation_date=item.get("creation_date"),
            completions=item.get("completions", [])
        )
        tracker.add_habit(habit)

    while True:
        print("\n🎯 Current Habits:")
        print("\n  Habit Tracker Menu")
        print("  1. View all Habits")
        print("  2. Add a New Habit")
        print("  3. Mark Habit as Done")
        print("  4. Filter Habits by frequency")
        print("  5. Exit")

        choice = input("  Enter the choice from 1 to 5: ")

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
            print("Invalid choice. Please enter from 1 to 5.")

if __name__ == "__main__":
    main()
