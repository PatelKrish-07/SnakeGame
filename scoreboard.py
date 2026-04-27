from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.high_score=int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.hideturtle()
        self.update()
    def update(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align="center", font=("Courier", 20, "normal"))

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.score))
        self.score=0
        self.update()


    def latest(self):
        self.score+=1
        self.update()

