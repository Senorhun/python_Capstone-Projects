from turtle import Turtle
import random 
from colors import bright_colors

class Paddle(Turtle):
    def __init__(self, position):
       super().__init__()
       self.shape("square") 
       self.color(random.choice(bright_colors))
       self.shapesize(stretch_wid=5, stretch_len=1)
       self.penup()
       self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    
