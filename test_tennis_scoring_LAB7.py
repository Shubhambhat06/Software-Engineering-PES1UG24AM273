"""Lab 7 - Fuzz tests for tennis_scoring.py using Hypothesis.

Three groups of tests:

1. NO-CRASH tests (required by the handout): every function must survive any
   text (or None) without raising an exception.
2. PROPERTY tests: on *valid* input the functions must return the right answer,
   and on arbitrary input the result must be either None (rejected) or a value
   of the right type / range.
3. MALFORMED-TYPE tests: non-string input (ints, floats, lists, bytes ...) must
   be rejected gracefully instead of raising TypeError / AttributeError.
"""
from hypothesis import given, strategies as st

from tennis_scoring import parse_score, game_lead, set_spread

TENNIS_POINTS = {"0": 0, "15": 1, "30": 2, "40": 3}

# Anything that is NOT a string (and not None) - "malformed" input.
non_strings = st.one_of(
    st.integers(),
    st.floats(allow_nan=True, allow_infinity=True),
    st.booleans(),
    st.binary(),
    st.lists(st.integers()),
    st.dictionaries(st.text(), st.integers()),
    st.tuples(st.integers(), st.integers()),
)


# --------------------------------------------------------------------------
# 1. NO-CRASH tests (from the handout)
# --------------------------------------------------------------------------
@given(st.text() | st.none())
def test_parse_score_no_crash(s):
    try:
        parse_score(s)
    except Exception as e:
        assert False, f"parse_score crashed with: {e!r}"


@given(st.text() | st.none())
def test_game_lead_no_crash(s):
    try:
        game_lead(s)
    except Exception as e:
        assert False, f"game_lead crashed with: {e!r}"


@given(st.text() | st.none())
def test_set_spread_no_crash(s):
    try:
        set_spread(s)
    except Exception as e:
        assert False, f"set_spread crashed with: {e!r}"


# --------------------------------------------------------------------------
# 2. PROPERTY tests - correctness on valid input, sane output on any input
# --------------------------------------------------------------------------
@given(st.integers(min_value=0, max_value=10**6),
       st.integers(min_value=0, max_value=10**6))
def test_parse_score_round_trip(a, b):
    assert parse_score(f"{a}-{b}") == (a, b)


@given(st.text())
def test_parse_score_result_shape(s):
    result = parse_score(s)
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
        and all(isinstance(n, int) and n >= 0 for n in result)
    )


@given(st.sampled_from(sorted(TENNIS_POINTS)),
       st.sampled_from(sorted(TENNIS_POINTS)))
def test_game_lead_valid_scores(first, second):
    expected = TENNIS_POINTS[first] - TENNIS_POINTS[second]
    assert game_lead(f"{first}-{second}") == expected
    # swapping the players must flip the sign
    assert game_lead(f"{second}-{first}") == -expected


@given(st.text())
def test_game_lead_result_range(s):
    result = game_lead(s)
    assert result is None or (isinstance(result, int) and -3 <= result <= 3)


@given(st.lists(st.integers(min_value=0, max_value=50), min_size=1))
def test_set_spread_valid_lists(games):
    csv = ",".join(str(g) for g in games)
    assert set_spread(csv) == max(games) - min(games)


@given(st.text())
def test_set_spread_result_shape(s):
    result = set_spread(s)
    assert result is None or (isinstance(result, int) and result >= 0)


# --------------------------------------------------------------------------
# 3. MALFORMED-TYPE tests - non-string input is rejected, never raises
# --------------------------------------------------------------------------
@given(non_strings)
def test_parse_score_rejects_non_strings(x):
    assert parse_score(x) is None


@given(non_strings)
def test_game_lead_rejects_non_strings(x):
    assert game_lead(x) is None


@given(non_strings)
def test_set_spread_rejects_non_strings(x):
    assert set_spread(x) is None


# --------------------------------------------------------------------------
# Regression tests: concrete inputs that Hypothesis found / the handout lists
# --------------------------------------------------------------------------
def test_known_bad_inputs_are_rejected():
    for bad in ["", "-", "3", "3-", "-2", "a-b", "3-2-1", "3--2", " ", "1_0-2", "\u0663-\u0662", "\u00b2-3", "+3-2"]:
        assert parse_score(bad) is None, bad
    for bad in ["", "40", "50-30", "40-", "-30", "AD-40", "40-30-15", "15–30"]:
        assert game_lead(bad) is None, bad
    for bad in ["", ",", "1,,3", "6,4,", ",6", "one,two", "6;4", "-1,3", "1.5,2", "\u0666,\u0664"]:
        assert set_spread(bad) is None, bad


def test_known_good_inputs():
    assert parse_score("3-2") == (3, 2)
    assert parse_score(" 3 - 2 ") == (3, 2)
    assert game_lead("40-30") == 1
    assert game_lead("0-40") == -3
    assert set_spread("6,4,7") == 3
    assert set_spread("6") == 0
