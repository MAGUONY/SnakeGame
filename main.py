from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

theScreen = Screen()
theScreen.setup(width=600, height=600)
theScreen.bgcolor("black")
theScreen.title("The Snake Game")
theScreen.tracer(0)

theSnake = Snake()
theFood = Food()
theScore = Scoreboard()

theScreen.listen()
theScreen.onkeypress(theSnake.up, "Up")
theScreen.onkeypress(theSnake.down, "Down")
theScreen.onkeypress(theSnake.left, "Left")
theScreen.onkeypress(theSnake.right, "Right")

keepPlaying = True

while keepPlaying:
    theScreen.update()
    time.sleep(0.1)

    theSnake.move()
    theScore.showScore()

    # Detect collision with the food
    if theSnake.theHead.distance(theFood) < 15:
        theFood.refresh()
        theSnake.extend()
        theScore.addScore()

    # Detect collision with a wall
    if theSnake.theHead.xcor() > 280 or theSnake.theHead.xcor() < -280 or theSnake.theHead.ycor() > 280 or theSnake.theHead.ycor() < -280:
        theScore.reset()
        theSnake.reset()

    # Detect collision with tail
    for bodyParts in theSnake.theTurtles[1:]:  # Slicing to start checking the body parts not including the head
        if bodyParts == theSnake.theHead:
            pass

        elif theSnake.theHead.distance(bodyParts) < 10:
            theScore.reset()
            theSnake.reset()


theScreen.exitonclick()
