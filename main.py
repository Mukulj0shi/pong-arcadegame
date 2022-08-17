from turtle import Turtle,Screen
from layout import layout1
from pong import ball

turtle_object = Turtle()
screen_object = Screen()
layout1_object = layout1()
ball_object = ball()

screen_object.tracer()
screen_object.listen()
screen_object.onkey(layout1_object.leftup, "w")
screen_object.onkey(layout1_object.leftdown, "s")
screen_object.onkey(layout1_object.rightup, "Up")
screen_object.onkey(layout1_object.rightdown, "Down")

is_game_on = True

while is_game_on:
    screen_object.update()
    ball_object.move_ball()




screen_object.exitonclick()


