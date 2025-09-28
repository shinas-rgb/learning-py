from turtle import Turtle
import random

class Food:
    def __init__(self):
        self.food = Turtle("square")
        self.food.color("green")
        self.food.speed(0)
        self.food.penup()
        self.new_food()

    def new_food(self):
        new_x = random.randint(-14, 14) * 20
        new_y = random.randint(-14, 14) * 20
        self.food.goto(new_x, new_y)