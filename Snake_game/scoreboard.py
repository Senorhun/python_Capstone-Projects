from turtle import Turtle

FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.best_score = 0
        self.lives = 3
        
        self.refresh_scoreboard()
        self.hideturtle()

    def game_over(self):
        
        self.lives -= 1
        self.refresh_scoreboard()
        if self.lives == 0:
            self.color("white")
            self.goto(0,0)
            self.write("GAME OVER", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.color("yellow")
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.score}   Best score: {self.best_score}", align="center", font=FONT)
        self.goto(0, 200)
        self.write(f"{self.lives} Lives left", align="center", font=FONT)

    def reset_score(self):
        if self.score > self.best_score:
            self.best_score = self.score
            self.score = 0
