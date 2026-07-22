import time

from words import (
    show_categories,
    get_random_word,
    get_attempts,
    get_base_score
)

from score import calculate_score
from leaderboard import save_score
from history import save_history


def generate_hint(secret, guess):
    """
    Show correctly guessed letters in the correct position.
    """

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    return hint


def start_game(player_name):

    print("\n" + "=" * 60)
    print("             SMART PASSWORD GUESSING GAME")
    print("=" * 60)

    # ------------------------
    # Category
    # ------------------------

    show_categories()

    category = input("\nChoose Category (1-5): ")

    # ------------------------
    # Difficulty
    # ------------------------

    print("\nChoose Difficulty")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        difficulty = "easy"
    elif choice == "2":
        difficulty = "medium"
    elif choice == "3":
        difficulty = "hard"
    else:
        print("\nInvalid Choice!")
        difficulty = "easy"

    result = get_random_word(category, difficulty)

    if result is None:
        print("\nInvalid Category.")
        input("Press Enter...")
        return

    secret_word, category_name = result

    attempts = get_attempts(difficulty)

    base_score = get_base_score(difficulty)

    previous_guesses = []

    print("\nGame Starting...")

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    print("\nGO!\n")

    print("=" * 60)
    print(f"Player      : {player_name}")
    print(f"Category    : {category_name}")
    print(f"Difficulty  : {difficulty.title()}")
    print(f"Word Length : {len(secret_word)}")
    print(f"Attempts    : {attempts}")
    print("=" * 60)

    start_time = time.time()

    # ------------------------
    # GAME LOOP
    # ------------------------

    while attempts > 0:

        print(f"\nRemaining Attempts : {attempts}")

        guess = input("Enter Guess : ").lower().strip()

        if guess == "":
            print("Please enter a word.")
            continue

        if not guess.isalpha():
            print("Only alphabets are allowed.")
            continue

        if len(guess) != len(secret_word):
            print(f"Word must contain {len(secret_word)} letters.")
            continue

        previous_guesses.append(guess)

        # ------------------------
        # Correct Guess
        # ------------------------

        if guess == secret_word:

            end_time = time.time()

            time_taken = round(end_time - start_time, 2)

            score = calculate_score(
                base_score=base_score,
                attempts_left=attempts,
                time_taken=time_taken
            )

            print("\n" + "=" * 60)
            print("🎉 CONGRATULATIONS!")
            print("=" * 60)
            print(f"Player        : {player_name}")
            print(f"Secret Word   : {secret_word}")
            print(f"Category      : {category_name}")
            print(f"Difficulty    : {difficulty.title()}")
            print(f"Time Taken    : {time_taken} seconds")
            print(f"Attempts Left : {attempts}")
            print(f"⭐ Final Score : {score}")

            save_score(player_name, score)

            save_history(
                player_name,
                category_name,
                difficulty,
                score,
                time_taken,
                "Won"
            )

            print("\n🏆 Score saved successfully!")

            input("\nPress Enter to return to menu...")

            return

        # ------------------------
        # Wrong Guess
        # ------------------------

        attempts -= 1

        hint = generate_hint(secret_word, guess)

        print("\n❌ Wrong Guess!")

        print("Hint :", hint)

        print("\nPrevious Guesses:")

        for i, word in enumerate(previous_guesses, start=1):
            print(f"{i}. {word}")

        if attempts > 0:
            print(f"\n❤️ Attempts Left : {attempts}")

    # ------------------------
    # Game Over
    # ------------------------

    print("\n" + "=" * 60)
    print("💀 GAME OVER")
    print("=" * 60)

    print(f"\nThe Secret Word was : {secret_word}")

    end_time = time.time()

    time_taken = round(end_time - start_time, 2)

    score = 0

    save_history(
        player_name,
        category_name,
        difficulty,
        score,
        time_taken,
        "Lost"
    )

    print(f"Time Taken : {time_taken} seconds")

    print("\nBetter Luck Next Time!")

    input("\nPress Enter to return to menu...")
        

# =====================================
# Create Game for Flask
# =====================================

def create_game(category, difficulty):

    word, category_name = get_random_word(category, difficulty)

    return {
        "word": word,
        "category": category_name,
        "difficulty": difficulty,
        "attempts": get_attempts(difficulty),
        "base_score": get_base_score(difficulty),
        "guesses": [],
        "hint": "_" * len(word)
    }