from turtle import Turtle

COORD = 280

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-300, 300)
        self.pendown()
        self.color("white")
        self.pensize(3)

        for _ in range(4):
            self.forward(600)
            self.right(90)

        self.hideturtle()
        self.penup()
        self.goto(-400, 400)

    def hit_border(self, snake_x, snake_y):
        if snake_x > COORD or snake_x < -COORD or snake_y > COORD or snake_y < -COORD:
            return True
        return False