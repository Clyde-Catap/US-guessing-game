import turtle
import pandas
from country_turtles import State_turtle
from Scoreboard import Scoreboard
import time

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
screen.addshape(image)

turtle.shape(image)


data_countries = list(data["state"])

FONT = ("Courier", 18, "bold")

scoreboard = Scoreboard()
score = 0

guessed = []

guessed_states = []


while len(guessed) < 50:

    scoreboard.write(arg=f"Score:{score}/50", align="center", move=False, font=FONT)
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").lower()
    guessed.append(answer_state)
    count = 0

    if answer_state == "exit":
        break

    for state in data["state"]:
        if answer_state.lower() == state.lower():
            for g in answer_state:
                if g == " ":
                    count += 1
            if count == 0:
                data_xcor = int(data[data["state"] == f"{answer_state.capitalize()}"]["x"])
                data_ycor = int(data[data["state"] == f"{answer_state.capitalize()}"]["y"])
                guessed_states.append(answer_state.capitalize())
            else:
                z = []
                ww = answer_state.split()
                for w in ww:
                    xww = w.capitalize()
                    z.append(xww)
                answer_state = " ".join(z)
                guessed_states.append(answer_state)
                data_xcor = int(data[data["state"] == f"{answer_state}"]["x"])
                data_ycor = int(data[data["state"] == f"{answer_state}"]["y"])
            for state in data["state"]:
                if answer_state.lower() == state.lower():
                    tortle = State_turtle()
                    tortle.goto(data_xcor, data_ycor)
                    if count==0:
                        tortle.write(arg=f"{answer_state.capitalize()}", move=False, align="center", font="calibri")
                    else:
                        tortle.write(arg=f"{answer_state}", move=False, align="center", font="calibri")
                    scoreboard.clear()
                    score += 1

over = turtle.Turtle()
over.color("black")
over.penup()
over.hideturtle()
over.write(arg=f"Game Over", align="center", move=False, font=FONT)


# save as as csv
unguessed_states = []

for www in guessed_states:
    data_countries.remove(www)


missed_coutries = pandas.DataFrame(data_countries)
missed_coutries.to_csv("missed_countries.csv")

# print(data_countries)



screen.exitonclick()



