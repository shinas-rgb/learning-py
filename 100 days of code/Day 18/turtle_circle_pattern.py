import turtle as t

tim = t.Turtle()
tim.pencolor("blue")
tim.speed("fastest")
for _ in range(40):
    tim.circle(100)
    tim.right(10)



screen = t.Screen()
screen.exitonclick()