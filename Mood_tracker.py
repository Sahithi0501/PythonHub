import random
import os

# Mood to Activity mapping:
mood_activities = {
    "happy": ["Listen to music", "Go for a walk", "Watch your favourite movie"],
    "sad": ["Call your best friend", "Read a book", "Write your feelings in a diary"],
    "stressed": ["Take deep breaths", "Do meditation", "Play your favourite game"],
    "bored": ["Learn Python", "Cook your favourite food", "Play a game"]
}
# This is the File to  store past moods :
history_file = "mood_history.txt"

# It Asks the  user for their name:
name = input("Enter your Name:")
# It Asks the user for their mood:
mood = input(f"How are you feeling today, Dear {name}? (Happy, Sad, Stressed, Bored):- ").lower()#it will convert into lower case

# Suggest an activity:
if mood in mood_activities:
    suggestion = random.choice(mood_activities[mood])
    print(f"The Suggested activity for you is: {suggestion}")

    # Saves mood to the history:
    with open(history_file, "a") as f:
        f.write(mood + "\n")

    # Shows the  mood history:
    print("\n Previous Moods:")
    with open(history_file, "r") as f:
        past_moods = f.readlines()
        past_moods = [m.strip().title() for m in past_moods]  # Convert moods to Title Case
        print(", ".join(past_moods))

else:
    print(f"Sorry! Dear {name}, I don't have suggestions for that mood yet!\n"
          "BUT ALWAYS REMEMBER, YOU ARE AMAZING, AND BETTER DAYS ARE COMING. KEEP SMILING DEAR!")
