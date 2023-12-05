from turtle import Screen


from player import Player
from car_manager import CarManager
from score_board import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=800)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()

screen.onkey(player.go_up, "Up")
game_is_on = True
while game_is_on:
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

#     detect collision with car
for car in car_manager.all_cars:
    if car.distance(player) < 20:
        game_is_on = False
        scoreboard.game_over()
#     detect successful collision
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


# player = Turtle()
# player.shape("turtle")
# player.penup()
# player.goto(0, -350)
# player.setheading(90)

screen.exitonclick()
