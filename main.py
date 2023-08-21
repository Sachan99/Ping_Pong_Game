from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen= Screen()
ball=Ball()
scoreboard=Scoreboard()

screen.setup(700,600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

right_paddle= Paddle((300,0))
left_paddle= Paddle((-300,0))


screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"a")
screen.onkey(left_paddle.down,"z")

should_cont=True
while should_cont:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard.update_score()
    if ball.ycor()>288 or ball.ycor()<-280:
        ball.bounce_wall()

    if ball.distance(right_paddle)<50 and ball.xcor()>260 or ball.distance(left_paddle)<50 and ball.xcor()<-260:
        ball.bounce_paddle()

    if ball.xcor()>330:
        ball.goto(0,0)
        ball.goto_nextplayer()
        scoreboard.l_points()

    if ball.xcor()<-330:
        ball.goto(0,0)
        ball.goto_nextplayer()
        scoreboard.r_points()













screen.exitonclick()

