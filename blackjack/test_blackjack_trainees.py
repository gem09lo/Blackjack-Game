# pylint: skip-file

"""File for tests written by you - the trainee"""

from blackjack import generate_deck, points_for, play, get_next_card_from_deck, deal_card_to_hand, who_wins, LOSE_MESSAGE, WIN_MESSAGE, DRAW_MESSAGE
from support.testing_util import player_chooses


def test_points_for_valid():
    assert points_for(["7H", "2D"]) == 9


def test_points_for_empty():
    assert points_for([]) == 0


def test_points_for_one_card_invalid():
    assert points_for(["8H"]) == 0


def test_points_for_two_aces():
    assert points_for(["AH", "AD"]) == 21


def test_points_for_six_card_draw():
    assert points_for(["2H", "6D", "2D", "3S", "2C", "3H",]) == 21


def test_points_for_two_aces_plus_one():
    assert points_for(["4H", "AD", "AS"]) == 26


def test_get_next_card_from_deck_valid():
    assert get_next_card_from_deck(["8H", "9S", "JD"]) == "8H"


def test_deal_card_to_hand():
    assert deal_card_to_hand(["7D", "8D", "JH"], ["AS", "8S", "JD"]) == [
        "AS", "8S", "JD", "7D"]


def test_who_wins_player_won():
    assert who_wins(["9D", "10S"], ["9H", "4S"]) == "You win!"


def test_who_wins_player_won_when_dealer_busts():
    assert who_wins(["KS", "10S"], ["4D", "AH", "9H"]) == "You win!"


def test_who_wins_player_lost():
    assert who_wins(["9D", "5S"], ["9H", "9S"]) == "You lose!"


def test_who_wins_draw():
    assert who_wins(["QC", "8C"], ["8S", "JC"]) == "Draw!"


def test_who_wins_both_21_draw():
    assert who_wins(["AC", "AD"], ["AS", "AH"]) == "Draw!"


def test_who_wins_draw():
    assert who_wins(["QC", "8C"], ["8S", "JC"]) == "Draw!"


def test_who_wins_player_starts_with_21():
    assert who_wins(["QC", "AD"], ["6C", "QS"]) == "You win!"


"""Challenge 2f: Testing code with capsys and monkeypatch"""


def test_player_turn_output_hitting(monkeypatch, capsys):
    """player_turn(): choosing to hit outputs a "Hitting" message """
    player_chooses(["hit", "stick"], monkeypatch)

    play(313131)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")

    assert "Hitting" in printed_lines


def test_player_wins_after_players_turn_then_dealer_busts(monkeypatch, capsys):
    """A test that confirms the player wins after their turn due to dealer busting"""
    player_chooses(["hit", "stick"], monkeypatch)

    play(313131)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")

    assert "You win!" in printed_lines


def test_player_loses_after_player_busts(monkeypatch, capsys):
    """A test that confirms the player loses after busting"""
    player_chooses(["hit"], monkeypatch)

    play(215)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")

    assert "You lose!" in printed_lines


def test_player_loses_with_lower_score_starting_hand(monkeypatch, capsys):
    """A test that confirms that the player loses with starting hand when the dealer has a higher score"""

    player_chooses(["stick"], monkeypatch)

    play(12)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")

    assert "You lose!" in printed_lines


def test_player_loses_with_lower_score_after_their_turn(monkeypatch, capsys):
    """A test that confirms that the player loses when they have the lower score after player_turn()"""

    player_chooses(["hit", "hit", "stick"], monkeypatch)

    play(313131)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")

    assert "You lose!" in printed_lines


def test_player_draws_two_aces_and_wins(monkeypatch, capsys):
    """A test that confirms the player draws two aces and gets a score of 21 and wins after dealer_turn()"""

    player_chooses(["stick"], monkeypatch)

    play(1172)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")

    assert "You win!" in printed_lines


def test_player_and_dealer_draw(monkeypatch, capsys):
    """A test that confirms the player and dealer draws game after getting the same points"""

    player_chooses(["stick"], monkeypatch)

    play(215)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")

    assert "Draw!" in printed_lines


def test_player_turn_first_then_dealer(monkeypatch, capsys):
    """A test that confirms that the player and dealer take their turns in order"""

    player_chooses(["stick"], monkeypatch)

    play(215)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")

    assert "Your hand" in printed_lines[0]
    assert "Dealer's hand" in printed_lines[2]


def test_dealer_turn_skipped_when_player_busts(monkeypatch, capsys):
    """A test that confirms that dealer's turn is skipped if player busts"""

    player_chooses(["hit"], monkeypatch)

    play(233)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")

    assert "Dealer's hand" not in printed_lines


def test_player_21_points_with_6_cards(monkeypatch, capsys):
    """A test that confirms the player gets 21 points after getting 6 cards and total points are lower than 21"""
    player_chooses(["hit", "hit", "hit", "hit"], monkeypatch)

    play(19643)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")[-4]

    assert "21 points" in printed_lines


def test_player_wins_with_6_cards(monkeypatch, capsys):
    """A test that confirms the player wins with 6 cards and higher points than dealer"""

    player_chooses(["hit", "hit", "hit", "hit"], monkeypatch)

    play(19643)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")

    assert "You win!" in printed_lines


def tests_dealer_stops_at_17(monkeypatch, capsys):
    """A test that confirms the dealer draws 17 or more and stops"""

    player_chooses(["stick"], monkeypatch)

    play(32)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")

    assert "Draw!" in printed_lines
