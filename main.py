from turtle import Turtle,Screen
from layout import Layout
from pong import Ball
import time
from score import Score

turtle_object = Turtle()
screen_object = Screen()
layout1_object = Layout()
ball_object = Ball()
score_object = Score()

screen_object.tracer()
screen_object.listen()
screen_object.onkey(layout1_object.leftup, "w")
screen_object.onkey(layout1_object.leftdown, "s")
screen_object.onkey(layout1_object.rightup, "Up")
screen_object.onkey(layout1_object.rightdown, "Down")

is_game_on = True

while is_game_on:
    time.sleep(ball_object.new_speed)
    screen_object.update()
    ball_object.move_ball()

    # Ball bounces when ball touches the boundary.
    if ball_object.ycor() > 260 or ball_object.ycor() < -260:
        ball_object.bounce_ball()
        print("Touched boundary")

    # Ball hit right or left bat
    if ball_object.distance(layout1_object.rightbat.position()) < 45 and ball_object.xcor() > 350 or ball_object.distance(layout1_object.leftbat.position()) < 45 and ball_object.xcor() < -350:
        ball_object.bounce_back_left()
        print(ball_object.new_speed)

    # Bring ball to center and start game again from winning side.
    elif ball_object.xcor() > 360:
        ball_object.start_again()
        ball_object.bounce_back_left()
        score_object.left_score()
    elif ball_object.xcor() < -360:
        ball_object.start_again()
        ball_object.bounce_back_right()
        score_object.right_score()

screen_object.exitonclick()


