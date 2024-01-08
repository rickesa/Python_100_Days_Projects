from Day11_Blackjack_Art import *
import random
# ************ Our Blackjack House Rules ************
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
# Use the following list as the deck of cards:
cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
card_art_dict = {"Ace": ace_art, 2: two_art, 3: three_art, 4: four_art, 5: five_art, 6: six_art, 7: seven_art, 8: eight_art, 9: nine_art, 10: ten_art, "Jack": jack_art, "Queen": queen_art, "King": king_art}
card_value = 0
user_cards = []
user_card_sum = 0
dealer_cards = []
dealer_card_sum = 0
user = "User"
dealer = "Dealer"
stop = False
bust_flag = False


def ace(hand_sum):
    """If an ace is pulled, assign its value as 11, or assign 1 if the hand sum + 11 would bust"""
    # print(f"Pre-ace hand_sum = {hand_sum}")
    ace_value = 0
    if hand_sum + 11 > 21:
        ace_value += 1
        return ace_value
    else:
        ace_value += 11
        return ace_value


face_values_dict = {"Ace": ace, "Jack": 10, "Queen": 10, "King": 10}


def deal_cards():
    """Deals 2 cards to both the user and the dealer"""
    print("Dealing cards...")
    card1 = random.choice(cards)
    user_cards.append(card1)
    card2 = random.choice(cards)
    user_cards.append(card2)
    card1 = random.choice(cards)
    print(f"Dealer's first card is {card1}")
    print(card_art_dict[card1])
    card2 = random.choice(cards)
    dealer_cards.append(card1)
    dealer_cards.append(card2)
    print(f"User's hand: {user_cards}")


def card_math(card_list):
    """Calculates the value of the current hand"""
    hand_sum = 0
    for card in card_list:
        if card in face_values_dict:
            if card == "Ace":
                card_value = ace(hand_sum)
            else:
                card_value = face_values_dict[card]
        else:
            card_value = card
        hand_sum += card_value
    return hand_sum


def check_bust(hand_sum):
    """checks whether a card being added to the hand will result in a bust"""
    is_bust = False
    if hand_sum > 21:
        is_bust = True
        return is_bust

    else:
        return is_bust


def hit_me(hand_sum1, player):
    """Deals additional card to the player or dealer, depending on which player is passed as an argument"""
    if player == user:
        again = True
        while again:
            card_next = random.choice(cards)
            print(f"The next card was a {card_next}")
            user_cards.append(card_next)
            hand_sum1 = card_math(user_cards)
            return hand_sum1
    elif player == "Dealer":
        card_next = random.choice(cards)
        print(f"Dealer drew a {card_next}.")
        dealer_cards.append(card_next)
        hand_sum1 = card_math(dealer_cards)
        # Logic to handle if dealer stays or hits. 16 or under must hit, 17 or over must stay
        if hand_sum1 <= 16:
            hand_sum1 = hit_me(hand_sum1, dealer)
            return hand_sum1
        elif hand_sum1 >= 17:
            return hand_sum1


def find_winner(user_hand_sum, dealer_hand_sum):
    """Takes the hands of each player and compares them to find the winner"""
    print(f"You had: {user_cards}")
    print(f"Dealer had: {dealer_cards}")
    if user_hand_sum > 21:
        print("You bust! You lose")
    elif dealer_hand_sum > 21:
        print("Dealer bust! You win!")
    elif user_hand_sum > dealer_hand_sum:
        print(f"Your hand of {user_hand_sum} beat the dealer's hand of {dealer_hand_sum}. You win!")
    elif user_hand_sum < dealer_hand_sum:
        print(f"The dealer's hand of {dealer_hand_sum} beat your hand of {user_hand_sum}. You lose!")
    elif user_hand_sum == dealer_hand_sum:
        print(f"Your hand and the dealer's hand are tied at {user_hand_sum}! This hand is a draw.")


def play_blackjack(user_sum, dealer_sum, should_stop, flag_for_bust):
    """begins a new blackjack game"""
    print(logo)
    deal_cards()
    user_sum += card_math(user_cards)
    dealer_sum += card_math(dealer_cards)
    if user_sum == 21:
        check_stop = input(f"Your cards are {user_cards} and have {user_sum}! You have no moves. Type 'y' to proceed")
        if check_stop == 'y':
            should_stop = True
        else:
            "Lol you lost because you wanted to I guess"
    while not should_stop:
        print(f"Your hand is at {user_sum}.")
        hit = input("Would you like another card? Type 'y' to hit or 'n' to stay ").lower()
        if hit == 'y':
            user_sum = hit_me(user_sum, user)
            flag_for_bust = check_bust(user_sum)
            if flag_for_bust:
                should_stop = True
        else:
            should_stop = True
    if not flag_for_bust:
        print(f"Dealer's cards are {dealer_cards}")
        if dealer_sum == 21:
            find_winner(user_sum, dealer_sum)
        if dealer_sum <= 16:
            dealer_sum = hit_me(dealer_sum, dealer)
        if dealer_sum >= 17:
            find_winner(user_sum, dealer_sum)
    else:
        print(f"Your hand of {user_sum} went over! You lose!")


play = True
while play:
    play_again = input("Would you like to play blackjack? Type 'y' or 'n' ").lower()
    if play_again == 'y':
        card_value = 0
        user_cards = []
        user_card_sum = 0
        dealer_cards = []
        dealer_card_sum = 0
        stop = False
        bust_flag = False
        play_blackjack(user_card_sum, dealer_card_sum, stop, bust_flag)
    else:
        print("Thanks for playing!")
        play = False
