from turtle import Screen
from button import Button

SNAKE = 0
PONG = 1
CROSS = 2
RACE = 3

screen = Screen()
screen.setup(width=810, height=900)
screen.bgpic("assets/arcade-game.gif")
screen.tracer(0)

snake_game_button = Button(game_num=SNAKE, game_name="Snake", color="red", position=(-110, 50), screen=screen)
snake_game_button.onclick(snake_game_button.on_click)

pong_button = Button(game_num=PONG, game_name="Pong", color="blue", position=(110, 50), screen=screen)
pong_button.onclick(pong_button.on_click)

cross_button = Button(game_num=CROSS, game_name="Turtle Crossing", color="yellow", position=(-110, -70), screen=screen)
cross_button.onclick(cross_button.on_click)

race_button = Button(game_num=RACE, game_name="Turtles Race", color="green", position=(110, -70), screen=screen)
race_button.onclick(race_button.on_click)

screen.update()

screen.exitonclick()
