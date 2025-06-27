"""Import modules and defined global variables"""
from time import time
from random import Random
import argparse

LOSE_MESSAGE = "You lose!"
WIN_MESSAGE = "You win!"
DRAW_MESSAGE = "Draw!"

SUITS = ["S", "D", "C", "H"]
NUMBERS = ["A", "2", "3", "4", "5", "6",
           "7", "8", "9", "10", "J", "Q", "K"]

MINIMUM_NUMBER_OF_CARDS = 2
MAX_SCORE = 21
MAX_NUMBER_OF_CARDS = 6


def shuffle(deck: list, seed: int) -> list[str]:
    """Randomises a deck of cards"""
    copy_of_deck = deck.copy()
    Random(seed).shuffle(copy_of_deck)
    return copy_of_deck


def generate_deck() -> list[str]:
    """Generates a deck of cards and returns them"""
    cards = []

    for suit in SUITS:
        for number in NUMBERS:
            cards.append(number + suit)
    return cards


def points_for(cards: list[str]) -> int:
    """Calculates the amount of points for a given list of cards"""

    total_points = 0

    if len(cards) < MINIMUM_NUMBER_OF_CARDS:
        return total_points

    if len(cards) == MINIMUM_NUMBER_OF_CARDS:
        if ("A" in cards[0] and "A" in cards[1]):
            return MAX_SCORE

    if len(cards) == MAX_NUMBER_OF_CARDS and total_points < 21:
        return MAX_SCORE

    for card in cards:
        number = card[:-1]

        if number == "A":
            points = 11
        elif number in {"J", "Q", "K"}:
            points = 10
        else:
            points = int(number)
        total_points += points

    return total_points


def get_next_card_from_deck(deck: list[str]) -> str:
    """Gets the next card from the deck and returns it"""

    return deck.pop(0)


def deal_card_to_hand(deck: list[str], hand: list[str]) -> list[str]:
    """
    Draws a card from the deck and adds it to the hand then return the hand.
    """
    next_card = get_next_card_from_deck(deck)
    hand.append(next_card)
    return hand


def player_turn(deck: list[str], hand: list[str]) -> bool:
    """
    Asks the player for their next choice and changes the game state
    based on their response of either 'hit' or 'stick'
    """

    print(f"Your hand is {', '.join(hand)} ({points_for(hand)} points)")

    action = input('What do you want to do? ("hit" or "stick")')

    if action == "hit":
        print("Hitting")
        hand = deal_card_to_hand(deck, hand)

        if points_for(hand) >= 21:
            print(f"Your hand is {', '.join(hand)
                                  } ({points_for(hand)} points)")
            return False

        return True
    if action == "stick":
        print("Sticking")
        return False
    print("Invalid")
    return True


def dealer_turn(deck: list[str], hand: list[str]) -> bool:
    """Dealer automatically hits or sticks based on the points of the card"""

    print(f"Dealer's hand is {', '.join(hand)} ({points_for(hand)} points)")

    if points_for(hand) < 17:
        print("Dealer is hitting")
        hand = deal_card_to_hand(deck, hand)

        if points_for(hand) >= 17:
            print(f"Dealer's hand is {', '.join(
                hand)} ({points_for(hand)} points)")
            return False

        return True

    return None


def who_wins(player_hand: list[str], dealer_hand: list[str]) -> str:
    """Determines whether the player wins, loses, or draws"""
    player_points = points_for(player_hand)
    dealer_points = points_for(dealer_hand)

    if dealer_points > MAX_SCORE:
        return WIN_MESSAGE
    if player_points > dealer_points:
        return WIN_MESSAGE
    if player_points < dealer_points:
        return LOSE_MESSAGE
    if player_points == dealer_points:
        return DRAW_MESSAGE
    return None


def play(seed: int) -> None:
    """
    Generates a deck and deals cards to the player and dealer.

    The 'seed' parameter is used to set a specific game. If you play the game
    with seed=313131 it will always have the same outcome (the order the cards are dealt)
    """
    new_deck = generate_deck()
    shuffled_deck = shuffle(new_deck, seed)

    player_hand = [shuffled_deck.pop(0), shuffled_deck.pop(0)]

    is_player_turn = True

    while is_player_turn:
        is_player_turn = player_turn(shuffled_deck, player_hand)

    if points_for(player_hand) > 21:
        print(LOSE_MESSAGE)
        return

    dealer_hand = [shuffled_deck.pop(0), shuffled_deck.pop(0)]

    is_dealer_turn = True

    while is_dealer_turn:
        is_dealer_turn = dealer_turn(shuffled_deck, dealer_hand)

    print(who_wins(player_hand, dealer_hand))


def get_seed() -> int:
    """
    You can safely ignore this function. It is used to accept a seed from the command line.
    For example

    python3 blackjack.py --seed 313131

    Would play the game with defined seed of 313131
    """
    parser = argparse.ArgumentParser("blackjack")
    parser.add_argument(
        "--seed", dest='seed', help="The seed that a game will be played with", type=int)
    args = parser.parse_args()
    seed = args.seed

    if seed is None:
        return time()

    return seed


if __name__ == "__main__":
    retrieve_seed = get_seed()
    play(retrieve_seed)
