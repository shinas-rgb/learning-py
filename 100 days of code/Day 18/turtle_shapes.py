import turtle as t

tim = t.Turtle()
tim.speed(1)
colors = ["red", "green", "blue", "yellow", "brown"]
sides = 4
tim.backward(50)
for i in range(0, 5):
    tim.pencolor(colors[i])
    for j in range(0, sides):
        tilt = 360 / sides
        tim.forward(100)
        tim.right(tilt)
    sides += 1




screen = t.Screen()
screen.exitonclick()