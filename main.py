""" Code Written by Sakib Dalal, GitHub:- https://github.com/Sakib-Dalal"""

import turtle

screen = turtle.Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake_pos = [(0, 0), (-20, 0), (-40, 0)]
snake_body_list = []
for i in range(len(snake_pos)):
    snake = turtle.Turtle()
    snake.penup()
    snake.color("white")
    snake.shape("square")
    snake.goto(snake_pos[i])
    snake_body_list.append(snake)

screen.exitonclick()
