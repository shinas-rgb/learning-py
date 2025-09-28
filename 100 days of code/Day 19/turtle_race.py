import turtle
from turtle import Turtle, Screen
import random
import sys

screen = Screen()
screen.setup(height= 400, width= 500)

tim1 = Turtle()
tim2 = Turtle()
tim3 = Turtle()
tim4 = Turtle()
tim5 = Turtle()

tim1.penup()
tim2.penup()
tim3.penup()
tim4.penup()
tim5.penup()

tim1.shape("turtle")
tim2.shape("turtle")
tim3.shape("turtle")
tim4.shape("turtle")
tim5.shape("turtle")

tim1.color("red")
tim1.goto(x= -230, y= 150)
tim2.color("yellow")
tim2.goto(x= -230, y= 75)
tim3.color("green")
tim3.goto(x= -230, y= 0)
tim4.color("purple")
tim4.goto(x= -230, y= -75)
tim5.color("orange")
tim5.goto(x= -230, y= -150)

speed_list = [5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 10, 3, 3, 3, 3, 4, 4, 4, 4, 1, 2, 2]

while 1:
    tim1.forward(random.choice(speed_list))
    tim2.forward(random.choice(speed_list))
    tim3.forward(random.choice(speed_list))
    tim4.forward(random.choice(speed_list))
    tim5.forward(random.choice(speed_list))
    if turtle.xcor() == 230:
        break
screen.exitonclick()