"""Tennis scoring helpers - hardened against invalid input (Lab 7).

Every public function validates its input and returns ``None`` when the input
is invalid, instead of raising an exception.  Callers can therefore do:

    result = parse_score(text)
    if result is None:
        ...  # report "invalid input"
"""
import re

# Defensive limit: no legitimate score / set summary is anywhere near this long.
# It stops absurdly large inputs from being processed (cheap DoS guard).
MAX_INPUT_LENGTH = 1000

# Valid tennis point labels within a game and their numeric value.
POINTS = {'0': 0, '15': 1, '30': 2, '40': 3}

# ASCII digits only.  int() would also accept things like '٣' (Arabic-Indic),
# '1_0' (underscores) or '+5', none of which are valid scores.
_NON_NEGATIVE_INT = re.compile(r'[0-9]+')


def _is_valid_text(value):
    """True only for a real string of acceptable length."""
    return isinstance(value, str) and len(value) <= MAX_INPUT_LENGTH


def _to_count(token):
    """Convert '12' (optionally padded with spaces) to 12; None if invalid."""
    token = token.strip()
    if _NON_NEGATIVE_INT.fullmatch(token):
        return int(token)
    return None


def parse_score(text):
    """Parse 'A-B' (e.g. '3-2') into a tuple of two non-negative ints.

    Returns None for anything that is not exactly two non-negative integers
    separated by a single '-'.
    """
    if not _is_valid_text(text):
        return None
    parts = text.split('-')
    if len(parts) != 2:
        return None
    a, b = _to_count(parts[0]), _to_count(parts[1])
    if a is None or b is None:
        return None
    return a, b


def game_lead(text):
    """Return player A's lead in points for a game score like '40-30'.

    Both sides must be one of 0, 15, 30, 40.  Returns an int in -3..3,
    or None for invalid input.
    """
    if not _is_valid_text(text):
        return None
    parts = text.split('-')
    if len(parts) != 2:
        return None
    first, second = parts[0].strip(), parts[1].strip()
    if first not in POINTS or second not in POINTS:
        return None
    return POINTS[first] - POINTS[second]


def set_spread(games_csv):
    """Return max - min of games won per set for a CSV like '6,4,7'.

    Every element must be a non-negative integer (so '', '1,,3', '6,4,' and
    'one,two' are all invalid).  Returns an int >= 0, or None for invalid input.
    """
    if not _is_valid_text(games_csv):
        return None
    games = [_to_count(g) for g in games_csv.split(',')]
    if any(g is None for g in games):
        return None
    return max(games) - min(games)


def main():
    try:
        print("==== Running parse_score ====")
        user_input = input("Enter points won as A-B (e.g. 3-2): ")
        result = parse_score(user_input)
        if result is None:
            print("Invalid input: expected two non-negative whole numbers as A-B.")
        else:
            print("Points A and B:", result)

        print("\n==== Running game_lead ====")
        user_input = input("Enter a game score (e.g. 40-30): ")
        result = game_lead(user_input)
        if result is None:
            print("Invalid input: expected two of 0, 15, 30, 40 as A-B.")
        else:
            print("Lead in Points:", result)

        print("\n==== Running set_spread ====")
        user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
        result = set_spread(user_input)
        if result is None:
            print("Invalid input: expected comma-separated whole numbers.")
        else:
            print("Spread:", result)
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")


if __name__ == "__main__":
    main()
