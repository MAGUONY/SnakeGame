from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.sety(270)

    def showScore(self):
        self.write(f"Score: {self.score}", False, "center", ("Times New Roman", 20, "normal"))

    def addScore(self):
        self.score += 1
        self.clear()

    def gameOver(self):
        self.sety(0)
        self.write("Game Over!", False, "center", ("Times New Roman", 30, "normal"))