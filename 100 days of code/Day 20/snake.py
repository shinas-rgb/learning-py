from turtle import Turtle, Screen
import time
from food import Food
from score import Score

class Snake:

    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.direction = "right"
        self.game_is_on = True
        self.food = Food()
        self.score = Score()
        self.pen = Turtle()
        self.rt = Turtle()
        self.screen_text()

    def screen_text(self):
        screen.tracer(0)
        self.pen.goto(-150, 250)
        self.pen.color("blue")
        self.pen.clear()
        self.pen.write(f"Score: {self.score.score} High Score: {self.score.highScore}", font= ("Arial", 20, "bold"))
        self.pen.hideturtle()
        screen.update()

    def create_snake(self):
        for i in self.starting_positions:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.speed(1)
            new_segment.goto(i)
            self.segments.append(new_segment)

    def move(self):
        self.segments[0].speed(7)
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].fd(20)
        if self.segments[0].distance(self.food.food) < 15:
            self.food.new_food()
            self.score.new_score()
            self.screen_text()
            last_pos = self.segments[-1].position()
            new_segment = Turtle("square")
            new_segment.goto(last_pos)
            new_segment.color("white")
            new_segment.penup()
            self.segments.append(new_segment)
        if self.segments[0].xcor() > 300 or self.segments[0].ycor() > 300 or self.segments[0].xcor() < -300 or self.segments[0].ycor() < -300:
            self.score.high_score()
            snake.retry()
            return False
        for seg in self.segments[1:]:
            if self.segments[0].distance(seg) < 10:
                self.score.high_score()
                snake.retry()
                return False
        return True

    def left(self):
        if self.direction == "up":
            self.segments[0].left(90)
            self.direction = "left"
        elif self.direction == "down":
            self.segments[0].right(90)
            self.direction = "left"

    def right(self):
        if self.direction == "up":
            self.segments[0].right(90)
            self.direction = "right"
        elif self.direction == "down":
            self.segments[0].left(90)
            self.direction = "right"

    def up(self):
        if self.direction == "left":
            self.segments[0].right(90)
            self.direction = "up"
        elif self.direction == "right":
            self.segments[0].left(90)
            self.direction = "up"

    def down(self):
        if self.direction == "right":
            self.segments[0].right(90)
            self.direction = "down"
        elif self.direction == "left":
            self.segments[0].left(90)
            self.direction = "down"

    def retry(self):
        self.score.score = 0
        self.rt.color("white")
        self.rt.write("Press \"r\" to retry", font= ("Arial", 20, "bold"), align= "center")
        screen.onkey(key="r", fun=snake.retry_yes)
        screen.listen()

    def retry_yes(self):
        for seg in self.segments:
            seg.hideturtle()
            seg.clear()
        self.segments = []
        self.game_is_on = True
        self.score.score = 0
        self.food.new_food()

        self.rt.clear()
        self.rt.hideturtle()

        self.create_snake()
        self.direction = "right"
        self.screen_text()

        self.run_game()

    def run_game(self):
        self.game_is_on = True
        while self.game_is_on:
            self.game_is_on = self.move()
            screen.update()
            time.sleep(.1)
        self.retry()


screen = Screen()
screen.setup(width= 600, height= 600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(1)

snake = Snake()
screen.listen()
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)

game_is_on = True
while game_is_on:
    game_is_on = snake.move()
    screen.update()
    time.sleep(.1)

game_is_on = True
snake.retry()

screen.mainloop()

