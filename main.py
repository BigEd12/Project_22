from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

scoreboard = Scoreboard()

screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_paddle()
    #detect point
    if ball.xcor() > 370:
        ball.new_start()
        scoreboard.l_point()

    if ball.xcor() < -370:
        ball.new_start()
        scoreboard.r_point()





screen.exitonclick()