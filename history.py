# history.py
# Save and Display Game History

HISTORY_FILE = "history.txt"


def save_history(player_name, category, difficulty, score, time_taken, result):
    """
    Save every game played.
    """

    with open(HISTORY_FILE, "a") as file:

        file.write(
            f"{player_name},{category},{difficulty},{score},{time_taken},{result}\n"
        )


def show_history():
    """
    Display complete game history.
    """

    try:

        with open(HISTORY_FILE, "r") as file:

            lines = file.readlines()

            if not lines:
                print("\nNo Game History Found.")
                return

            print("\n" + "=" * 85)
            print(" " * 30 + "GAME HISTORY")
            print("=" * 85)

            print(
                f"{'Player':<15}"
                f"{'Category':<15}"
                f"{'Difficulty':<12}"
                f"{'Score':<10}"
                f"{'Time':<10}"
                f"{'Result'}"
            )

            print("-" * 85)

            for line in lines:

                data = line.strip().split(",")

                if len(data) != 6:
                    continue

                player, category, difficulty, score, time_taken, result = data

                print(
                    f"{player:<15}"
                    f"{category:<15}"
                    f"{difficulty:<12}"
                    f"{score:<10}"
                    f"{time_taken:<10}"
                    f"{result}"
                )

            print("=" * 85)

    except FileNotFoundError:
        print("\nNo history available.")

def get_history():
    """
    Return all game history for Flask.
    """

    history = []

    try:
        with open(HISTORY_FILE, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                data = line.split(",")

                if len(data) != 6:
                    continue

                history.append(data)

    except FileNotFoundError:
        return []

    return history