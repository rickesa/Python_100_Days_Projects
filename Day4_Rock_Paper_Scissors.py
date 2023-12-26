import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

response_objects = [rock,paper,scissors]
responses = ["rock","paper","scissors"]
computer_move = random.randint(0,2)
while True:
    input1 = input("Choose rock, paper, or scissors\n")
    if input1 not in responses:
        print("Invalid answer. Try again")
    else:
        break
computer = response_objects[computer_move]
inputindex = responses.index(input1)
player1 = response_objects[inputindex]
print(f"You played")
print(player1)
print("Computer played")
print(computer)

# Original method using strings
# if player1 == player2:
#     print("The game was a tie")
# elif player1 == rock and player2 == scissors:
#     print("Your win!")
# elif player1 == rock and player2 == paper:
#     print("You lose!")
# elif player1 == paper and player2 == rock:
#     print("You win!")
# elif player1 == paper and player2 == scissors:
#     print("You lose!")
# elif player1 == scissors and player2 == paper:
#     print("You win!")
# elif player1 == scissors and player2 == rock:
#     print("You lose!")

# Faster method using indexes
# 0 = rock, 1 = paper, 2 = scissors
# if computer picks scissors and I pick rock, I lose
if computer_move == 0 and inputindex == 2:
    print("You lose!")
# if computer picks scissors and I pick rock, I win
elif computer_move == 2 and inputindex == 0:
    print("You win!")
# paper beats rock, scissors beats paper
elif computer_move > inputindex:
    print("You lose!")
elif computer_move < inputindex:
    print("You win!")



elif computer_move == inputindex:
    print("the game was a tie")


