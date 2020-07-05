import time
import turtle
import os
from turtle import *


def Pong():
    P_Window = turtle.Screen()
    P_Window.title("PONG")
    P_Window.bgcolor("black")
    P_Window.setup(width = 800, height = 600)
    P_Window.tracer(0)
##Score
    score_a = 0
    score_b = 0
    
## Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)
## Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
    paddle_b.penup()
    paddle_b.goto(+350, 0)
## Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.2
    ball.dy = -0.2

## pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

    def moveLeftPaddleUp():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def moveLeftPaddleDown():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)
    def moveRightPaddleUp():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)


    def moveRightPaddleDown():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)


    P_Window.onkey(moveLeftPaddleUp, "w")
    P_Window.onkey(moveLeftPaddleDown, "s")
    P_Window.onkey(moveRightPaddleUp, "Up")
    P_Window.onkey(moveRightPaddleDown, "Down")



    

    while True:
        P_Window.listen()

        P_Window.onclick(lambda*a:[P_Window.bye(),os.system("menusystem.py")])

        
        P_Window.update()
        ## move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        ##Boarder Checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)

            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        ##Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1

Pong()
        
