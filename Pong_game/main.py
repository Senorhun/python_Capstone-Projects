from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from scoreboard_background import Background
import time
import turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
turtle.colormode(255)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
ball = Ball()
l_scoreboard_background = Background(-102, 240, l_paddle.chosen_color)
r_scoreboard_background = Background(98, 240, r_paddle.chosen_color)
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s ")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    scoreboard.update_scoreboard() 
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if 330 < ball.xcor() < 350 and r_paddle.ycor() - 60 < ball.ycor() < r_paddle.ycor() + 60:
        ball.setx(320)
        ball.bounce_x()

    if -350 < ball.xcor() < -330 and l_paddle.ycor() - 60 < ball.ycor() < l_paddle.ycor() + 60:
        ball.setx(-320)
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()