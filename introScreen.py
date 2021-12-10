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
    while cont:
        global box
        box = True
        writeSegment(catcherNameSeg)
        catcherInp = turtle.textinput("catcher name", "").title()
        cont = playerInfo(catcherInp)
    if catcherInp[-1] == "?":
        catcherInp = catcherInp[:-1]
    time.sleep(3)
    writeSegment(segThree.format(catcherInp, catcherInp))
    time.sleep(3)
    wn.onclick(None)
    writeSegment(segFour)
    time.sleep(3)
    wn.onclick(None)
    playerName = turtle.textinput("Player Name", "").title()
    writeSegment(playerNameSeg)
    time.sleep(3)
    wn.onclick(None)
    
    writeSegment(transition.format(playerName))

    
drawer = turtle.Turtle()   
box = False 
def writeSegment(seg):
    global box    
    drawer.clear()
    wn.bgcolor("white")
    drawer.penup()
    drawer.goto(-380, -280)
    print("box", box)
    if box != True:
        boxDrawer = turtle.Turtle()
        boxDrawer.color("pink")
        boxDrawer.penup()
        boxDrawer.goto(-380, -280)
        boxDrawer.pendown()
        for i in range(2):
            boxDrawer.forward(760)
            boxDrawer.left(90)
            boxDrawer.forward(90)
            boxDrawer.left(90)
            box = True
    drawer.penup()
    drawer.forward(20)
    drawer.right(90)
    drawer.write(seg, font=("Arial", 17, "normal"))
    drawer.setheading(0)

def playerInfo(inpStr):
    alex = "Alex-(Hard)\nPros: Tall (catches phone faster than others) Con: Slower\n " \
        "Alex is tall which gives him the advantage of catching anything falling from the sky."\
            "However, he is has quite a slow pace at running."

    kate = "Kate-(Normal)\nPros: Normal speed + height\nKate is an average person" \
        "with an average pace. She considers herself to have no disadvantages" \
            "with her normal height and a speed that she's happy about."
    
    gina = "Gina-(Easy)" \
            "Pros: Fast Con: Short" \
                "Gina is a quick runner and has an advantage if something happened to fall from the sky."\
                "However, she is quite short so she happens to have many close call moments."

    playerInfo = {"Alex": alex,"Kate": kate, "Gina": gina}  
    againSeg = "Would you like to get info on other characters? \n (y or n)\n"
    errorMssg = "Error! \nSorry, thats an invalid input. Please try running the program again\n"
    cont = True
    while cont:
        if inpStr[-1] == "?":
            writeSegment(playerInfo[inpStr[:-1]]) 
            writeSegment(againSeg)
            again = turtle.textinput("Again?", "")
            if again == "y":
                return True
            if again == "n":
                return False
            else:
                writeSegment(errorMssg)
        else:
            return False


intro()
# questions: does onclick count as an event if we're not passing in a function
wn.mainloop()