FONT = ("courier", 24, "normal")
SCORE_POS = (0,265)
CURRENT_SCORE = 0

from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = []
        score = Turtle()
        score.penup()
        score.hideturtle()
        self.current_score = CURRENT_SCORE
        score.goto(SCORE_POS) #change this to start at and not goto
        score.color("green")
        self.score.append(score)

    def add_point(self):
        self.current_score += 1

    def show_score(self):
        self.score[0].clear()
        score_string = f"Score: {  self.current_score  }"
        self.score[0].write(score_string, align = "center", font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.penup()
        self.color("white")
        self.write("Game over", align="center", font=FONT)

