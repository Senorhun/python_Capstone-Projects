from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)

    def scoreboard_update(self):
        self.clear()
        self.write(f"Level: {self.lvl}", align='left', font= FONT)

    def score_up(self):
         self.lvl += 1
    
    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"GAME OVER", align='center', font= FONT)