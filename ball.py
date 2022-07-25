from turtle import Turtle, goto


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
        self.move_x = 10
        self.move_y = 10

    def create(self):
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y

        self.goto(new_x, new_y)

    def restart_position(self):
        self.move_x = 10
        self.move_y = 10
        self.goto(0,0)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1