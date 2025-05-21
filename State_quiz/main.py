import pandas
import turtle

data = pandas.read_csv("State_quiz/50_states.csv")
data_list = data["state"].to_list()


screen = turtle.Screen()
image = "State_quiz/blank_states_img.gif"
screen.bgpic(image)
screen.title("USA states quiz game")

guessed_states = []

text = turtle.Turtle()
text.hideturtle()
text.penup()

for i in range(len(data_list)):
    user_input = screen.textinput(title=f"Guessing states {len(guessed_states)}/50", prompt="Guess state's name: ").capitalize()
    if user_input in data_list:
        state_data = data[data["state"] == user_input]
        text_x = int(state_data["x"])
        text_y = int(state_data["y"])
        text.goto(text_x,text_y)
        text.write(user_input, align="center", font=("Arial", 10, "normal"))
        guessed_states.append(user_input)

screen.exitonclick()