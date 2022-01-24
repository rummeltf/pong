from turtle import Turtle
move_dist = 15

class Paddle(Turtle):

    # initial settings of the paddles
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    # move the paddle up an increment
    def up(self):
        x_cor = self.xcor()
        new_y = self.ycor() + move_dist
        if new_y >= 240:
            self.goto(x_cor, 240)
        else:
            self.goto(x_cor, new_y)

    # move the paddle down an increment
    def down(self):
        x_cor = self.xcor()
        new_y = self.ycor() - move_dist
        if new_y <= -240:
            self.goto(x_cor, -240)
        else:
            self.goto(x_cor, new_y)
