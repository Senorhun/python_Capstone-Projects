import pandas
import turtle

data = pandas.read_csv("State_quiz/50_states.csv")


screen = turtle.Screen()
image = "State_quiz/blank_states_img.gif"
screen.bgpic(image)
screen.title("USA states quiz game")
screen.textinput(title="Guessing states", prompt="Guess state's name: ")
screen.exitonclick()