from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"🏁Score 🐍: {self.score}", False, ALIGN, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME 🐍 OVER 😭.", False, ALIGN, FONT)

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.update_score()
