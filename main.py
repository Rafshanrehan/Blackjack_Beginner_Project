import random
from art import logo

def deal_card():
    ''''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #A given list of cards, which are simplified to values 2-10
    #Each 10 corresponds to the value itself, jack, king, and queen

    card = random.choice(cards)
    #picks a random card from the list and returns it
    return card


def calculate_score(cards):
    """Takes a list of cards and returns the score"""
    if sum(cards) ==21 and len(cards) == 2:
        #Easy blackjack win condition
        return 0
    if 11 in cards and sum(cards) > 21:
        #code that models how the Ace card behaves
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    #returns win and lose conditions as output
    if u_score == 0:
        return "You win with a Blackjack"
    elif c_score == 0:
        return "You lose, opponent has a Blackjack"
    elif u_score == c_score:
        return "Draw"
    elif u_score > 21:
        return "You lose, you went over 21"
    elif c_score > 21:
        return "You win, opponent went over 21"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)

    #initial setup of game condition and variables
    game_over = False
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    #first two cards are dealt
    for iteration in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #calculates score we have on hand
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        #Only show first hand of opponent
        print(f"Computer's first card: {computer_cards[0]}")



        #game ends at a blackjack for either player or if user overdraws
        if user_score ==0 or computer_score == 0 or user_score >21:
            game_over = True

        #asks user if they want to draw more or not
        else:
            user_choice = input("Type y to get another card, type n to pass: ")
            if user_choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    #modeling the dealer's actions, drawing as long as score is less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    #prints final stats
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#This runs the game itself
while input("Do you want to play a game of Blackjack? Type y for yes or n for no: ") == "y":
    print("\n" * 20)
    play_game()
