from  turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()


    def player_1_score(self):
        self.goto(-100,270)
        self.write(f'{self.score}', font=('Arial', 15))
        self.hideturtle()

    def player_2_score(self):
        self.goto(100, 270)
        self.write(f'{self.score}', font=('Arial', 15))
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f'{self.score}', font=('Arial', 15))