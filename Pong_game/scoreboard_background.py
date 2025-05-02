from turtle import Turtle

class Background(Turtle):

    def __init__(self, x, y, choosen_color):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=3, stretch_len=2)
        self.color(choosen_color)
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.stamp()