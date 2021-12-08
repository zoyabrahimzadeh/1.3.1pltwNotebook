import turtle
import random
wn = turtle.Screen()

def runningAnimation(runFrames, rangeSpotsY, rangeSpotsX, myTurtle=turtle.Turtle()):
    ySpot = random.randint(rangeSpotsY[0], rangeSpotsY[1])
    xSpot = random.randint(rangeSpotsX[0], rangeSpotsX[1])
    xCur, yCur = myTurtle.pos()
    xDiff = int(abs(xSpot) - abs(xCur)) #absolute value of ySpot and xCur and their difference 
    yDiff = 0
    xRemainder = xDiff % 10
    myTurtle.setpos(xCur, ySpot)
    myTurtle.showturtle()
    for i in range(xDiff//10):
        for j in runFrames:
            myTurtle.shape(j)
            movement = 10/len(runFrames)
            myTurtle.forward(movement)
    myTurtle.forward(xRemainder)

runningAnimation(["triangle", "classic", "circle"], [120, 130], [-150, 150])
wn.mainloop()