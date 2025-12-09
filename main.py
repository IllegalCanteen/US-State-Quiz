import turtle
from turtle import Turtle

import pandas
screen=turtle.Screen()
screen.title("US State Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states=[]
data=pandas.read_csv("50_states.csv")
data_list=data.state.to_list()
while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 states guessed",prompt="Guess another state").title()
    if answer_state=="Exit":
        missing_states=[state for state in data_list if state not in guessed_states]
        missing_states_data=pandas.DataFrame(missing_states)
        missing_states_data.to_csv("states_to_learn.csv")
        break
    if answer_state in data_list and  answer_state not  in guessed_states:
        guessed_states.append(answer_state)
        t=Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)

turtle.mainloop()
