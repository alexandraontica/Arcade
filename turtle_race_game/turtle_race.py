from turtle import Turtle
import random

ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")

def play_turtle_race(screen):
    screen.setup(width=500, height=400)
    screen.bgpic("nopic")
    screen.title("Turtle Race")

    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.setheading(270)
    finish_line.goto(250, 200)
    finish_line.pendown()
    finish_line.goto(250, -200)

    prompt = Turtle()
    prompt.hideturtle()
    
    is_race_on = False

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    turtles = []

    for turtle_index in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=-70 + 30 * turtle_index)
        turtles.append(new_turtle)

    user_bet = None
    while user_bet not in colors:
        user_bet = screen.textinput(
            title="Make your bet", 
            prompt="Which turtle will win the race (red, orange, yellow, green, blue, purple)? Enter a color: "
        )
        if user_bet is None:
            break

    if user_bet:
        is_race_on = True
    else:
        prompt.write("Race cancelled", align=ALIGNMENT, font=FONT)
        return

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False

                winning_color = turtle.pencolor()

                if winning_color == user_bet:
                    prompt.write(f"You've won! The {winning_color} turtle is the winner!", align=ALIGNMENT, font=FONT)
                else:
                    prompt.write(f"You've lost! The {winning_color} turtle is the winner!", align=ALIGNMENT, font=FONT)

            turtle.forward(random.randint(0, 10))

    for turtle in turtles:
        turtle.hideturtle()
