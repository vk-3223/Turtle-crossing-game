from turtle import Turtle,Screen
from player import Player
from car_maneger import Carmanger
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.bgcolor("pink")
player = Player()
car_manger = Carmanger()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_up,"8")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manger.creat_cars()
    car_manger.move_cars()
    for car in car_manger.all_cars:
        if car.distance(player)<20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_statrt()
        car_manger.level_up()        

screen.exitonclick()
