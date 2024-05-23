# Task 1: Your Mood Today
# Write a program that prints off different moods for each day of the week. Create a list of moods 
# such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through the days 
# of the week and for each day, randomly select a mood from the list and print it. Ensure that your 
# program includes the use of the random module to select the mood.



import random




days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["Happy", "Sad", "Energetic", "Mad", "Calm"]

mood = {}

for day in days:
    random_mood = random.choice(moods)
    mood [day] = random_mood


for day, mood in mood.items():
    print(day, mood)

