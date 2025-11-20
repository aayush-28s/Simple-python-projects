import random
from getpass import getpass
import sys

emojis = {'s':'✂️','p':'📃','r':'🪨'}
choices = ['s','p','r']

user_win = 0
computer_win = 0
tie = 0

def get_user_choice(player_name,secret=False):
    while True:
        if secret:
            print(f"{player_name}, enter your move (s/p/r): ", end='',flush=True)
            user_choice = getpass("").lower()
        else:
            user_choice = input(f"{player_name} scissors,paper or rock ? (s/p/r):").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice")

def display_choice(player1,choice1,player2,choice2):
    print(f"{player1} chose: {emojis[choice1]}")
    print(f"{player2} chose: {emojis[choice2]}")

def determine_winner(player1,choice1,player2,choice2):
    global tie, user_win, computer_win
    if choice1 == choice2:
        print("It's a tie!")
        tie += 1
    elif (choice1 == 's' and choice2 == 'p') or\
            (choice1 == 'p' and choice2 == 'r') or \
            (choice1 == 'r' and choice2 == 's'):
        print(f"{player1} won!")
        if player2 == "computer":
            user_win += 1
    else:
        print(f"{player2} won")
        if player2 == "computer":
            computer_win += 1

def play_singleplayer():
    while True:
        user_choice = get_user_choice("you")
        computer_choice = random.choice(choices)

        display_choice("you",user_choice,"computer", computer_choice)
        determine_winner("you",user_choice,"computer", computer_choice)

        a_continue = input("Continue? (y/n):").lower()
        if a_continue == 'n':
            break

def play_multiplayer():
    while True:
        player1 = "player1"
        player2 = "player2"
        print("\n" + "-"*10)
        choice1 = get_user_choice("player1", secret=True)
        choice2 = get_user_choice("player2", secret=True)

        display_choice(player1,choice1,player2,choice2)
        determine_winner(player1,choice1,player2,choice2)

        a_continue = input("Continue? (y/n):").lower()
        if a_continue == 'n':
            break

while True:
    print("Welcome to the Scissors,Papers and Rock game")
    mode = input("Do you want to play with (1) Computer (2) Another player or press any key except 1,2 to exit the game?(1/2):")

    if mode == "1":
        play_singleplayer()
        print("Game Over")
        print(f"Total you won: {user_win}")
        print(f"Computer won: {computer_win}")
        print(f'total tie: {tie}')
    elif mode == "2":
        play_multiplayer()
        print("Game Over")
    else :
        print("Thank you for your time and have a nice day!")
        break




