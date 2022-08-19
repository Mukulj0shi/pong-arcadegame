from turtle import Turtle, Screen

style = ('Courier', 40, 'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-10, 260)
        self.color('white')
        self.r_score = 0
        self.l_score = 0
        self.write(str(self.r_score) + "      " +str(self.l_score), font=style, align='center')
        self.hideturtle()

    def score_board(self):
        self.clear()
        self.write(str(self.l_score) + "      " +str(self.r_score), font=style, align='center')


    def right_score(self):
        self.r_score += 1
        self.score_board()

    def left_score(self):
        self.l_score += 1
        self.score_board()