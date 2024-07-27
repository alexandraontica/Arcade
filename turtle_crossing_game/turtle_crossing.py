import time
from turtle_crossing_game.player import Player
from turtle_crossing_game.car_manager import CarManager
from turtle_crossing_game.scoreboard import Scoreboard

def play_turtle_crossing_game(screen):
    screen.setup(width=600, height=600)
    screen.bgcolor("white")
    screen.bgpic("nopic")
    screen.title("Turtle Crossing Game")
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.go_up, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(car_manager.move_speed)
        screen.update()
        car_manager.move_cars()
        car_manager.hide_old_cars()

        # detect collision with cars:
        for car in car_manager.cars:
            if player.distance(car) < 20:
                game_is_on = False
                scoreboard.game_over()

        if player.reached_top():
            scoreboard.increase_score()
            player.reset()
            car_manager.increase_car_speed()
