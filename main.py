
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=800)
screen.title('Ping Pong')
screen.tracer(0)

# create paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# create ball
ball = Ball()

# create scoreboard
scoreboard = Scoreboard()


screen.listen()

# control right paddle
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')

# control left paddle
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')


game_over = True

while game_over:

    game_is_on = True

    while game_is_on:
        time.sleep(0.1)

        ball.move()

        # detect collision with wall top and bottom
        if ball.ycor() >= 385 or ball.ycor() <= -385:
            ball.bounce_y()

        # detect collision with wall right and left
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # detect point for left gamer
        if ball.xcor() > 380:
            game_is_on = False
            scoreboard.addscore(False)
            ball.restart_position()
            l_paddle.restart_position()
            r_paddle.restart_position()

        # detect point for right gamer
        elif ball.xcor() < - 380:
            game_is_on = False
            scoreboard.addscore(True)
            ball.restart_position()
            l_paddle.restart_position()
            r_paddle.restart_position()

        screen.update()

    # game over
    if scoreboard.score_l >= 5 or scoreboard.score_r >= 5:
        scoreboard.game_over()
        break

    time.sleep(2)


screen.exitonclick()
