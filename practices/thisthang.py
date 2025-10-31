
# DU P2 turtle race gambling

import turtle
import random

# make turtle screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("white")

# draw red finish line on right
finish = turtle.Turtle()
finish.speed(0)
finish.penup()
finish.goto(350, 300)
finish.pendown()
finish.pensize(5)
finish.color("red")
finish.right(90)
finish.forward(600)

# create list of five colors
colors = ["red", "green", "blue", "orange", "purple"]
# make empty list for turtles
racers = []

# for each of five turtles
for i in range(5):
    # create new turtle
    t = turtle.Turtle()
    # set shape to turtle
    t.shape("turtle")
    # set color from list
    t.color(colors[i])
    # lift pen up
    t.penup()
    # move to start position on left
    t.goto(-370, -150 + i * 75)
    # add to turtles list
    racers.append(t)

# define race function
def run_race():
    # loop forever until winner
    while True:
        for turtle in racers:
            # move forward random number
            move = random.randint(5, 25)
            turtle.forward(move)
            
            # check if past finish line
            if turtle.xcor() >= 350:
                # if yes return that turtle
                return turtle

# call race function
winner = run_race()

# close window
screen.bye()
# print winner color
print(f"The {winner.color()[0]} turtle won!")
