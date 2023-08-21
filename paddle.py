from turtle import Turtle
import random

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    def up(self):
        y_cor=self.ycor()+20
        if y_cor<265:
            self.goto(self.xcor(),y_cor)

    def down(self):
        y_cor=self.ycor()-20
        if y_cor>-255:
            self.goto(self.xcor(),y_cor)

