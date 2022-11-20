from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setposition(0, 260)
        self.score = 0
        self.highest_score = 0
        self.refresh_scoreboard()
        self.refresh_highest_score()

    def refresh_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  , Highest score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def refresh_highest_score(self):
        if self.score >= self.highest_score:
            self.highest_score = self.score

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER :(", align=ALIGNMENT, font=FONT)

    def increase_score(self, increase_amount=1):
        self.score += increase_amount
        self.refresh_scoreboard()
