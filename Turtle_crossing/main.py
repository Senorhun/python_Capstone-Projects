from turtle import Screen
import time
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True
turtle = Player()
car = CarManager()
screen.listen()
screen.onkey(turtle.move_up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
