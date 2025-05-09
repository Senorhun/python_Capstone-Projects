from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True
turtle = Player()
car = CarManager()
screen.listen()
screen.onkey(turtle.move_up, "Up")
scoreboard = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    scoreboard.scoreboard_update()
    for c in car.car_list:
        if abs(turtle.xcor() -c.xcor()) < 28 and abs(turtle.ycor() - c.ycor()) <20:
            scoreboard.game_over()
            game_is_on = False
    if turtle.ycor() > 280:
        turtle.next_lvl()
        car.speed_up()
        scoreboard.score_up()
        scoreboard.scoreboard_update()


screen.exitonclick()
