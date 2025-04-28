from turtle import Turtle
THE_COORDINATES = [(-20, 0), (-40, 0), (0, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.speed("fastest")

    def add_segment(self, position):
        new_segments = Turtle("square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def create_snake(self):
        for position in THE_COORDINATES:
            self.add_segment(position)

    def move(self):
        for num_seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[num_seg-1].xcor()
            new_y = self.segments[num_seg-1].ycor()
            self.segments[num_seg].goto(x=new_x, y=new_y)
        self.head.fd(MOVE_DISTANCE)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)