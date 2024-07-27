import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.iteration = 0
        self.move_speed = 0.1
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.penup()

        y = random.randint(-250, 250)
        new_car.goto(300, y)

        new_car.shape("square")
        new_car.shapesize(stretch_len=2, stretch_wid= 1)

        color = random.choice(COLORS)
        new_car.color(color)
        new_car.setheading(180)

        self.cars.append(new_car)

    def new_car(self):
        if self.iteration % 6 == 0:
            return True
        return False
    
    def move_cars(self):
        self.iteration += 1

        for car in self.cars:
            car.forward(self.move_distance)

        if self.new_car():
            self.create_car()

    def hide_old_cars(self):
        for car in self.cars:
            if car.xcor() <= -300:
                car.hideturtle()

    def increase_car_speed(self):
        self.move_speed *= 0.9
        self.move_distance *= 1.1