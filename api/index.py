from flask import Flask, render_template, request
import random

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

choices = ["Rock", "Paper", "Scissor"]

@app.route("/", methods=["GET", "POST"])
def game():
    user = None
    computer = None
    result = None

    if request.method == "POST":
        user = request.form["choice"]
        computer = random.choice(choices)

        if user == computer:
            result = "Draw"
        elif (
            (user == "Rock" and computer == "Scissor")
            or (user == "Paper" and computer == "Rock")
            or (user == "Scissor" and computer == "Paper")
        ):
            result = "User Win!"
        else:
            result = "Computer Win!"

    return render_template(
        "index.html",
        user=user,
        computer=computer,
        result=result
    )