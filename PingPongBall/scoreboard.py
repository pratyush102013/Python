from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_scoreboard = 0
        self.r_scoreboard = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_scoreboard, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 200)
        self.write(self.r_scoreboard, align="center", font=("Courier", 80, "bold"))

    def l_point(self):
        self.l_scoreboard += 1
        self.update_score()

    def r_point(self):
        self.r_scoreboard += 1
        self.update_score()
