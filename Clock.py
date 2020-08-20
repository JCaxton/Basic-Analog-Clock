#  Getting started

#  Setting up the clock and importing necessary libraries.

import time
import turtle

win = turtle.Screen()
win.bgcolor("black")
win.setup(width=450, height=450)
win.title("Simple Analog Clock")
win.tracer(0)

#  Creating drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def draw_clock(hr, mn, sec, pen):
    """This function draws the clock face"""
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("red")
    pen.pendown()
    pen.circle(210)

    #  Draw clock markings
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    for j in range(12):
        pen.fd(185)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    #  Draw hour hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("green")
    pen.setheading(90)
    angle = (hr / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(125)

    #  Draw minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("yellow")
    pen.setheading(90)
    angle = (mn / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(175)

    #  Draw seconds hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    angle = (sec / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(190)


while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))

    draw_clock(hr, mn, sec, pen)
    win.update()  #  Updates the clock with the current time.

    time.sleep(1)   #  Pauses the action for 1 second before drawing again. Gives the 'tik-tok illusion.

    pen.clear()    # Clears the pen in order to redraw it again.

win.mainloop()  #  This runs the code.
