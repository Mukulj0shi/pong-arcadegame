from turtle import Turtle


class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.penup()


    def move_ball(self):
        if self.heading() == 0 and self.xcor() < 380:
            self.forward(10)
            print(self.position())
        elif self.xcor() == 380:
            self.setheading(180)
            self.forward(1)
            print(self.heading())
        elif self.heading() == 180.0 and self.xcor() >= -380:
            self.forward(10)
            print(self.position())
        elif self.xcor() == -381:
            self.setheading(0)
            self.forward(1)
            print(self.heading())





