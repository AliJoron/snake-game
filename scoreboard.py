from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.readata()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Hight Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.wridata()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def readata(self):
        with open('data.txt', mode='r') as data:
            content = data.read()
        return int(content)

    def wridata(self):
        with open('data.txt', mode='w') as data:
            data.write(f"{self.highscore}")

