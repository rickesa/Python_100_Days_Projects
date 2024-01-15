from Higher_Lower_Art import *
from Higher_Lower_Data import data
import random
game_dict = {'previous_points': 0, 'option': random.randint(0, len(data) - 1)}


def generate_option():
	number = random.randint(0, len(data) - 1)
	# print(f"Followers = {data[number]['follower_count']}")  # Debug
	return number


def compare(a, b):
	"""checks if option a has a larger follower count than option b"""
	print(f"{data[a]['name']}: {data[a]['follower_count']}")
	print(f"{data[b]['name']}: {data[b]['follower_count']}")
	if data[a]['follower_count'] > data[b]['follower_count']:
		print(f"{data[a]['name']} has more followers than {data[b]['name']}")
		return True
	else:
		print(f"{data[b]['name']} has more followers than {data[a]['name']}")
		return False


def game(points, option_a):
	transfer_list = {'points': points, 'carry_option': 0}  # This will carry the values out to be reused
	print(vs)
	option_b = generate_option()
	while option_a == option_b:  # Prevent duplicate options from being compared
		option_b = generate_option()
	print(f"Against B: {data[option_b]['name']}, a {data[option_b]['description']} from {data[option_b]['country']} ")

	# Take the guess of the player and compare their guess to the correct answer
	guess = input("Who has more IG followers? type 'a' or 'b'.\n").lower()
	if guess == "a":
		bigger = True
	else:
		bigger = False

	if compare(option_a, option_b) == bigger:
		print("You are correct")
		transfer_list['points'] += 1
		transfer_list['carry_option'] = option_b
		return transfer_list  # transfer_list now carries the point total and the new option A for the next round
	else:
		print("You are incorrect")
		return transfer_list


play_again = True
while play_again:
	previous_points = game_dict['previous_points']

	print(logo)
	print(f"Current points: {previous_points}")
	option = game_dict['option']
	print(f"Compare A: {data[option]['name']}, a {data[option]['description']} from {data[option]['country']}")
	# print(f"Followers = {data[option]['follower_count']}")  # Debug

	result = game(previous_points, option)

	if result['points'] == previous_points:
		print(f"You've ended with {previous_points} points.")
		play_again = False
	else:
		game_dict['previous_points'] = result['points']
		game_dict['option'] = result['carry_option']
