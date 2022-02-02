from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

# controls
screen.listen()
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

# so the game instantly updates after each input

ball_speed_modifier = .1
gaming = True
while gaming:
    time.sleep(ball_speed_modifier)
    screen.update()
    ball.move()

    # detect collision with ceiling or floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # paddle collision
    if ball.distance(right_paddle) < 50 and ball.xcor() > 280:
        ball.paddle_bounce()
        ball_speed_modifier *= .95

    if ball.distance(left_paddle) < 50 and ball.xcor() < -280:
        ball.paddle_bounce()
        ball_speed_modifier *= .95

    # scoring and resetting
    if ball.xcor() > 330:
        scoreboard.left_point()
        scoreboard.clear()
        scoreboard.update_score()
        ball_speed_modifier = .1
        time.sleep(2)
        ball.goto(0, 0)
        screen.update()
        time.sleep(1)
        ball.paddle_bounce()
        ball.move()

    elif ball.xcor() < -330:
        scoreboard.right_point()
        scoreboard.clear()
        scoreboard.update_score()
        ball_speed_modifier = .1
        time.sleep(2)
        ball.goto(0, 0)
        screen.update()
        time.sleep(1)
        ball.paddle_bounce()
        ball.move()

screen.exitonclick()
