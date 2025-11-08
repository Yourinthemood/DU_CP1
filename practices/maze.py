
# DU P3 Maze Generator

import turtle
import random
# set up screen and turtle
# make turtle fast and lift pen
# define setup function to make screen and position turtle
# define draw wall function to put pen down draw line and lift pen
# define generate maze function
# use nested loops for grid rows and columns
# at each cell position turtle
# use random to decide if wall should be drawn
# skip walls at start and end positions
# mark start and end with colors
# call generate maze function
# keep window open

screen = turtle.Screen()
screen.bgcolor("white")
maze_turtle = turtle.Turtle()
maze_turtle.speed(0)
maze_turtle.penup()

def setup():
    screen.setup(800, 800)
    maze_turtle.goto(-180, 180)

def draw_wall():
    maze_turtle.pendown()
    maze_turtle.pensize(3)
    maze_turtle.forward(30)
    maze_turtle.penup()

def generate_maze():
    setup()
    
    for row in range(6):
        for col in range(6):
            maze_turtle.goto(-180 + col * 60, 180 - row * 60)
            
            if random.random() > 0.3:
                if row == 0 and col == 0:
                    pass
                elif row == 5 and col == 5:
                    pass
                else:
                    draw_wall()
    
    mark_start_end()

def mark_start_end():
    maze_turtle.goto(-180, 210)
    maze_turtle.color("green")
    maze_turtle.write("START", align="center")
    
    maze_turtle.goto(180, -210)
    maze_turtle.color("red")
    maze_turtle.write("END", align="center")

generate_maze()
turtle.done()
