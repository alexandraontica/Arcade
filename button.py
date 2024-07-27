from turtle import Turtle
from turtle_race_game.turtle_race import play_turtle_race
from pong_game.pong import play_pong
from snake_game.snake_game import play_snake_game
from turtle_crossing_game.turtle_crossing import play_turtle_crossing_game

GAMES = [play_snake_game, play_pong, play_turtle_crossing_game, play_turtle_race]
FONT_SIZE = 15
FONT = ('Courier', FONT_SIZE, 'bold')
ALIGNMET = "center"

class Button(Turtle):
    def __init__(self, game_num, game_name, color, position, screen):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_len=9.5, stretch_wid=2.5)
        self.pensize(50)
        self.color(color)
        self.fillcolor("")
        self.penup()
        self.goto(position)
        self.showturtle()
        self.text = Turtle()
        self.write_text(position, game_name)
        self.game_num = game_num
        self.game_screen = screen

    def write_text(self, position, game_name):
        self.text.penup()
        self.text.color("white")
        self.text.hideturtle()
        self.text.goto(position[0], position[1] - FONT_SIZE)
        self.text.write(game_name, align=ALIGNMET, font=FONT)

    def on_click(self, x, y):
        self.screen.clear()
        GAMES[self.game_num](self.game_screen)
             