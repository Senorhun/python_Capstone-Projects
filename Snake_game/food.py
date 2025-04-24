from turtle import Turtle
from random import randint
import turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.8)
        self.speed("fastest")
        self.color("white")
        self.relocate_food()

    def relocate_food(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
