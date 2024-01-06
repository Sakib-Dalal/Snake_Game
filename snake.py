import turtle

SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(len(SNAKE_POSITIONS)):
            snake = turtle.Turtle()
            snake.penup()
            snake.color("white")
            snake.shape("square")
            snake.goto(SNAKE_POSITIONS[i])
            self.snake_segments.append(snake)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(x=new_x, y=new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)
