import pandas
import turtle

data = pandas.read_csv("State_quiz/50_states.csv")
data_list = data["state"].to_list()
print(data_list)

screen = turtle.Screen()
image = "State_quiz/blank_states_img.gif"
screen.bgpic(image)
screen.title("USA states quiz game")

guessed_states = []

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0,-200)

for i in range(2):
    user_input = screen.textinput(title=f"Guessing states {len(guessed_states)}/50", prompt="Guess state's name: ")
    if user_input in data_list:
        text.write("Success")
        guessed_states.append(user_input)

screen.exitonclick()