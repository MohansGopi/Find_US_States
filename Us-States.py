import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S states guess')
image = 'blank_states_img.gif'
turtle.bgpic(picname=image)
turtle.penup()
turtle.hideturtle()

is_game_on = True

count_states = 0

answer_list = []

while is_game_on:
    turtle.goto(10,100)
    answer = screen.textinput(title=f'{count_states}/50 states',prompt='Fine another State?')

    print(answer)

    us_states_data = pd.read_csv('50_states.csv')

    states = us_states_data['state']
    us_state_list =[]

    for state in states:
        us_state_list.append(state.lower())

    if answer.lower() == 'exit':
        break

    if answer.lower() in us_state_list:
        answer_list.append(answer)
        answer_x_y = us_states_data[us_states_data.state == answer.title()]
        x = answer_x_y['x']
        y = answer_x_y['y']
        turtle.setposition(x=int(x),y=int(y))
        turtle.write(answer)
        count_states +=1


missed_state = []

for state in us_state_list:
    if state not in answer_list:
        missed_state.append(state)

missed_dict = {
    'missed_states': missed_state
}

missed_df = pd.DataFrame(missed_dict)

missed_df.to_csv('missed_states.csv')