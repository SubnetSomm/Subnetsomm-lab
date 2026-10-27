"""
basketball_game.py
@author: Franco Pisano
Date Created: April 14, 2026
This program simulates a one-on-one basketball game using nested for loops,
if structures, and Python's random.randint() function to generate points
"""


import random

def main():
    counter = 0
    player1 = input_player_name('Player 1')
    player2 = input_player_name('Player 2')
    player1_score = 0
    player2_score = 0

    # for loop to count the quarters from 1 to 4
    for i in range(4): # same as for i in range(0, 4, 1):
        print("--------------------------- Quarter ", (i + 1),
            "-------------------------")
        print(f'{"":8s} {player1:<31s} {player2:<30s}')

        print(f'{"Shot #":8s} {"Shot":15s} {"Score":15s} {"Shot":15s} {"Score":14s}')
        # We have 12 minutes in each quarter and 60 seconds in a minute thus 720
        # seconds. We want each player to take a shot within a 30 second interval
        for j in range(720, 0, -30):
            player1_shot = random.randint(0, 3)
            player2_shot = random.randint(0, 3)
            counter = counter + 1
            # determine the shotmade for player1
            player1_shotmade = determine_player_shotmade(player1_shot)
            # determine the shotmade for player2
            player2_shotmade = determine_player_shotmade(player2_shot)

            player1_score = calculate_score(player1_score, player1_shot)
            player2_score = calculate_score(player2_score, player2_shot)

            print(
                f'{counter:<8d} '
                f'{player1_shotmade:<15s} '
                f'{player1_score:<15d} '
                f'{player2_shotmade:<15s} '
                f'{player2_score:<15d}'
            )

    display_winner(player1_score, player2_score, player1, player2)


# input_player_name gets the player name and returns it
def input_player_name(player):
    print('Please enter the ', player, ' name:')
    player_name = input()
    return player_name

# determine_player_shotmade determines Air Ball, Free Throw, Two Pointer, or
# Three Pointer based on the player_shot that was randomly generated
def determine_player_shotmade(player_shot):
    if player_shot == 0:
        player_shotmade = "Air Ball"
    elif player_shot == 1:
        player_shotmade = "Free Throw"
    elif player_shot == 2:
        player_shotmade = "Two Pointer"
    else:
        player_shotmade = "Three Pointer"

    return player_shotmade

# calculate_score calculates the score for each player
def calculate_score(player_score, player_shot):
    player_score = player_score + player_shot
    return player_score


# display_winner determines the winner based on the score
def display_winner(player1_score, player2_score, player1, player2):
    if player1_score > player2_score:
        print(player1, " bringing a W!")
    elif player2_score > player1_score:
        print(player2, " bringing a W!")
    else:
        print("Tie Game..Go Home..See ya' later!")

# call the main function
if __name__ == '__main__':
    main()
