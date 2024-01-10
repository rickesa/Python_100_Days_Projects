import random
from Day11_Blackjack_Art import logo
cards = {"Ace": 11, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 10, "Queen": 10, "King": 10}
user_hand = []
dealer_hand = []


def deal_cards():
    """Deals a card"""
    card = random.choice(list(cards))
    return card


def ace(hand_score):
    """Calculates the value of an ace depending on the current hand"""
    ace_value = 0
    if hand_score + 11 > 21:
        ace_value = 1
        return ace_value
    else:
        ace_value = 11
        return ace_value


def calculate_score(card_list):
    """Calculates the value of the current hand"""
    hand_score = 0
    for card in card_list:
        if card == "Ace":
            hand_score += ace(hand_score)
        else:
            hand_score += cards[card]
    if len(card_list) == 2 and hand_score == 21:
        hand_score = 0
    return hand_score


def find_winner(users_score, dealers_score):
    """Determines the winner by taking the user's score and the dealer's score"""
    if dealers_score == 0:
        dealers_score = 21
    print(f"Your score: {users_score} | Dealer's score: {dealers_score}")
    if users_score > 21:
        print("You bust!")
    elif dealers_score > 21:
        print("Dealer bust! You win!")
    elif users_score == dealers_score:
        print("The game is a draw.")
    elif users_score > dealers_score:
        print("You win!")
    elif users_score < dealers_score:
        print("You lose!")


print(logo)
for i in range(2):
    user_hand.append(deal_cards())
    dealer_hand.append(deal_cards())
print("Dealing cards...")
print(f"    User's hand: {user_hand}")
print(f"    Dealer's first card is {dealer_hand[0]}")
user_score = calculate_score(user_hand)
dealer_score = calculate_score(dealer_hand)
if user_score == 0 and dealer_score != 0:
    print("You had blackjack! You win!")
elif user_score == 0 and dealer_score == 0:
    print("Wow! You BOTH had blackjack! Unlucky! The game ends in a tie.")
else:
    hit = True
    while hit:
        hit_me = input(f"Type 'y' for another card or 'n' to stay at {user_score}\n").lower()
        if hit_me == "y":
            user_hand.append(deal_cards())
            user_score = calculate_score(user_hand)
            print(user_hand)
            print(f"    Your score is now {user_score}")
            if user_score > 21:
                hit = False
        elif hit_me == 'n':
            hit = False
        else:
            print("     Invalid response. Try again")
    dealer_hit = True
    while dealer_hit:
        if dealer_score == 0:
            dealer_hit = False
        elif dealer_score >= 17:
            dealer_hit = False
        else:
            print(f"    Dealer's hand: {dealer_hand}, for a score of {dealer_score}. Dealer must hit")
            dealer_hand.append(deal_cards())
            dealer_score = calculate_score(dealer_hand)
    print(f"    Dealer's final hand is {dealer_hand} for a score of {dealer_score}")
    find_winner(user_score, dealer_score)
