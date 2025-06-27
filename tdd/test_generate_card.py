# pylint: skip-file

"""Tests for the generate_card.py file"""

from generate_card import generate_card, get_score

"""Tests that the generate_card function returns the correct card"""


def test_generate_card():
    assert generate_card("H", "8") == "8H"

# TODO: Write several more tests below using different inputs for the generate_card function. You won't be able to cover them all - but try to cover the main cases.


"""Tests that the generate_card function returns an error message if the suit is invalid"""
# TODO: Write several tests below to test this function


def test_generate_card_invalid_suit():
    assert generate_card("9", "8") == "Error - Invalid"


"""Tests that the generate_card function returns an error message if the number is invalid"""
# TODO: Write several tests below to test this function


def test_generate_card_invalid_number():
    assert generate_card("H", "D") == "Error - Invalid"


"""Tests that the get_score function returns the correct score"""
# TODO: Write several tests below to test this function


def test_get_score_valid():
    assert get_score("8H") == 8


"""Tests that the get_score function returns 0 if the card is invalid"""
# TODO: Write several tests below to test this function


def test_get_score_invalid():
    assert get_score("HD") == 0
