"""
Random Workout Generator
Task Objective
In this task, students will create a program that generates a random workout routine.
The workout routine will include a warm-up exercise, a main workout exercise, and a cool-down exercise, each chosen randomly from predefined lists.
Instructions
Import the random module.
Define three separate lists of exercises:
Warm-up exercises
Main workout exercises
Cool-down exercises
Randomly select one exercise from each list.
Print the selected warm-up, main workout, and cool-down exercises as a full workout routine.

"""

import random 


# Define lists of exercises
warm_up_exercises = ["Jumping jacks", "High knees", "Arm circles", "Butt kicks", "Lunges"]
main_workout_exercises = ["Push-ups", "Squats", "Burpees", "Plank", "Mountain climbers"]
cool_down_exercises = ["Stretching", "Yoga poses", "Slow jogging", "Deep breathing", "Hamstring stretch"]


# Randomly select one exercise from each list
warmUp = random.choice(warm_up_exercises)
# print(destination)
mainWorkout = random.choice(main_workout_exercises)
coolDown = random.choice(cool_down_exercises)

# Print the full workout routine

print("Your Random Workout Routine:")
print(f"Warm-up: {warmUp}")
print(f"Main Workout: {mainWorkout}")
print(f"Cool-down: {coolDown}")