from turtle import Screen
from paddles import Paddle
from ball import Ball
import time

# initial setup of game screen
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
right__player_score = 0
left_player_score = 0
gaming = True
while gaming:
    time.sleep(.1)
    screen.update()
    ball.move()

    # detect collision with ceiling or floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # paddle collision
    if ball.distance(right_paddle) < 50 and ball.xcor() > 280:
        ball.paddle_bounce()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -280:
        ball.paddle_bounce()

    # scoring and resetting
    if ball.distance(right_paddle) > 50 and ball.xcor() > 300:
        left_player_score += 1
        time.sleep(2)
        ball.goto(0, 0)
        screen.update()
        time.sleep(1)
        ball.move()
    elif ball.distance(left_paddle) > 50 and ball.xcor() < -300:
        right__player_score += 1
        time.sleep(2)
        ball.goto(0, 0)
        screen.update()
        time.sleep(1)
        ball.move()

screen.exitonclick()
