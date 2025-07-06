"""This file is used to generate a card for the blackjack game"""

suits = ["D", "C", "H", "S"]
numbers = ["A", "2", "3", "4", "5", "6",
           "7", "8", "9", "10", "J", "Q", "K"]


def is_valid(suit, number):
    return suit in suits and number in numbers


def generate_card(suit: str, number: str) -> str:
    """Generates a card based on the suit and number. (e.g. 8J) Should return an "Error" message if the suit or number is invalid."""
    card = ""

    if is_valid(suit, number):
        card = number + suit
        return card
    return ("Error - Invalid")


card = generate_card("H", "8")
print(card)
# valid card - "8H"


def get_score(card: str) -> int:
    """Gets the score of the card (e.g. 8J returns 8). Return 0 if the card is invalid"""

    number = card[:-1]
    suit = card[-1]

    if is_valid(suit, number):

        print(suit)
        print(number)
        if number == "A":
            points = 11
        elif number in ("J", "Q", "K")
        points = 10
        else:
            points = int(number)
    else:
        points = 0

    return points


print(get_score(card))
