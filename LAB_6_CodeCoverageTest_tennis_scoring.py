"""Lab 6 - Code (line) coverage tests for tennis_scoring.py

Run from the lab6 directory:
    coverage run --source=. -m pytest CodeCoverageTest_tennis_scoring.py
    coverage report -m
"""
import pytest
from tennis_scoring import game_score, set_winner, match_status


# ---------------------------------------------------------------- game_score
def test_game_start():
    assert game_score(0, 0) == "0-0"


def test_game_normal_score():
    assert game_score(2, 1) == "30-15"


def test_game_negative_points_raises():
    with pytest.raises(ValueError):
        game_score(-1, 0)


def test_game_won_by_a_before_deuce():
    assert game_score(4, 1) == "game A"


def test_game_won_by_b_before_deuce():
    assert game_score(0, 4) == "game B"


def test_game_deuce():
    assert game_score(3, 3) == "deuce"


def test_game_advantage_a():
    assert game_score(4, 3) == "advantage A"


def test_game_advantage_b():
    assert game_score(3, 4) == "advantage B"


def test_game_won_by_a_after_deuce():
    assert game_score(5, 3) == "game A"


def test_game_won_by_b_after_deuce():
    assert game_score(3, 5) == "game B"


# --------------------------------------------------------------- set_winner
def test_set_undecided():
    assert set_winner(3, 2) is None


def test_set_won_by_a():
    assert set_winner(6, 4) == "A"


def test_set_won_by_b():
    assert set_winner(2, 6) == "B"


def test_set_tiebreak_won_by_a():
    assert set_winner(7, 6) == "A"


# ------------------------------------------------------------- match_status
def test_match_a_wins():
    assert match_status(2, 0, 3) == "A wins"


def test_match_b_wins():
    assert match_status(1, 2, 3) == "B wins"


def test_match_decider():
    assert match_status(1, 1, 3) == "decider"


def test_match_in_progress():
    assert match_status(1, 0, 3) == "in progress"
