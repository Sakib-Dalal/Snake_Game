""" Code Written by Sakib Dalal, GitHub:- https://github.com/Sakib-Dalal"""

import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = turtle.Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_segments = []

snake = Snake()
food = Food()
score = Score()

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

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh_score()
        snake.extend()

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_high_score()
        snake.reset()

    # Detect Collision with tail
    for segment in snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_high_score()
            snake.reset()

screen.exitonclick()
