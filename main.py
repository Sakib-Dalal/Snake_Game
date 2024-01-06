""" Code Written by Sakib Dalal, GitHub:- https://github.com/Sakib-Dalal"""

import turtle
import time

screen = turtle.Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_pos = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []
for i in range(len(snake_pos)):
    snake = turtle.Turtle()
    snake.penup()
    snake.color("white")
    snake.shape("square")
    snake.goto(snake_pos[i])
    snake_segments.append(snake)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.2)

    for seg_num in range(len(snake_segments) - 1, 0, -1):
        new_x = snake_segments[seg_num - 1].xcor()
        new_y = snake_segments[seg_num - 1].ycor()
        snake_segments[seg_num].goto(x=new_x, y=new_y)
    snake_segments[0].forward(20)

screen.exitonclick()
