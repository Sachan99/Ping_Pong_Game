from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1
    def move(self):
        # self.penup()
        x= self.xcor() + self.x_move
        y=self.ycor() + self.y_move
        self.goto(x,y)

    def goto_nextplayer(self):
        self.move_speed = 0.1
        self.x_move *=-1


    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *=0.9


