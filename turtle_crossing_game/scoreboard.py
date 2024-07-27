from turtle import Turtle

FONT = ("Courier", 24, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.__score = 1
        self.goto(-215, 260)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.__score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.__score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        