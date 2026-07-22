from flask import Flask, render_template, request, session, redirect
from game import create_game, generate_hint
from score import calculate_score
from leaderboard import save_score, get_leaderboard
from history import save_history, get_history
import time

app = Flask(__name__)
app.secret_key = "smart_password_secret"


# ---------------- HOME ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- START PAGE ---------------- #

@app.route("/start")
def start():
    return render_template("start.html")


# ---------------- START GAME ---------------- #

@app.route("/play", methods=["POST"])
def play():

    category = request.form["category"]
    difficulty = request.form["difficulty"]

    # Remove extra spaces and capitalize the name
    player_name = request.form["player_name"].strip().title()

    game = create_game(category, difficulty)

    game["player_name"] = player_name
    game["start_time"] = time.time()

    session["game"] = game

    return render_template("play.html", game=game)


# ---------------- GUESS ---------------- #

@app.route("/guess", methods=["POST"])
def guess():

    game = session["game"]

    user_guess = request.form["guess"].lower().strip()

    # Validation
    if not user_guess:
        return render_template("play.html", game=game)

    if not user_guess.isalpha():
        return render_template("play.html", game=game)

    if len(user_guess) != len(game["word"]):
        return render_template("play.html", game=game)

    # Save Guess
    game["guesses"].append(user_guess)

    # Correct Guess
    if user_guess == game["word"]:

        end_time = time.time()

        time_taken = round(end_time - game["start_time"], 2)

        score = calculate_score(
            base_score=game["base_score"],
            attempts_left=game["attempts"],
            time_taken=time_taken
        )

        save_score(
            game["player_name"],
            score
        )

        save_history(
            game["player_name"],
            game["category"],
            game["difficulty"],
            score,
            time_taken,
            "Won"
        )

        return render_template(
            "win.html",
            word=game["word"],
            score=score,
            time_taken=time_taken
        )

    # Wrong Guess
    game["attempts"] -= 1
    game["hint"] = generate_hint(game["word"], user_guess)

    # Save Updated Game
    session["game"] = game

    # Game Over
    if game["attempts"] == 0:

        end_time = time.time()

        time_taken = round(end_time - game["start_time"], 2)

        save_history(
            game["player_name"],
            game["category"],
            game["difficulty"],
            0,
            time_taken,
            "Lost"
        )

        return render_template(
            "gameover.html",
            word=game["word"],
            time_taken=time_taken
        )

    return render_template("play.html", game=game)


# ---------------- LEADERBOARD ---------------- #

@app.route("/leaderboard")
def leaderboard():

    leaderboard = get_leaderboard()

    return render_template(
        "leaderboard.html",
        leaderboard=leaderboard
    )

@app.route("/clear_leaderboard", methods=["POST"])
def clear_leaderboard():

    with open("leaderboard.txt", "w") as file:
        pass

    return redirect("/leaderboard")


@app.route("/history")
def history():

    history = get_history()

    return render_template(
        "history.html",
        history=history
    )

@app.route("/clear_history", methods=["POST"])
def clear_history():

    with open("history.txt", "w") as file:
        pass

    return redirect("/history")


# ---------------- RUN APP ---------------- #

if __name__ == "__main__":
    app.run(debug=True)