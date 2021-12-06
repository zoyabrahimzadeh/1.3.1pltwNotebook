import turtle

catcherTurtle = turtle.Turtle()
def moveLeft(catcherTurtle=catcherTurtle):
    catcherTurtle.penup()
    catcherTurtle.setheading(180)
    catcherTurtle.forward(5)


def moveRight(catcherTurtle=catcherTurtle):
    catcherTurtle.penup()
    catcherTurtle.setheading(0)
    catcherTurtle.forward(5)
    

wn = turtle.Screen()
catcherTurtle.speed(0)
wn.onkeypress(moveLeft, "a")
wn.onkeypress(moveRight, "d")
wn.listen()
wn.mainloop()