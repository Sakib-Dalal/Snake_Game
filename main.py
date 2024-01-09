""" Code Written by Sakib Dalal, GitHub:- https://github.com/Sakib-Dalal"""

import turtle
import time
from snake import Snake
from food import Food


screen = turtle.Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_segments = []

snake = Snake()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
