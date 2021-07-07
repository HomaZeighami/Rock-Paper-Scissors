# Python Random Module.
import random

while True:
    # The player's chosen action.
    player_action = input("Enter a choice (Rock, Paper, Scissors): ")

    # The game chooses a random action among the possible actions.
    possible_actions = ["rock", "paper", "scissors"]
    game_action = random.choice(possible_actions)

    print(f"\nYou chose {player_action}, I chose {game_action}.\n")

    # If the player's action is equal to the game's action, then the game is a tie.
    if player_action == game_action:
        print(f"Both players selected {player_action}. It's a tie!")

    # If the player's action is rock, and the game's action is scissors, they win the game.
    elif player_action == "rock":
        if game_action == "scissors":
            print("Rock smashes scissors! You win!")
        # If the player's action is rock, and the game's action is paper, they lose the game.
        else:
            print("Paper covers rock! You lose.")
    # If the player's action is paper, and the game's action is rock, they win the game.
    elif player_action == "paper":
        if game_action == "rock":
            print("Paper covers rock! You win!")
        # If the player's action is paper, and the game's action is scissors, they lose the game.
        else:
            print("Scissors cuts paper! You lose.")
    # If the player's action is scissors, and the game's action is paper, they win the game.
    elif player_action == "scissors":
        if game_action == "paper":
            print("Scissors cuts paper! You win!")
        # If the player's action is scissors, and the game's action is rock, they lose the game.
        else:
            print("Rock smashes scissors! You lose.")

    # If the player doesn't want to play again, the loop stops.
    play_again = input("Do you want to play again? (Yes/No): ")
    if play_again.lower().capitalize() != "Yes":
        break
