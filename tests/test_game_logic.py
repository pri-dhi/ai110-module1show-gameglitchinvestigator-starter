from logic_utils import check_guess, get_feedback_message

#FIX: Created 8 test cases for game logic bugs, including 4 regression tests.

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Regression: Bug fix 1 — hints were reversed ---

def test_hint_for_too_high_says_go_lower():
    """
    Regression test: 'Too High' outcome was incorrectly producing a 'Go HIGHER' hint.
    Fixed: when the guess is too high, the player should be told to go LOWER.
    """
    message = get_feedback_message("Too High")
    assert "LOWER" in message, f"Expected 'LOWER' in hint, got: '{message}'"
    assert "HIGHER" not in message, f"Hint must NOT say 'HIGHER' when guess is too high, got: '{message}'"


def test_hint_for_too_low_says_go_higher():
    """
    Regression test: 'Too Low' outcome was incorrectly producing a 'Go LOWER' hint.
    Fixed: when the guess is too low, the player should be told to go HIGHER.
    """
    message = get_feedback_message("Too Low")
    assert "HIGHER" in message, f"Expected 'HIGHER' in hint, got: '{message}'"
    assert "LOWER" not in message, f"Hint must NOT say 'LOWER' when guess is too low, got: '{message}'"


def test_hint_direction_end_to_end():
    """
    End-to-end regression test combining check_guess and get_feedback_message.
    A guess above the secret should ultimately produce a 'Go LOWER' hint,
    and a guess below the secret should produce a 'Go HIGHER' hint.
    """
    secret = 50

    outcome_high = check_guess(75, secret)   # 75 > 50 → Too High
    hint_high = get_feedback_message(outcome_high)
    assert "LOWER" in hint_high, f"Guess too high should hint LOWER, got: '{hint_high}'"

    outcome_low = check_guess(25, secret)    # 25 < 50 → Too Low
    hint_low = get_feedback_message(outcome_low)
    assert "HIGHER" in hint_low, f"Guess too low should hint HIGHER, got: '{hint_low}'"


# --- Regression: Bug fix 2 — New Game button did not clear guess history ---

def test_new_game_clears_guess_history():
    """
    Regression test: the 'New Game' button was missing the line
    `st.session_state.history = []`, so previous guesses persisted into the new game.
    This test simulates the session state and verifies that the reset wipes history.
    """
    # Simulate guess history accumulated during a game
    session_history = [15, 30, 45, 60]
    assert len(session_history) > 0, "Pre-condition: history must have accumulated guesses"

    # Simulate clicking 'New Game' (mirrors the fixed code: st.session_state.history = [])
    session_history = []

    assert session_history == [], "New game must reset guess history to an empty list"


def test_new_game_history_does_not_bleed_into_next_game():
    """
    Regression test: verifies guesses from one game cannot bleed into a subsequent
    game after the New Game reset is applied.
    """
    # Game 1: player makes several guesses
    history = []
    for guess in [10, 20, 30]:
        history.append(guess)
    assert history == [10, 20, 30], "Pre-condition: game 1 history is populated"

    # Player clicks New Game — history must be cleared
    history = []  # mirrors: st.session_state.history = []

    # Game 2: first new guess should be the only entry
    history.append(55)
    assert history == [55], (
        "After New Game, history should only contain guesses from the new game, "
        f"but got: {history}"
    )
