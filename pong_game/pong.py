from pong_game.paddle import Paddle
from pong_game.border import Border
from pong_game.ball import Ball
from pong_game.scoreboard import Scoreboard
import time

def play_pong(screen):
    screen.bgcolor("black")
    screen.bgpic("nopic")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)

    border = Border()

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))

    ball = Ball()

    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # detect collision with wall
        if border.hit_top_or_bottom_border(ball.ycor()):
            ball.bounce_y()

        # detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # right player didn't catch the ball
        if border.hit_right_border(ball.xcor()):
            ball.reset_position()
            scoreboard.l_point()

        # left player didn't catch the ball
        if border.hit_left_border(ball.xcor()):
            ball.reset_position()
            scoreboard.r_point()

