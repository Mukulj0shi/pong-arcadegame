from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.circle(20)
        self.color("blue")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.new_speed = 0.1
        ## Question : How to identify and print this object in which we are working.

    def move_ball(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)
        #print(f"move {self.xmove},{self.ymove}")

    def bounce_ball(self):
        self.ymove *= -1

    def bounce_back_left(self):
        self.xmove *= -1
        self.new_speed *= 0.01
        #print(f"left {self.xmove},{self.ymove}")

    def bounce_back_right(self):
        self.xmove *= -1
        #print(f"right {self.xmove},{self.ymove}")

    # Start game again once ball leaves the screen
    def start_again(self):
        self.hideturtle()
        self.goto(0, 0)
        self.new_speed = 0.1
        self.showturtle()


