# step1 import setup turtle color speed

import turtle
import random
turtle.bgcolor("black")
t=turtle.Turtle()
t.speed("fastest")
t.penup

#step 2 create all RGB color
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r, g, b)
    return random_color

#step 3 set up dots position and count
t.setheading(255)
t.setheading(0)
t.forward(300)
dots=101

#step 4 use ofr loop and if statement to repeat 100 dots

for current_dots in range(1, dots):
    t.color(random_color())
    t.dot(20)
    t.forward(50)
    if current_dots % 10==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
turtle.exitonclick()
