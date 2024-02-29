import math

# Deliverable 1: Prompts the user for their name
name = input("Welcome to GC mini golf! What is your name? ")

# Deliverable 2: Prompts the user if they would like to play 3 or 6 holes of golf
number_holes = int(input("Hi, " + name + "! Would you like to play 3 or 6 holes today? "))

# Math for scoring
course_par = number_holes * 3
total_score = 0

'''Deliverable 3: Prompts the user three or six times (depending on their answer for #2) for the number of putts for 
each hole'''
for hole in range(1, number_holes + 1):
    x = number_holes
    while x <= number_holes:
        hole_stroke = int(input(f"How many putts for hole {hole}? (par: 3) "))
        x += 1
    total_score += hole_stroke

# More math for final scoring
end_score = total_score - course_par

# Deliverable 8-10:
if end_score > 0:
    print(f"Nice Try, {name}... Your total score was: +{end_score}.")
elif end_score < 0:
    print(f"Great job, {name}! Your total score was: {end_score}.")
else:
    print(f"Good game, {name}. Your total score was: 0.")