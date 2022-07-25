from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color('white')
        self.penup()
        self.goto(0, 365)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'{self.score_l} : {self.score_r}',align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.color('red')
        self.goto(0, 20)
        if self.score_r > self.score_l:
            self.write('WIN : RIGHT', align=ALIGNMENT, font=FONT)
        elif self.score_l > self.score_r:
            self.write('WIN : LEFT', align=ALIGNMENT, font=FONT)
        else:
            self.write('DRAW', align=ALIGNMENT, font=FONT)
        

    def addscore(self,gamer):
        """
        gamer = True     // right\n
        gamer = False    // left
        """
        
        if gamer:
            self.score_r += 1
        else:
            self.score_l += 1

        self.clear()
        self.update_scoreboard()
