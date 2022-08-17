from turtle import Turtle


class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.circle(20)
        self.color("blue")
        self.penup()




    def move_ball(self):
        #self.left(45)
        self.goto(362, 260)  # Y is a variable
        #self.setheading(180)
        self.goto(0, 0)
        self.goto(-365, 260)







