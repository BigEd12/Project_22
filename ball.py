from turtle import Turtle, Screen
import time
screen = Screen()
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        screen.tracer(1)
        self.speed("slowest")
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def new_start(self):
        screen.tracer(0)
        self.goto((0, 0))
        screen.update()
        self.x_move *= -1
