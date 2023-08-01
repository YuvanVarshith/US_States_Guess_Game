import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
state_list = state_data["state"].to_list()
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 State Correct", prompt="Whats another state name?").title()
    if answer_state in guessed_state:
        pass
    elif answer_state == "Exit":
        not_guessed_state = []
        for state in state_list:
            if state not in guessed_state:
                not_guessed_state.append(state)
        new_data = pandas.DataFrame(not_guessed_state)
        new_data.to_csv("states_to_learn.csv")
        break
    else:
        if answer_state in state_list:
            guessed_state.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            user_state = state_data[state_data.state == answer_state]
            t.goto(int(user_state.x), int(user_state.y))
            t.write(answer_state)



screen.exitonclick()
