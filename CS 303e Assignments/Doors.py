# File: Deal.py

# Description:Simulation of let's make a deal. Finds the probability that
#             a contestent would win by swapping doors, rather than sticking
#             with the one that 

# Student Name:

# Student UT EID:

# Course Name: CS 303E

# Unique Number: 

# Date Created:

# Date Last Modified:

import random

#determines which door the host reveals
def other_door(door_prize, door_guess):

    door_other = 1
    while door_other == door_guess or door_other == door_prize:
        door_other += 1

    return(door_other)

#function that runs the simulation of making deals and swapping doors
def swap_door(games):

    current_game = 0
    won_swapping = 0

    while current_game < games:
#generates door for prize and what contestent chooses 
        door_prize = random.randint(1,3)
        door_guess = random.randint(1,3)
        current_door = 1

        revealed_door = other_door(door_prize, door_guess)
#considering whether or not the game is won by swapping 
        while current_door == door_guess or current_door == revealed_door:
            current_door += 1
        if current_door == door_prize:
            won_swapping += 1
        current_game += 1
        print(" "*3,door_prize," "*8,door_guess," "*8,revealed_door," "*8, current_door)
    
    print()
    probability = won_swapping/games
    print("Probability of winning by swapping = ",format(probability,".2f"))
    print("Probability of winning by not swapping = ", format(1 - probability,".2f"))
    
def main():

    games = int(input("Enter number of times you want to play: "))
    print()
    print("  Prize      Guess       View    New Guess")
# calls function that finds probability of winning and prints doors information
    swap_door(games)

main()

        
