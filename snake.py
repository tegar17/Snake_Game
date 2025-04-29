from turtle import Turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
import random
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]
        self.rand_col = ""

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_turtle(position)

    def move(self):
        for turtle_num in range(len(self.all_turtle)-1, 0, -1):
            new_x = self.all_turtle[turtle_num - 1].xcor()
            new_y = self.all_turtle[turtle_num - 1].ycor()

            self.all_turtle[turtle_num].goto(new_x, new_y)

        rand_color = random.choice(colors)
        self.rand_col = rand_color

        for i in range(len(self.all_turtle)):
            self.all_turtle[i].color(self.rand_col)

        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_turtle(self, position):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.all_turtle.append(turtle)

    def extend(self):
        self.add_turtle(self.all_turtle[-1].position())
        self.all_turtle[-1].color(self.rand_col)

