from time import sleep
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,250)
        self.color("white")
        self.score = 0
        with open("data.txt") as file:
            high_score = int(file.read())
        self.high_score = high_score
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        with open("data.txt") as file:
            high_score = int(file.read())
        self.high_score = high_score
        self.clear()
        self.penup()
        self.write(f"Score: {self.score}", move=False,align=("right"), font=('Arial', 20, 'bold'))
        self.write(f"  High Score:{self.high_score}", move=False,align="left",font=('Arial', 20, 'bold'))


    def reset(self):
        if self.score > self.high_score:
            with open("data.txt",mode="w") as f:
                f.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()