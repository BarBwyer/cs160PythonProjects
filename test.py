from turtle import *
from time import sleep

#house
for i in range(4):
	forward(100)
	right(90)
#forward(100)
#right(90)
#forward(100)
#right(90)
#forward(100)

#door
left(90)
backward(100)
right(90)
forward(25)
left(90)
forward(50)
right(90)
forward(35)
right(90)
forward(50)
penup()

#roof
right(90)
forward(60)
right(90)
forward(100)
left(90)
forward(15)
left(90)
forward(10)
left(135)
pendown()
forward(92)
right(90)
forward(92)

#ground
right(45)
penup()
forward(90)
right(90)
forward(470)
left(180)
pendown()
pencolor("#0f9122")
forward(700)

#person 1
penup()
right(180)
forward(200)
right(135)
pencolor("#fcdb00")
pendown()
forward(30)
right(90)
forward(30)
right(180)
forward(30)
right(45)
forward(20)

sleep(3)