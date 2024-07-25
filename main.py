import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
location = turtle.Turtle()
location.hideturtle()
location.penup()


data = pandas.read_csv("50_states.csv")
correct_guess = []


game_is_on = True
while len(correct_guess) < 30:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 Correct States", prompt="What's the another states name?")
    guess = answer_state.title()
    if guess == "Exit":

        res= [states for states in data["state"].to_list() if states not in correct_guess]
        states_dict = {"states": res}
        learn_data = pandas.DataFrame(states_dict)
        learn_data.to_csv("states_to_learn.csv")
        break


    if guess in data["state"].to_list():
        row_state = data[data["state"] == guess]
        location.setposition(int(row_state.x), int(row_state.y))
        location.write(guess, align="center")
        correct_guess.append(guess)
