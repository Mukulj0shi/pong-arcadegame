from turtle import Turtle,Screen

bat_cordinate = [(-350, 0), (350, 0)]

class Layout():
    def __init__(self):
        #self.turtle_object = Turtle()
        self.turtle_bat_object = []
        self.screen_object = Screen()
        self.screen_object.setup(width=800, height=600)
        self.screen_object.bgcolor("black")
        self.screen_object.title("Pong Game")
        for bat in bat_cordinate:
            self.turtle_object = Turtle()
            self.turtle_object.shape("square")
            self.turtle_object.color("white")
            self.turtle_object.hideturtle()
            self.turtle_object.penup()
            self.turtle_object.goto(bat)
            self.turtle_object.setheading(90)
            self.turtle_object.shapesize(stretch_wid=1, stretch_len=5)
            self.turtle_object.showturtle()
            self.turtle_bat_object.append(self.turtle_object)
            print(self.turtle_bat_object)
        self.rightbat = self.turtle_bat_object[1]
        self.leftbat = self.turtle_bat_object[0]

    def createnet(self):
        self.turtle_object.shape("square")
        self.turtle_object.color("white")
        self.turtle_object.hideturtle()
        self.turtle_object.penup()
        self.turtle_object.goto(0.00, -260.00)
        self.turtle_object.setheading(90)
        self.turtle_object.shapesize(0.2, 3)
        self.turtle_object.showturtle()

    def leftup(self):
        if self.leftbat.ycor() < 270:
            #print(self.turtle_bat_object[0])
            self.turtle_bat_object[0].forward(50)

    def leftdown(self):
        if self.leftbat.ycor() > -270:
            #print(self.turtle_bat_object[0])
            self.turtle_bat_object[0].backward(50)

    def rightup(self):
        if self.rightbat.ycor() < 270:
            #print(self.turtle_bat_object[1])
            self.turtle_bat_object[1].forward(50)

    def rightdown(self):
        if self.rightbat.ycor() > -270:
            #print(self.turtle_bat_object[0])
            self.turtle_bat_object[1].backward(50)







