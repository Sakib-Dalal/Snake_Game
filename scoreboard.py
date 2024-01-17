from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data_file:
            data = data_file.read()
            self.highscore = int(data)
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"🏁Score 🐍: {self.score} High Score: {self.highscore}", False, ALIGN, FONT)

    def refresh_score(self):
        self.score += 1
        self.update_score()

    def reset_high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data_file:
                data_file.write(str(self.highscore))
        self.score = 0
        self.update_score()
