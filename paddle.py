from turtle import Turtle


class Paddle(Turtle):
    """
    example:\n
    position = (0,0)
    """

    def __init__(self, position):
        super().__init__()
        self.position_start = position
        self.create()

    def create(self):
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(self.position_start)

    def restart_position(self):
        self.goto(self.position_start)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
