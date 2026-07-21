from flask import Flask, request
import random

app = Flask(__name__)

CHOICES = ["rock", "paper", "scissors"]

def decide_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if beats[player] == computer:
        return "You win!"
    return "Computer wins!"

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Rock Paper Scissors</title>
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 60px; background: #f4f4f4; }}
        h1 {{ color: #333; }}
        button {{
            font-size: 18px; padding: 10px 20px; margin: 10px;
            border: none; border-radius: 8px; background: #4CAF50; color: white; cursor: pointer;
        }}
        button:hover {{ background: #45a049; }}
        .result {{ font-size: 24px; margin-top: 30px; color: #222; }}
    </style>
</head>
<body>
    <h1>Rock, Paper, Scissors</h1>
    <form method="POST">
        <button name="choice" value="rock">Rock</button>
        <button name="choice" value="paper">Paper</button>
        <button name="choice" value="scissors">Scissors</button>
    </form>
    <div class="result">{result}</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = "Make your move!"
    if request.method == "POST":
        player_choice = request.form.get("choice")
        computer_choice = random.choice(CHOICES)
        outcome = decide_winner(player_choice, computer_choice)
        result = f"You chose {player_choice}, computer chose {computer_choice}. {outcome}"
    return PAGE.format(result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)