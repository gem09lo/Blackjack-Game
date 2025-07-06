# pylint: skip-file

"""Tests for the generate_card.py file"""

from generate_card import generate_card, get_score


def test_generate_card():
    """Tests that the generate_card function returns the correct card"""
    assert generate_card("H", "8") == "8H"


def test_generate_card_invalid_suit():
    """Tests that the generate_card function returns an error message if the suit is invalid"""
    assert generate_card("9", "8") == "Error - Invalid"


def test_generate_card_invalid_number():
    """Tests that the generate_card function returns an error message if the number is invalid"""
    assert generate_card("H", "D") == "Error - Invalid"


def test_get_score_valid():
    """Tests that the get_score function returns the correct score"""
    assert get_score("8H") == 8


def test_get_score_invalid():
    """Tests that the get_score function returns 0 if the card is invalid"""
    assert get_score("HD") == 0
