from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.pu()
        self.left(90)
        self.goto(0,-280)

    def move(self):
        self.fd(10)

    def finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        return False


