import turtle
wn = turtle.Screen()
wn.setup(800,600)
def intro(playerName):
    segOne = "Welcome to the games!\n Today, you will be playing as...er...who are you going to be" \
        " playing as?\n"
    catcherNameSeg = "Our three character options are Kate, Gina, and Alex. \nType a catchers name with a question mark"\
         "to learn more about their \nbenefits/disadvantages."
         # do the .format once you collect the inputs
    segThree = "{} name? Great! \nOk, so today you will be playing as {} to keep Teresa's " \
        "phone from falling.\n "
    segFour = "If you manage to catch all her attempts (using the A and D keys)\n"\
        "by the time the timer is up, you win!" \
        " If you don't...\n"
    playerNameSeg = "Anyways! I forgot to ask you your name, you are...?\n\n"
    writeSegment(segOne)
    playerName = input("")
    cont = True
    while cont:
        cont = writeSegment(catcherNameSeg)
    
    

def writeSegment(seg):
    global box
    box = False
    drawer = turtle.Turtle()
    drawer.clear()
    wn.bgcolor("white")
    drawer.penup()
    drawer.goto(-380, -280)
    if box != True:
        drawer.pendown()
        for i in range(2):
            drawer.forward(760)
            drawer.left(90)
            drawer.forward(90)
            drawer.left(90)
            box = True
    drawer.penup()
    drawer.forward(20)
    drawer.right(90)
    drawer.write(seg, font=("Arial", 17, "normal"))

def playerInfo(inpStr):
    playerInfo = {"Teresa":"", "Alex":"", "Gina":""}  
    againSeg = "Would you like to get info on other characters? \n (y or n)\n"
    errorMssg = "Error! \nSorry, thats an invalid input. Please try running the program again\n"
    cont = True
    while cont:
        if inpStr[-1] == "?":
            writeSegment(playerInfo[inpStr[:-1]]) # use while loop in main code
            writeSegment(againSeg)
            again = input("")
            if again == "y":
                return True
            if again == "n":
                return False
            else:
                writeSegment(errorMssg)
        else:
            return False


intro("zoy")

wn.mainloop()