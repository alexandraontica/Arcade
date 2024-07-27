from turtle import Turtle

X_COORD = 380
Y_COORD = 280

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-400, 300)
        self.pendown()
        self.color("white")
        self.pensize(3)

        for _ in range(2):
            self.forward(800)
            self.right(90)
            self.forward(600)
            self.right(90)

        self.hideturtle()
        self.penup()
        self.goto(-400, 400)

    def hit_top_or_bottom_border(self, y):
        if y > Y_COORD or y < -Y_COORD:
            return True
        return False
    
    def hit_right_border(self, x):
        if x > X_COORD:
            return True
        return False
    
    def hit_left_border(self, x):
        if x < -X_COORD:
            return True
        return False