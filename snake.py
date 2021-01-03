from turtle import Turtle

TURTLES_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.theTurtles = []
        self.createSnake()
        self.theHead = self.theTurtles[0]

    def createSnake(self):
        for position in TURTLES_POSITIONS:
            self.addBody(position)

    def addBody(self, position):
        newTurtle = Turtle("square")
        newTurtle.color("white")
        newTurtle.penup()
        newTurtle.goto(position)
        self.theTurtles.append(newTurtle)

    def move(self):
        for turtleNum in range(len(self.theTurtles) - 1, 0, -1):  # start stop step
            theNewX = self.theTurtles[turtleNum - 1].xcor()
            theNewY = self.theTurtles[turtleNum - 1].ycor()
            self.theTurtles[turtleNum].goto(theNewX, theNewY)

        self.theHead.forward(MOVE_DISTANCE)

    def extend(self):
        # add a piece to the body of the snake
        self.addBody(self.theTurtles[-1].position())

    def up(self):
        if self.theHead.heading() != DOWN:
            self.theHead.setheading(UP)

    def down(self):
        if self.theHead.heading() != UP:
            self.theHead.setheading(DOWN)

    def left(self):
        if self.theHead.heading() != RIGHT:
            self.theHead.setheading(LEFT)

    def right(self):
        if self.theHead.heading() != LEFT:
            self.theHead.setheading(RIGHT)

    def reset(self):
        for bodyparts in self.theTurtles:
            bodyparts.goto(1000, 1000)

        self.theTurtles.clear()
        self.createSnake()
        self.theHead = self.theTurtles[0]