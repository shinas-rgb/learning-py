import turtle as t
import random

tim = t.Turtle()
colors = ["red", "yellow", "blue", "black", "pink", "orange", "brown", "green", "violet"]
tilts = [0, 90, 180, 270]
tim.speed(1)
tim.pensize(5)

for i in range(0, 50):
    tim.pencolor(random.choice(colors))
    tim.forward(50)
    tim.setheading(random.choice(tilts))

screen = t.Screen()
screen.exitonclick()