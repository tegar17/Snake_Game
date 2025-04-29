from time import sleep
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,250)
        self.color("white")
        self.score = -1
        self.show_incrace()
        self.hideturtle()

    def show_incrace(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 20, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=('Arial', 20, 'bold'))




