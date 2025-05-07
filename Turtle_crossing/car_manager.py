from turtle import Turtle
import random 

COLORS = ["red","orange", "yellow","green","blue","purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()

    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(280,random.randint(-250,250))
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.goto(car.xcor() - STARTING_MOVE_DISTANCE, car.ycor())