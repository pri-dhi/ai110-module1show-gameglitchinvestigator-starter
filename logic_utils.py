#FIX: Refactored logic into logic_utils.py using Copilot Agent mode
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100

#FIX: Refactored logic into logic_utils.py using Copilot Agent mode
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    raw = raw.strip()
    if raw == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw)
    except Exception:
        return False, None, "That is not a whole number."

    return True, value, None

#FIX: Refactored logic into logic_utils.py using Copilot Agent mode
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win"
    #FIX: Returning correct hints based on guess vs. secret
    if guess > secret:
        return "Too High"
    return "Too Low"

#FIX: Refactored logic into logic_utils.py using Copilot Agent mode
def get_feedback_message(outcome: str):
    """Return user-facing hint text for a guess outcome."""
    #FIX: Returning correct hints based on guess vs. secret
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        return "📉 Go LOWER!"
    if outcome == "Too Low":
        return "📈 Go HIGHER!"
    return ""

#FIX: Refactored logic into logic_utils.py using Copilot Agent mode
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
