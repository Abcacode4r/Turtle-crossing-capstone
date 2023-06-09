from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.create_car()


    def create_car(self):
        car=Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.pu()
        car.ycor = random.randint(-240, 250)
        car.goto(300, car.ycor)
        self.all_cars.append(car)


    def move_car(self):
        for car in self.all_cars:
            car.setheading(180)
            car.fd(STARTING_MOVE_DISTANCE)



