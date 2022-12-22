from turtle import Turtle
import random
clors = ["red","orange","green","blue","purple"]
stating_move_distance  = 5
move_increment = 10

class Carmanger(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = stating_move_distance
    def creat_cars(self):
        random_chance = random.randint(1,6)
        if random_chance==1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choices(clors))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)    
    def level_up(self):
        self.car_speed += move_increment        