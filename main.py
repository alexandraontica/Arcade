from turtle import Screen
from button import Button

GAMES = [
    {"game_num": 0, "name": "Snake", "color": "red", "position": (-110, 50)},
    {"game_num": 1, "name": "Pong", "color": "blue", "position": (110, 50)},
    {"game_num": 2, "name": "Turtle Crossing", "color": "yellow", "position": (-110, -70)},
    {"game_num": 3, "name": "Turtles Race", "color": "green", "position": (110, -70)},
]

screen = Screen()
screen.setup(width=810, height=900)
screen.title("PyArcade")
screen.bgpic("assets/arcade-game.gif")
screen.tracer(0)

buttons = []
for game in GAMES:
    button = Button(game_num=game["game_num"], game_name=game["name"], color=game["color"], position=game["position"], screen=screen)
    button.onclick(button.on_click)
    buttons.append(button)

screen.update()
screen.exitonclick()
