#Step 1

word_list = ["baboon", "camel","dinosaur","giraffe","pizza","pepperoni","anchovy","zebras","galalxy","twinkle","starlight","christmas","snowman"]
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
# lives = int(input("How many lives for the game?\n"))
lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# print(f"{chosen_word}, {word_length}")
print("Welcome to Hangman!")
user_sees = []
for letter in chosen_word:
    user_sees += "_"
def check_lives(lives):
    if lives >= 1:
        print(f"You have {lives} lives remaining")
    if lives == 0:
        print(f"Sorry, the word was {chosen_word}")
        print("Game Over!")
        return False
def lose_life(lives):
    return lives-1

while lives >= 1:
    print(stages[lives])
    print(*user_sees, sep="")
    guess = input("Choose a letter:\n").lower()
    if len(guess) > 1:
        print("You may only guess one letter at a time")
    else:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                user_sees[position] = letter
        # i=0
        # for letter in chosen_word:
        #     if guess == letter:
        #         user_sees[i] = letter
        #         i+=1
        #     else:
        #         i+=1
        if guess not in user_sees:
            lives = lose_life(lives)
            check_lives(lives)
        # if check_lives(lives) == False:
        #     break
        if "_" not in user_sees:
            print(f"The word was {chosen_word}. You had {lives} lives left. You Win!")
            break





