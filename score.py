# score.py
# Calculates the player's final score

def calculate_score(base_score, attempts_left, time_taken):
    """
    Calculate the final score based on:
    - Difficulty base score
    - Remaining attempts
    - Time taken
    """

    # Bonus for remaining attempts
    attempt_bonus = attempts_left * 20

    # Time penalty
    time_penalty = int(time_taken / 5)

    score = base_score + attempt_bonus - time_penalty

    if score < 50:
        score = 50

    return score


def show_high_score():
    """
    Display the highest score stored
    in leaderboard.txt
    """

    try:
        with open("leaderboard.txt", "r") as file:

            scores = []

            for line in file:

                parts = line.strip().split(",")

                if len(parts) == 2:
                    name = parts[0]
                    score = int(parts[1])

                    scores.append((name, score))

            if not scores:
                print("\nNo scores available.")
                return

            highest = max(scores, key=lambda x: x[1])

            print("\n========== HIGH SCORE ==========")
            print(f"Player : {highest[0]}")
            print(f"Score  : {highest[1]}")
            print("================================")

    except FileNotFoundError:
        print("\nNo leaderboard found yet.")