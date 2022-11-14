from turtle import Turtle
Alignment = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setposition(0, 260)
        self.score = 0
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=Alignment, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER :(", align=Alignment, font=FONT)

    def increase_score(self, increase_amount=1):
        self.score += increase_amount
        self.refresh_scoreboard()
