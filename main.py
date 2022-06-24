import pandas as pd
import turtle
from turtle import Screen
from naming_countries import Naming

data = pd.read_csv('50_states.csv')
states = str(data.state)
c = 0
states_said = []
all_states = data.state.to_list()

screen = Screen()
screen.title("U.S States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

while c < 50:
    answer_state = screen.textinput(title=f"U.S States {c}/50", prompt="Type a state. ")
    answer_state = answer_state.title()
    if answer_state == 'Exit':
        missing_state = []
        for state in all_states:
            if state not in states_said:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        print(new_data)
        break
    if answer_state in states_said:
        print("State already said")
    elif answer_state in all_states:
        states_said.append(answer_state)
        pos = data[data.state == answer_state]
        pos_x = int(pos['x'])
        pos_y = int(pos['y'])
        Naming(pos_x, pos_y, answer_state)
        c += 1

if c == 50:
    print("Congratulations, you got all 50 states!")

turtle.mainloop()