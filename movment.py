import turtle
from turtle import Turtle, Screen
import snake
def move():
    gameon=True
    while gameon:
        snake.mysnake[0].forward(1)
        # for i in range(1,snake.mysnake.__len__()):
        for i in range(1, 4):
            temppostion=snake.mysnake[i-1].position()
            tempheading=snake.mysnake[i-1].heading()
            snake.mysnake[i].goto(temppostion)
            snake.mysnake[i].setheading(tempheading)


        turtle.update()

