# from turtle import Turtle, Screen,tracer
from turtle import *
from control import *
import snake,screen,movment

myscreen=screen.MyScreen()
tracer(0)
listen()
python=snake.Snake(4,0)


movment.move()
myscreen.screen.exitonclick()
