from turtle import Turtle

FONT = ("Arial", 16, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.Og_score()

    def Og_score(self):
        self.pu()
        self.hideturtle()
        self.goto(-200,260)
        self.write(f"Level: {self.score}",align="right",font=FONT)

    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.write("GAME OVER!",align="center",font=FONT)

    def score_up(self):
        self.clear()
        self.score+=1
        self.Og_score()



