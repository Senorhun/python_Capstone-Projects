from turtle import Turtle

FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 250)
        self.refresh_scoreboard()
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("Game over", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=FONT)
