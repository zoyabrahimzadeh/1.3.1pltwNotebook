import random
import turtle
catcherTurtle = turtle.Turtle()
wn = turtle.Screen()
def person_falling(y, skyRange, phoneTurtle=turtle.Turtle(), catcher=catcherTurtle):
    phoneTurtle.penup()
    phone = 'triangle'
    phone2 = "ezgif-3-2a18e3e7accc.gif"
    wn.addshape(phone2)
    phoneTurtle.shape('triangle')
    angle = [phone, phone, phone, phone, phone, phone]
    # this would also be the x of where teresa would run to
    x = random.randint(skyRange[0], skyRange[1])
    print(x)
    phoneTurtle.goto(x,y) # top of building cords
    phoneTurtle.setheading(260) # sets the angle so it falls downwards
    in_air = True

    # checks if the x position for the next body is close to the x position of the previous body
    # while loop - code will run until they are in close range of each other (collision)
    while in_air: # runs as long as the phone hasn't reached the floor coordinates
        phoneTurtle.setheading(260)
        catcherTurtle.speed(0)
        wn.onkeypress(moveLeft, "a")
        wn.onkeypress(moveRight, "d")
        wn.listen()
        phoneTurtle.speed(0)
        phoneTurtle.forward(random.randint(10,30)) # moves forward a random amount before turning a random amount
        angleTurn = random.randint(1,180) # this is so that the movement isn't linear and instead turns and staggers  
        phoneTurtle.right(angleTurn)

        for i in range(6):
            phoneTurtle.shape(angle[i]) # almost like stop motion, switches through 4 angles of person falling to make it seem like movement      
        
        xCheck, yCheck = phoneTurtle.pos() # defines the variable that contains the current y cord to see if its near the fall of building
        xCheckCatcher, yCheckCatcher = catcher.pos()
        
        if yCheckCatcher-20 < yCheck <yCheckCatcher + 20 and xCheckCatcher-20 < xCheck <xCheckCatcher + 20:# checks if the person is near the floor, stopping them from falling
            in_air = False
            # score +=1
        if yCheckCatcher > yCheck:
            in_air = False
            print("u suck") 

def moveLeft(catcherTurtle=catcherTurtle):
    catcherTurtle.penup()
    catcherTurtle.setheading(180)
    catcherTurtle.forward(5)


def moveRight(catcherTurtle=catcherTurtle):
    catcherTurtle.penup()
    catcherTurtle.setheading(0)
    catcherTurtle.forward(5)

def runningAnimation(runFrames, rangeSpotsY, rangeSpotsX, myTurtle=turtle.Turtle()):
    ySpot = random.randint(rangeSpotsY[0], rangeSpotsY[1])
    xSpot = random.randint(rangeSpotsX[0], rangeSpotsX[1])
    xCur, yCur = myTurtle.pos()
    xDiff = int(abs(xSpot) - abs(xCur)) #absolute value of ySpot and xCur and their difference 
    xRemainder = xDiff % 10
    myTurtle.setpos(xCur, ySpot)
    myTurtle.showturtle()
    for i in range(xDiff//10):
        for j in runFrames:
            myTurtle.shape(j)
            movement = 10/len(runFrames)
            myTurtle.forward(movement)
    myTurtle.forward(xRemainder)

person_falling(200, [-100,100])
wn = turtle.Screen()
wn.mainloop()
