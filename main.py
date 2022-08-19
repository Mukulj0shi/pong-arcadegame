from turtle import Turtle,Screen
from layout import Layout
from pong import Ball
import time

turtle_object = Turtle()
screen_object = Screen()
layout1_object = Layout()
ball_object = Ball()

screen_object.tracer()
screen_object.listen()
screen_object.onkey(layout1_object.leftup, "w")
screen_object.onkey(layout1_object.leftdown, "s")
screen_object.onkey(layout1_object.rightup, "Up")
screen_object.onkey(layout1_object.rightdown, "Down")

is_game_on = True

while is_game_on:
    time.sleep(0.8)
    screen_object.update()
    ball_object.move_ball()
    #print(ball_object.xcor())
    if ball_object.ycor() > 260 or ball_object.ycor() < -260:
        ball_object.bounce_ball()
        print("Toched boundary")
    if ball_object.distance(layout1_object.rightbat.position()) < 45:
        #print("TRUE BRU")
        ball_object.bounce_back_left()
        print(layout1_object.rightbat.position())
        print(ball_object.position())
        print(f" distnce:{ball_object.distance(layout1_object.rightbat.position())}")

    elif ball_object.xcor() > 390:
        print(layout1_object.rightbat.position())
        print(ball_object.position())
        print(f" distnce:{ball_object.distance(layout1_object.rightbat.position())}")


screen_object.exitonclick()


