"""Lab 6 - Branch coverage tests for tennis_scoring.py

Every decision in the module is exercised in both its True and False
direction, including boundary values.

Run from the lab6 directory:
    coverage run --branch --source=. -m pytest BranchCoverageTest_tennis_scoring.py
    coverage report -m
"""
import pytest
from tennis_scoring import game_score, set_winner, match_status


# ---------------------------------------------------------------- game_score
def test_game_start():
    assert game_score(0, 0) == "0-0"


@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 0, "15-0"), (0, 1, "0-15"), (2, 1, "30-15"), (3, 2, "40-30"), (2, 3, "30-40")],
)
def test_game_normal_scores(a, b, expected):
    # a < 4, b < 4 and not both >= 3 -> falls through to the lookup table
    assert game_score(a, b) == expected


@pytest.mark.parametrize("a, b", [(-1, 0), (0, -1), (-1, -1)])
def test_game_negative_points_raises(a, b):
    # True branch of "a < 0 or b < 0" (each operand on its own and both)
    with pytest.raises(ValueError, match="negative points"):
        game_score(a, b)


def test_game_zero_points_does_not_raise():
    # False branch of the negative check (boundary: 0 is valid)
    assert game_score(0, 0) == "0-0"


@pytest.mark.parametrize("a, b", [(4, 0), (4, 1), (4, 2)])
def test_game_won_by_a_before_deuce_zone(a, b):
    assert game_score(a, b) == "game A"


@pytest.mark.parametrize("a, b", [(0, 4), (1, 4), (2, 4)])
def test_game_won_by_b_before_deuce_zone(a, b):
    assert game_score(a, b) == "game B"


def test_game_a_at_three_b_below_three_skips_deuce_zone():
    # a >= 3 True, b >= 3 False
    assert game_score(3, 2) == "40-30"


def test_game_b_at_three_a_below_three_skips_deuce_zone():
    # a >= 3 False (short-circuit)
    assert game_score(2, 3) == "30-40"


@pytest.mark.parametrize("a, b", [(3, 3), (4, 4), (10, 10)])
def test_game_deuce(a, b):
    assert game_score(a, b) == "deuce"


@pytest.mark.parametrize("a, b", [(4, 3), (5, 4), (11, 10)])
def test_game_advantage_a(a, b):
    assert game_score(a, b) == "advantage A"


@pytest.mark.parametrize("a, b", [(3, 4), (4, 5), (10, 11)])
def test_game_advantage_b(a, b):
    assert game_score(a, b) == "advantage B"


@pytest.mark.parametrize("a, b", [(5, 3), (6, 4), (12, 10)])
def test_game_won_by_a_after_deuce(a, b):
    assert game_score(a, b) == "game A"


@pytest.mark.parametrize("a, b", [(3, 5), (4, 6), (10, 12)])
def test_game_won_by_b_after_deuce(a, b):
    assert game_score(a, b) == "game B"


# --------------------------------------------------------------- set_winner
def test_set_undecided():
    assert set_winner(3, 2) is None


@pytest.mark.parametrize("a, b", [(0, 0), (5, 5), (6, 5), (5, 6), (6, 6)])
def test_set_undecided_boundaries(a, b):
    # 6 games without a 2-game lead and not a 7-6 / 6-7 result
    assert set_winner(a, b) is None


@pytest.mark.parametrize("a, b", [(6, 0), (6, 4), (8, 6)])
def test_set_won_by_a_with_two_game_lead(a, b):
    assert set_winner(a, b) == "A"


@pytest.mark.parametrize("a, b", [(0, 6), (4, 6), (6, 8)])
def test_set_won_by_b_with_two_game_lead(a, b):
    assert set_winner(a, b) == "B"


def test_set_tiebreak_won_by_a():
    assert set_winner(7, 6) == "A"


def test_set_tiebreak_won_by_b():
    assert set_winner(6, 7) == "B"


def test_set_seven_games_but_not_tiebreak_score():
    # a == 7 True, b == 6 False -> falls through to None
    assert set_winner(7, 5) == "A"  # 2-game lead, decided earlier
    assert set_winner(7, 7) is None


# ------------------------------------------------------------- match_status
@pytest.mark.parametrize("best_of, sets_a", [(1, 1), (3, 2), (5, 3)])
def test_match_a_wins(best_of, sets_a):
    assert match_status(sets_a, 0, best_of) == "A wins"


@pytest.mark.parametrize("best_of, sets_b", [(1, 1), (3, 2), (5, 3)])
def test_match_b_wins(best_of, sets_b):
    assert match_status(0, sets_b, best_of) == "B wins"


@pytest.mark.parametrize("best_of, sets", [(3, 1), (5, 2)])
def test_match_decider(best_of, sets):
    assert match_status(sets, sets, best_of) == "decider"


@pytest.mark.parametrize(
    "sets_a, sets_b, best_of",
    [(0, 0, 3), (1, 0, 3), (0, 1, 3), (2, 1, 5), (1, 2, 5), (2, 0, 5)],
)
def test_match_in_progress(sets_a, sets_b, best_of):
    assert match_status(sets_a, sets_b, best_of) == "in progress"
