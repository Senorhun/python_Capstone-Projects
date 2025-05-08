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
time_speed = 0.1
while game_is_on:
    time.sleep(time_speed)
    screen.update()
    car.create_car()
    car.move()
    for c in car.car_list:
        if abs(turtle.xcor() -c.xcor()) < 28 and abs(turtle.ycor() - c.ycor()) <20:
            game_is_on = False
    if turtle.ycor() > 280:
        turtle.next_lvl()
        time_speed *= 0.7
screen.exitonclick()
