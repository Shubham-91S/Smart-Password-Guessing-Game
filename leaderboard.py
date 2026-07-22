def save_score(player_name, score):
    """
    Save player's score to leaderboard.txt
    """

    with open("leaderboard.txt", "a") as file:
        file.write(f"{player_name},{score}\n")


def get_leaderboard():
    """
    Read leaderboard.txt and return top 10 scores.
    """

    leaderboard = []

    try:
        with open("leaderboard.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) == 2:

                    player = data[0]

                    score = int(data[1])

                    leaderboard.append((player, score))

    except FileNotFoundError:
        pass

    # Sort by score (highest first)
    leaderboard.sort(key=lambda x: x[1], reverse=True)

    return leaderboard[:10]


def show_leaderboard():
    """
    Display leaderboard in terminal (optional).
    """

    leaderboard = get_leaderboard()

    print("\n🏆 Leaderboard 🏆")
    print("-" * 30)

    if not leaderboard:
        print("No scores available.")
        return

    for rank, (player, score) in enumerate(leaderboard, start=1):
        print(f"{rank}. {player} - {score}")