from turtle import Turtle

class Side(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.2, stretch_len=80)
        self.goto(x, y)
        self.stamp() 