import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

loop = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if loop % 6 == 0:
        car_manager.create_cars()

    car_manager.move_car()
    loop += 1

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()
