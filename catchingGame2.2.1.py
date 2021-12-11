# imports
import random
import turtle
from endings020 import Ending

turtle.hideturtle()
# variable initialization 
endingScreens = Ending()
catcherTurtle = turtle.Turtle()
catcherTurtle.color("green")
catcherTurtle.penup()
phoneTurtle=turtle.Turtle()
score = 0
winning = True
fontSetup = ("Arial", 16, "normal")
timer = 30
counterInterval = 1000   #1000 represents 1 second
timerUp = False
phoneImg = "phoneTransparentBg.gif"
kate = "catcherKate.gif"
gina = "catcherGina.gif"
alex = "catcherAlex.gif"
teresaThrowOne = "teresaThrowFrame1.gif"
teresaThrowTwo = "teresaThrowFrame2.gif"
teresaRunOne = "teresaRunFrameOne.gif"
runFrames = [teresaRunOne]
throwFrames = [teresaThrowTwo, teresaThrowOne]
counter=turtle.Turtle() 
counter.hideturtle()
boxDrawer = turtle.Turtle()
boxDrawer.hideturtle()
scoreWriter = turtle.Turtle()
scoreWriter.color("lightgreen")
scoreWriter.penup()
scoreWriter.hideturtle()
scoreWriter.goto(-165, 200)
schoolBg = "schoolBg_1_800x600.gif"
wn = turtle.Screen()
wn.addshape(schoolBg)
wn.bgpic(schoolBg)
# wn.bgcolor("lightgreen")
# function for countdown/timer
wn.addshape(phoneImg)
wn.addshape(kate)
wn.addshape(gina)
wn.addshape(alex)
wn.addshape(teresaThrowOne)
wn.addshape(teresaThrowTwo)
wn.addshape(teresaRunOne)

import turtle
import time
wn = turtle.Screen()
wn.setup(800,600)

def intro():
    segOne = "Welcome to the games!\n Today, you will be playing as...er...who are you going to be" \
        " playing as?\n"
    catcherNameSeg = "Our three character options are Kate, Gina, and Alex. \nType a catchers name with a question mark"\
         " to learn more about their \nbenefits/disadvantages. Or just type their name to select them!"
         
    segThree = "{}? Great! \nOk, so today you will be playing as {} to keep Teresa's " \
        "phone from \nfalling. "
    segFour = "If you manage to catch all their attempts (using the A and D keys)\n"\
        "by the time the timer is up, you win!" \
        " If you don't...\n"
    playerNameSeg = "Anyways! I forgot to ask you your name, you are...?\n\n"
    transition = "Great to meet you, {}! Let the games begin!\n\n"
    writeSegment(segOne)
    time.sleep(3)
    wn.onclick(None)
    cont = True
    # if extra time: fix bug where you can put any name, not catcher names
    while cont == True or cont == "m":
        global box
        box = True
        writeSegment(catcherNameSeg)
        catcherInp = turtle.textinput("catcher name", "").title()
        cont = playerInfo(catcherInp)
    if catcherInp[-1] == "?":
        catcherInp = catcherInp[:-1]
    writeSegment(segThree.format(catcherInp, catcherInp))
    time.sleep(3)
    wn.onclick(None)
    writeSegment(segFour)
    time.sleep(3)
    wn.onclick(None)
    writeSegment(playerNameSeg)
    playerName = turtle.textinput("Player Name", "").title()
    wn.onclick(None)
    
    writeSegment(transition.format(playerName))
    return catcherInp

    
drawer = turtle.Turtle()   
box = False 
def writeSegment(seg):
    global box    
    drawer.clear()
    drawer.penup()
    drawer.goto(-380, -280)
    print("box", box)
    if box != True:
        boxDrawer.speed(0)
        boxDrawer.color("red")
        boxDrawer.hideturtle()
        boxDrawer.penup()
        boxDrawer.goto(-380, -280)
        boxDrawer.pendown()
        boxDrawer.begin_fill()
        boxDrawer.fillcolor("white")
        for i in range(2):
            boxDrawer.forward(760)
            boxDrawer.left(90)
            boxDrawer.forward(90)
            boxDrawer.left(90)
            box = True
        boxDrawer.end_fill()
    drawer.speed(0)
    drawer.penup()
    drawer.forward(20)
    drawer.right(90)
    drawer.write(seg, font=("Arial", 17, "normal"))
    drawer.setheading(0)

def playerInfo(inpStr):
    alex = "Alex (Hard) --> Pros: Tall (catches phone faster), Cons: Slower.\n" \
        "Alex is tall which gives him an advantage when catching things. "\
            "However, \nhe has quite a slow pace at running."

    kate = "Kate (Normal) --> Pros: Normal speed and height.\nKate is an average person " \
        "with an average pace. She has no \ndisadvantages, " \
            "she has a normal height and speed that she's happy about."
    
    gina = "Gina (Easy) --> " \
            "Pros: Fast, Cons: Short.\n" \
                "Gina is a quick runner,"\
                " however, she is quite short so she happens to \nhave many close call moments."

    playerInfo = {"Alex": alex,"Kate": kate, "Gina": gina}  
    againSeg = "Would you like to get info on other characters? \n (y or n)\n"
    errorMssg = "Error! \nSorry, thats an invalid input. Please try running the program again\n"
    cont = True
    while cont:
        if inpStr[-1] == "?":
            writeSegment(playerInfo[inpStr[:-1]])
            time.sleep(8) 
            writeSegment(againSeg)
            again = turtle.textinput("Again?", "")
            if again == "y":
                return True
            if again == "n":
                return "m" #change this to 3 diff values, choose character no info, wants info on character, choose character after getting info
            else:
                writeSegment(errorMssg)
                time.sleep(4)
        else:
            return False


def countdown(counter=counter):
  counter.color("lightblue")

  global timer, timerUp
  # sets up the visual aspects of the timer (clearing the writing, correct spot)
  counter.clear()
  counter.penup()
  counter.setpos(165, 200)
  counter.pendown()
  counter.hideturtle()
  # stops the timer if the player looses or the time is up
  if timer <= 0 or not winning:
    # counter.write("Time's Up", font=fontSetup)
    timerUp = True
    catcherTurtle.hideturtle()
    phoneTurtle.hideturtle()

    # incrementally decreases the timer so that it eventually reaches 0 
  else:
    counter.write("Timer: " + str(timer), font=fontSetup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counterInterval)

# function for the all of movement/ functionality of the phone
def phoneFalling(y, skyRange, throwFrames=throwFrames, phoneTurtle=phoneTurtle, catcher=catcherTurtle):
    phoneTurtle.penup()
    teresaTurtle.penup()
    teresaTurtle.goto(350, 200)

    teresaY = runningAnimation(runFrames, skyRange, [200, 201])
    phoneTurtle.goto(teresaTurtle.xcor(), teresaY+15)
    phoneTurtle.penup()
    phoneTurtle.color("red")
    catcher.color("purple")
    catcher.penup()
    # sets the phone appearance of turtle
    phoneTurtle.shape(phoneImg)
    

    # since we can't use actual videos, we're using stop motion of different angles 
    # to make it stimulate / appear as if theres movement
    angle = [phoneImg, phoneImg, phoneImg, phoneImg, phoneImg, phoneImg]

    # this would also be the x of where teresa would run to (where she drops the phone from)
    # x = random.randint(skyRange[0], skyRange[1])
    # print(x)
    # phoneTurtle.goto(x,y) # top of bridge, where the phone is dropped cords
    phoneTurtle.setheading(260) # sets the angle so it falls downward

    # defines the variable used to repeat the while loop until the phone reaches catcher/ floor

    inAir = True

    # checks if the  position for the catcher is close to the position of the phone
    # code looping phone movement will run until they are in close range of each other (collision)
    # there are two cases in which the loop stops iterating, reaching the catcher, or the floor
    teresaTurtle.penup()
    # teresaTurtle.setpos(phoneTurtle.pos())
    phoneTurtle.showturtle()
    for i in throwFrames:
        teresaTurtle.shape(i)
        time.sleep(0.5)

    while inAir: 
       
        phoneTurtle.setheading(260)
        catcherTurtle.speed(0)
        # makes movement more randomized
        phoneTurtle.speed(0)
        phoneTurtle.forward(random.randint(10,30)) # moves forward a random amount before turning a random amount
        angleTurn = random.randint(1,180) # this is so that the movement isn't linear and instead turns and staggers  
        phoneTurtle.right(angleTurn)
        
    
        for i in range(6):
            # almost like stop motion, switches through 4 angles of person 
            # falling to make it seem like movement
            phoneTurtle.shape(angle[i])       
        
        # defines the variables that contains the current cords of catcher and phone
        # these are used to check if there's collisions
        xCheck, yCheck = phoneTurtle.pos() 
        xCheckCatcher, yCheckCatcher = catcher.pos()
 
        # compares the coordinates of the two turtles to see if they're near each other/ collided
        if yCheckCatcher-30 < yCheck <yCheckCatcher + 30 and xCheckCatcher-20 < xCheck <xCheckCatcher + 20:# checks if the person is near the floor, stopping them from falling
            inAir = False

            # updates/ displays score accordingly
            global score 
            score +=1
            scoreWriter.clear()
            scoreWriter.write(score, font=("Arial", 17, "normal"))
            phoneTurtle.hideturtle()

        # checks if the player lost (by not catching the phone) and updating the program accordingly   
        if yCheckCatcher > yCheck:
            inAir = False
            global winning
            winning = False
            print("u suck") 

            

def moveLeft(catcherTurtle=catcherTurtle):
    catcherTurtle.penup()
    catcherTurtle.setheading(180)
    global speedSteps
    catcherTurtle.forward(speedSteps)


def moveRight(catcherTurtle=catcherTurtle):
    catcherTurtle.penup()
    catcherTurtle.setheading(0)
    global speedSteps
    catcherTurtle.forward(speedSteps)

teresaTurtle = turtle.Turtle()

def runningAnimation(runFrames, rangeSpotsX, rangeSpotsY , myTurtle=teresaTurtle):
    myTurtle.color("orange")
    ySpot = random.randint(rangeSpotsY[0], rangeSpotsY[1])
    xSpot = random.randint(rangeSpotsX[0], rangeSpotsX[1])
    xCur, yCur = myTurtle.pos()
    # gets the difference between these two spots to know how far we need to move
    xDiff = abs(int(abs(xSpot) - abs(xCur)))
    print(xDiff)
    # uses iteration to move forward while doing stop motion, the extra amount of steps needed to be taken that cannot be
    # distributed equally will be added at the end 
    xRemainder = xDiff % 10
    myTurtle.setpos(xCur, ySpot)
    myTurtle.setheading(180)
    myTurtle.showturtle()
    for i in range(xDiff//10):
        for j in runFrames:
            # moves forward the same amount while changing stop motion frames
            # this makes everything look as efficient as possible
            myTurtle.shape(j)
            movement = 10/len(runFrames)
            myTurtle.forward(movement)
    myTurtle.forward(xRemainder)
    return ySpot

def setCatcherSpecs(catcherName, turtle=catcherTurtle):
    global speedSteps
    if catcherName == "Alex":
        turtle.turtlesize(2)
        speedSteps = 3
        turtle.shape(alex)
        # teresaRunFrameOne.gif

    elif catcherName == "Gina":
        speedSteps = 15
        turtle.turtlesize(0.5)
        turtle.shape(gina)

    elif catcherName == "Kate":
        speedSteps = 9
        turtle.shape(kate)

    return turtle




# fixing spinny thingy - add more frames/iteratiosn
wn.bgcolor("white")
catcherName = intro() #call intro here
# sets up the timer
time.sleep(3)
drawer.clear()
boxDrawer.clear()
setCatcherSpecs(catcherName)
wn.ontimer(countdown, counterInterval)
# timerUp and winning are the two conditions where the game would be over
# the program can only run if these conditions are not met

catcherTurtle.goto(0, -200)
# loops through the movement and catching/scoring of the game
while not timerUp and winning:
    # controls movement of the catcher
    wn.onkeypress(moveLeft, "a")
    wn.onkeypress(moveRight, "d") # do i have to use threading?
    wn.listen()
    # calls the phone movement
    phoneFalling(200, [-100,100])

# displays an ending depending on how the player performed 

if timer <= 0:
    # good ending
    counter.clear()
    scoreWriter.clear()
    wn.clear()
    goodSegment = "Thank you so much for saving Teresa's phone, despite her many efforts! \n" \
        "You got a score of {}. Thank you so much for your assistance,\n" \
            "we appreciate it".format(score)
    endingScreens.goodEnding()
    writeSegment(goodSegment)
    pass
else:
    # if the timer isn't 0, that means it stopped incrementing before it reached 0
    # meaning that one of the loosing conditions was met, stopping the iteration
    # bad ending 
    badSegment = "I can't believe you! I had faith that you would be able to save \n Teresa's phone." \
        " This is shameful. You got a score of {} too.... \n".format(score)
    counter.clear()
    scoreWriter.clear()
    wn.clear()
    endingScreens.badEnding()
    writeSegment(badSegment)

print(score)

wn = turtle.Screen()
wn.mainloop()
