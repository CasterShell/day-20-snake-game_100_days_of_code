FONT = ("courier", 24, "normal")
SCORE_POS = (0, 265)
CURRENT_SCORE = 0


from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POS)
        self.color("green")
        self.current_score = CURRENT_SCORE
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.show_score()

    def add_point(self):
        self.current_score += 1

    def show_score(self):
        self.clear()
        score_string = f"Score: {self.current_score} High Score: {self.high_score}"
        self.write(score_string, align="center", font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.current_score = 0
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.penup()
        self.color("white")
        self.write("Game over", align="center", font=FONT)

