""" Code Written by Sakib Dalal, GitHub:- https://github.com/Sakib-Dalal"""

import turtle
import time
from snake import Snake

screen = turtle.Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_pos = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []

snake = Snake()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

screen.exitonclick()
