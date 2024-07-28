from snake_game.snake import Snake
from snake_game.border import Border
from snake_game.food import Food
from snake_game.scoreboard import ScoreBoard
import time

def play_snake_game(screen):
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.bgpic("nopic")
    screen.title("Snake")
    screen.tracer(0)

    border = Border()
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.segments[0].distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # detect collision with wall
        if border.hit_border(snake.segments[0].xcor(), snake.segments[0].ycor()):
            scoreboard.reset()
            snake.reset()

        # detect collision with tail
        for segment in snake.segments[1:]:
            if snake.segments[0].distance(segment) < 10:
                scoreboard.reset()
                snake.reset()
