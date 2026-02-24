from turtle import Turtle
ALIGTGNMENT= "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGTGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGTGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()