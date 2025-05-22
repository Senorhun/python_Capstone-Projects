import pandas
import turtle
import time

data = pandas.read_csv("State_quiz/50_states.csv")
data_list = data["state"].to_list()


screen = turtle.Screen()
image = "State_quiz/blank_states_img.gif"
screen.setup(width=725, height=500)
screen.bgpic(image)
screen.title("USA states quiz game")
guessed_states = []

message = turtle.Turtle()
message.color("green")
message.penup()
message.hideturtle()
message.goto(0,0)

text = turtle.Turtle()
text.hideturtle()
text.penup()
faulty_tipps = 5
for i in range(len(data_list) + faulty_tipps):
    user_input = screen.textinput(title=f"Guessing states {len(guessed_states)}/50", prompt="Guess state's name: ").title()
    if user_input in guessed_states:
        continue
    if user_input in data_list:
        state_data = data[data["state"] == user_input]
        text_x = int(state_data["x"])
        text_y = int(state_data["y"])
        text.goto(text_x,text_y)
        text.write(user_input, align="center", font=("Arial", 10, "normal"))
        guessed_states.append(user_input)
    if len(guessed_states) == 50 or user_input == "Exit":
        message.write("Thanks for participate!", align="center", font=("Arial", 20, "normal"))
        time.sleep(1.5)
        break

states_to_learn = []
for state in data_list:
    if state not in guessed_states:
        states_to_learn.append(state)
states_to_learn_df = pandas.DataFrame(states_to_learn, columns=["STATES YOU MISSED"])
states_to_learn_df.to_csv("State_quiz/states_to_learn.csv", index=False)

