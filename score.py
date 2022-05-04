from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=('arial', 10, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align="center", font=('arial', 10, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()