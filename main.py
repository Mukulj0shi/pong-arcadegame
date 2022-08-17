from turtle import Turtle,Screen
from layout import layout1

turtle_object = Turtle()
screen_object = Screen()
layout1_object = layout1()

screen_object.listen()
screen_object.onkey(layout1_object.leftup, "w")
screen_object.onkey(layout1_object.leftdown, "s")
screen_object.onkey(layout1_object.rightup, "Up")
screen_object.onkey(layout1_object.rightdown, "Down")





screen_object.exitonclick()


