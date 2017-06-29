from turtle import *

sides = int(input("Enter number of sides:"))
angle = 360/sides
pencolor('cyan')

fillcolor('cyan')
print ("sides:", sides, "angle:", angle)

for s in range(sides):
    forward(100)
    right(angle)
    forward(100)

exitonclick()
