# Creating a basic Pong game

import turtle

# The Screen code
wn = turtle.Screen()
wn.title("A Classic Pong Game!")
wn.bgcolor("black")
wn.setup(height=600, width=800)
wn.tracer(0)


# Left Paddle

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.shapesize(stretch_len=1, stretch_width=5)
paddle_a.goto(0, 0)



input()