from turtle import Turtle


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.color("red")
        self.shapesize(100)
        self.penup()
        self.hideturtle()
        self.goto(x=-270, y=200 )
        # self.write(arg="Score:", align="center", move=False, font="calibri")