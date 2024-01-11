import random
from Day12_NumberArt import *
EASY_GAME = 10
HARD_GAME = 5


# Create a function to Compare the guess to the target number. Return Too high or Too Low or Got It
def compare(check, answer, lives_remaining):
	if check == answer:
		print(win)
		print(f"{answer} was the correct number!")
		lives_remaining = 100
		return lives_remaining
	# Track the lives available to the player. Subtract 1 when a guess is wrong. Easy = 10, Hard = 5
	elif check > answer:
		print(too_high)
		return lives_remaining - 1
	elif check < answer:
		print(too_low)
		return lives_remaining - 1


# Create an input for easy vs hard and the first guess
def set_difficulty():
	difficulty = input("Choose your difficulty. Type 'easy' or 'hard'. ").lower()
	if difficulty == 'easy':
		return EASY_GAME
	else:
		return HARD_GAME


def game():
	print(logo)
	print("I'm thinking of a number between 1 and 100...")
	# Create a variable to store the target number and generate it randomly
	target = random.randint(1, 100)
	lives = set_difficulty()
	# Wrap Guessing and checking in a loop to repeat until the number is guessed
	keep_playing = True
	while keep_playing:
		guess = int(input("Guess a number: "))
		lives = compare(guess, target, lives)
		if lives == 100:
			keep_playing = False
		elif lives == 0:
			print(f"	You've run out of lives. The correct number was {target}.")
			print(lose)
			keep_playing = False
		else:
			print(f"	You have {lives} lives remaining.")


game()

