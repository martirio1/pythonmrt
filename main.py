import random

choices = ['rock', 'paper', 'scissors']

player_choice = input("Enter your choice (rock/paper/scissors): ").lower()

while player_choice not in choices:
    print("Invalid choice. Please try again.")
    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()

computer_choice = random.choice(choices)
print("Computer chooses:", computer_choice)

if player_choice == computer_choice:
    print("It's a tie!")
elif (
    (player_choice == 'rock' and computer_choice == 'scissors') or
    (player_choice == 'paper' and computer_choice == 'rock') or
    (player_choice == 'scissors' and computer_choice == 'paper')
):
    print("Congratulations! You win!")
else:
    print("Sorry! You lose.")

