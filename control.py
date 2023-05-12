from turtle import *
import snake

def left ():
    snake.mysnake[0].setheading(180)

def right ():
    snake.mysnake[0].setheading(0)
def up ():
    snake.mysnake[0].setheading(90)

def down ():
    snake.mysnake[0].setheading(270)

onkeypress(left,"Left")
onkeypress(right,"Right")
onkeypress(up,"Up")
onkeypress(down,"Down")



