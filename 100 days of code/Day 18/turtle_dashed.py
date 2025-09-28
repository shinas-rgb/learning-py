import turtle as t

timmy = t.Turtle()
timmy.pencolor("black")
timmy.speed(1)
for i in range(0, 50):
    timmy.forward(5)
    if i % 5 == 0:
        timmy.penup()
        if i % 10 == 0:
            timmy.pendown()
    i += 1
screen = t.Screen()
screen.exitonclick()
