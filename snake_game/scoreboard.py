from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.__score = 0
        with open("snake_game/data.txt") as highscore:
            self.__high_score = int(highscore.read())
        self.color("white")
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.__score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.__score}  High score: {self.__high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.__score > self.__high_score:
            self.__high_score = self.__score
            with open("snake_game/data.txt", "w") as highscore:
                highscore.write(f"{self.__high_score}")
        self.__score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)