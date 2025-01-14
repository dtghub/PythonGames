from PlayingCard import *
import time

user_hand = 0
computer_hand = 1

# Function: initialise_score
# Description: Initialises who turn it is the computer of the user and how many winning hands
def initialise_score():
    return [{"turn":True, "score":0}, {"turn":False, "score":0}]

# Function: is_snap
# Description: Determine if it is snap by comparing two playing cards
def is_snap(previous_card, next_card):
    return previous_card[0] == next_card[0]

# Function: play_card
# Description: Deals a card from either the computer or the users hands and prompts the console. The next card dealt
# from either hand is then returned.
def play_card(current_score, hands, counter):
    if computer_hand == counter % 2:
        next_card = deal_a_card(hands[1])
        prompt = "Computer plays "
    else:
        # The next function returns a playing card. The playing card is the next card from the users hand. A list
        # "hands" is a list of lists of cards. The constant play_card.user_hand is used to get the hand of cards for the
        # user
        next_card = deal_a_card(hands[user_hand])
        prompt = "You played "
    print(prompt + next_card)
    return next_card

# Method: determine_winner
# Description: Determine if the computer or the user has won and display the result. If the user call snap they must do
# it in a given time set by the user.
def determine_winner(current_score, previous_card, next_card, answer, waited, seconds_to_wait):
    if answer == "S" and is_snap(previous_card, next_card) and waited < seconds_to_wait:
        print("Correct you win in " + str(waited))
        current_score[user_hand]["score"] += 1
        print("You have won " + str(current_score[user_hand]["score"]) + " hands")
    elif answer == "S" and is_snap(previous_card, next_card) and waited > seconds_to_wait:
        print("Sorry to slow you waited " + str(waited))
        print("Computer wins")
        current_score[computer_hand]["score"] += 1
        print("Computer has won " + str(current_score[computer_hand]["score"]) + " hands")
    elif answer == "S" and not is_snap(previous_card, next_card):
        print("Wrong the cards are different")
    elif answer == "N" and is_snap(previous_card, next_card):
        print("Computer wins")
        current_score[computer_hand]["score"] += 1
        print("Computer has won " + str(current_score[computer_hand]["score"]) + " hands")

# Method: main
# Description: The main logic for snap given a hands of cards and a wait time.
def snap(hands, seconds_to_wait):
    answer = "N"
    next_card = "  "
    counter = 0
    current_score = initialise_score()
    while answer.upper() in ["N", "S"]:
        previous_card = next_card
        next_card = play_card(current_score, hands, counter)
        start = time.time()
        answer = input("Please enter (S)nap or (N)ext")
        waited = time.time() - start
        determine_winner(current_score, previous_card, next_card, answer.upper(), waited, seconds_to_wait)
        counter += 1

def main():
    deck = generate_deck()
    deck = shuffle_cards(deck)
    print("We will play snap to match on suites")
    seconds_to_wait = int(input("Please enter the number of seconds to wait"))
    # The next function returns two hands of cards. It has a full deck of cards as an input. The number of cards to deal
    # is zero so all cards are dealt to the two players. The last parameter is an empty list since the players have not
    # already been dealt any cards.
    hands = deal_cards(deck, 0, 2)
    snap(hands, seconds_to_wait)

main()