from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

screen.listen()
food = Food()
snake = Snake(food)
scoreboard = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

try:
    with open("Snake_game/saved_score.txt") as file:
        content = file.read()
        scoreboard.best_score = int(content)
except FileNotFoundError:
    scoreboard.best_score = 0
scoreboard.refresh_scoreboard()

game_is_on = True
for i in range(3):
    snake.reset_snake()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            eaten_food_color = food.rgb
            food.relocate_food()
            scoreboard.increase_score()
            snake.extend(eaten_food_color)

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
screen.exitonclick()

with open("Snake_game/saved_score.txt", mode="w") as file:
    file.write(str(scoreboard.best_score))