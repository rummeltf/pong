from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.update_score()
    
    def update_score(self):
        self.goto(-100, 190)
        self.write(self.left_player_score, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 190)
        self.write(self.right_player_score, align="center", font=("Arial", 80, "normal"))

    def left_point(self):
        self.left_player_score += 1

    def right_point(self):
        self.right_player_score += 1