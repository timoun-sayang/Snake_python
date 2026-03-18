import turtle
import time 
import random

delay = 0.25

screenGUI = turtle.Screen()
screenGUI.title("Jeu Snake par Thomas")
screenGUI.bgcolor("green")
screenGUI.setup(width=600,height= 600)
screenGUI.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)



def up():
    head.direction ="up"
def left():
    head.direction = "left"
def right():
    head.direction ="right"
def down():
    head.direction ="down"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#key bindings
screenGUI.listen()
screenGUI.onkeypress(up,"Up")
screenGUI.onkeypress(down, "Down")
screenGUI.onkeypress(right, "Right")
screenGUI.onkeypress(left, "Left")


while True:
    screenGUI.update()

    move()
    time.sleep(delay)


screenGUI.mainloop()
