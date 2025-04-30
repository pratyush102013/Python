from turtle import Turtle

class Paddles(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x=x_position, y=y_position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)
