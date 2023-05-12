import random
from turtle import Turtle, Screen
mysnake=[]
class Snake:
    def __init__(self,length,speed):
        self.head=Turtle("circle")
        self.head.penup()
        self.head.speed(0)
        self.head.fillcolor("white")
        self.length=length
        self.head.speed(speed)
        mysnake.append(self.head)
        self.csnake(self.length)

    def csnake(self,length):
        for i in range(1,length):
            bodypart=Turtle("square")
            bodypart.penup()
            bodypart.speed(0)
            bodypart.fillcolor("white")
            # bodypart.setx(mysnake[i-1].xcor()-20)
            mysnake.append(bodypart)

