from turtle import Turtle
FONT = ("Courier", 15, "italic")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.speed("fastest")
        self.previous_high_score()
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=FONT, align=ALIGN)

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT, align=ALIGN)

    def reset_game(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            self.record_high_score()
        self.score = 0
        self.refresh_score()

    def record_high_score(self):
        with open("high_score.txt", mode="w") as score:
            score.write(str(self.high_score))

    def previous_high_score(self):
        with open("high_score.txt", mode="r") as score:
            num = score.read()
            self.high_score = int(num)

