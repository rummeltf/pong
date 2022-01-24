from turtle import Screen
from paddles import Paddle
from ball import Ball
import time

#initial setup of game screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# initializing game elements
left_paddle = Paddle((-300, 0))
right_paddle = Paddle((300, 0))
ball = Ball()

# controls
screen.listen()
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

# so the game instantly updates after each input
gaming = True
while gaming:
    time.sleep(.1)
    screen.update()
    ball.move()

screen.exitonclick()
