from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt", mode="r") as highScore:
            self.highScore = int(highScore.read())

        self.color("white")
        self.penup()
        self.hideturtle()
        self.sety(270)
        self.showScore()

    def showScore(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highScore}", False, "center", ("Times New Roman", 20, "normal"))

    def addScore(self):
        self.score += 1
        self.clear()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", mode="w") as highScore:
                self.highScore = highScore.write(str(self.score))


        self.score = 0
        self.showScore()

    # def gameOver(self):
    #     self.sety(0)
    #     self.write("Game Over!", False, "center", ("Times New Roman", 30, "normal"))