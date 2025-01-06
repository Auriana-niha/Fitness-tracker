import datetime

class FitnessTracker:
    def __init__(self):
        self.activity_log = []

    def log_activity(self, activity, duration, calories_per_minute):
        """Logs an activity with duration and calories burned per minute."""
        calories_burned = duration * calories_per_minute
        activity_data = {
            'date': datetime.datetime.now().strftime("%Y-%m-%d"),
            'activity': activity,
            'duration': duration,  # in minutes
            'calories_burned': calories_burned
        }
        self.activity_log.append(activity_data)
        print(f"Activity logged: {activity}, Duration: {duration} min, Calories burned: {calories_burned:.2f} kcal.")

    def display_progress(self):
        """Displays the total calories burned over time and the log of activities."""
        if not self.activity_log:
            print("No activities logged yet.")
            return
        
        total_calories = sum(activity['calories_burned'] for activity in self.activity_log)
        print(f"\nTotal Calories Burned: {total_calories:.2f} kcal\n")
        print("Activity Log:")
        for entry in self.activity_log:
            print(f"{entry['date']} - {entry['activity']} for {entry['duration']} min, Calories burned: {entry['calories_burned']:.2f} kcal")

    def clear_log(self):
        """Clear the activity log."""
        self.activity_log.clear()
        print("Activity log cleared.")

def __main__():
    tracker = FitnessTracker()
    
    while True:
        print("\nFitness Tracker Menu:")
        print("1. Log Activity")
        print("2. Display Progress")
        print("3. Clear Log")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            activity = input("Enter the activity (e.g., Walking, Running, Cycling): ")
            duration = float(input("Enter the duration in minutes: "))
            calories_per_minute = float(input("Enter calories burned per minute for this activity: "))
            tracker.log_activity(activity, duration, calories_per_minute)
        elif choice == '2':
            tracker.display_progress()
        elif choice == '3':
            tracker.clear_log()
        elif choice == '4':
            print("Exiting the Fitness Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    __main__()