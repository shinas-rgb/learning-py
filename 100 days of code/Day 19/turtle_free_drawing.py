from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.pencolor("black")
def forward():
    tim.fd(10)

def backward():
    tim.bk(10)

def left():
    tim.left(10)

def right():
    tim.right(10)

def clear():
    tim.clear()
    tim.home()

screen.listen()
#screen.onkey(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="d", fun=right)
screen.onkeypress(key="a", fun=left)
screen.onkeypress(key="c", fun=clear)
screen.onkeypress(key="w", fun=forward)





screen.exitonclick()