from graphics import *

def main():

    win = GraphWin("Tic-Tac-Joe", 800, 800)
    win.setCoords(0, 0, 11, 11)
    startWindow(win)

def startWindow(window):

    # Set the title for the start menu
    start_Title = Text(Point(5.5, 9.5), 'Main Menu')
    start_Title.setStyle('bold')
    start_Title.setSize(36)

    # Create a button to choose local multiplayer mode
    multiPlayer = Rectangle(Point(4, 7), Point(7, 8))
    multiPlayer.draw(window)
    multi_Text = Text(Point(5.5, 7.5), 'Play Local')
    multi_Text.setSize(30)
    multi_Text.draw(window)

    # Create a button to play against AI
    playJoe = Rectangle(Point(4, 5), Point(7, 6))
    playJoe.draw(window)
    joe_Text = Text(Point(5.5, 5.5), 'Challenge Joe')
    joe_Text.setSize(30)
    joe_Text.draw(window)

    # Creates help button
    help = Rectangle(Point(4, 3), Point(7, 4))
    help.draw(window)
    help_Text = Text(Point(5.5, 3.5), 'Rules')
    help_Text.setSize(30)
    help_Text.draw(window)

    # Draws start menu
    start_Title.draw(window)

    quit_Button = Text(Point(9.5, 10.5), 'Quit')
    quit_Button.setTextColor('red')
    quit_Button.setSize(18)
    quit_Button.setStyle('bold')
    quit_Button.draw(window)

    quit_Box = Rectangle(Point(9, 10.25), Point(10, 10.75))
    quit_Box.setOutline('red')
    quit_Box.draw(window)

    # Determines position of mouse click
    mouse_Position = window.getMouse()
    x = mouse_Position.getX()
    y = mouse_Position.getY()


    # Undraw the Game Window (Quit button)
    if 9 <= x and x <= 10:
        if 10.25 <= y and y <= 10.75:
            window.close()

    # Decides if you click on the multiplayer button
    if x >= 4 and x <= 7:
        if y >= 7 and y <= 8:
            start_Title.undraw()
            multiPlayer.undraw()
            multi_Text.undraw()
            playJoe.undraw()
            joe_Text.undraw()
            help.undraw()
            help_Text.undraw()
            gameWindow(window)

    # Decides if you click on the AI button
    if x >= 4 and x <= 7:
        if y >= 5 and y <= 6:
            start_Title.undraw()
            multiPlayer.undraw()
            multi_Text.undraw()
            playJoe.undraw()
            joe_Text.undraw()
            help.undraw()
            help_Text.undraw()
            gameWindow(window)

    # Decides if you click on the help button
    if x >= 4 and x <= 7:
        if y >= 3 and y <= 4:
            start_Title.undraw()
            multiPlayer.undraw()
            multi_Text.undraw()
            playJoe.undraw()
            joe_Text.undraw()
            help.undraw()
            help_Text.undraw()
            helpWindow(window)

    # if window.getMouse():
    #     start_Title.undraw()
    #     multiPlayer.undraw()
    #     gameWindow(window)

def helpWindow(window):
    #Create title for help menu
    help_Title = Text(Point(5.5, 9.5), 'Help Menu')
    help_Title.setStyle('bold')
    help_Title.setSize(36)
    help_Title.draw(window)


    #Import image of the rules
    rules_Image = Image(Point(5.5, 5.5), 'rules.png')
    rules_Image.draw(window)

    #Creates Quit Button
    quit_Button = Text(Point(9.5, 10.5), 'Quit')
    quit_Button.setTextColor('red')
    quit_Button.setSize(18)
    quit_Button.setStyle('bold')
    quit_Button.draw(window)

    quit_Box = Rectangle(Point(9, 10.25), Point(10, 10.75))
    quit_Box.setOutline('red')
    quit_Box.draw(window)

    quit_position = window.getMouse()
    quit_x = quit_position.getX()
    quit_y = quit_position.getY()

    # Undraw the Game Window
    if 9 <= quit_x and quit_x <= 10:
        if 10.25 <= quit_y and quit_y <= 10.75:
            help_Title.undraw()
            quit_Box.undraw()
            quit_Button.undraw()
            rules_Image.undraw()
            startWindow(window)

########################__DRAW GAME WINDOW__###################################

# creates the game play window with the 9x9 tic-tac-toe board (very nice)
def gameWindow(window):

    # Draw the big board
    BB_line1 = Line(Point(4, 1), Point(4, 10))
    BB_line2 = Line(Point(7, 1), Point(7, 10))
    BB_line3 = Line(Point(1, 4), Point(10, 4))
    BB_line4 = Line(Point(1, 7), Point(10, 7))

    #contains everything on game window
    All = [BB_line1, BB_line2, BB_line3, BB_line4]

    # -------------------------------

    # Draw all the small boards
    for k in range(3):
        for j in range(3):
            for i in range(2):
                line = Line(Point(3 * j + 2 + i, 3 * k + 1.25), Point(3 * j + 2 + i, 3 * k + 3.75))
                All.append(line)
                line = Line(Point(3 * j + 1.25, 3 * k + 2 + i), Point(3 * j + 3.75, 3 * k + 2 + i))
                All.append(line)


    for item in All:
        item.setWidth(3)
        item.draw(window)
    # ---------------------------------

    # Make the Title
    title = Text(Point(5.5, 10.5), 'Ultimate Tic-Tac-Toe')
    title.setStyle('bold')
    title.setSize(24)
    title.draw(window)

    turn = 1
    All.append(title)
    for i in range(81):
        getPosition(window, turn, All)
        turn = (turn + 1) % 2

    quit_Button = Text(Point(9.5, 10.5), 'Quit')
    quit_Button.setTextColor('red')
    quit_Button.setSize(18)
    quit_Button.setStyle('bold')
    quit_Button.draw(window)

    quit_Box = Rectangle(Point(9, 10.25), Point(10, 10.75))
    quit_Box.setOutline('red')
    quit_Box.draw(window)

    quit_position = window.getMouse()
    quit_x = quit_position.getX()
    quit_y = quit_position.getY()

    # Undraw the Game Window
    if 9 <= quit_x and quit_x <= 10:
        if 10.25 <= quit_y and quit_y <= 10.75:
            for item in All:
                item.undraw()
            quit_Box.undraw()
            quit_Button.undraw()
            startWindow(window)

    window.getMouse()

# Connect Back End to Front End by Returning [sb,bb]
# should be edited to impliment user turn ^ drawing to screen
# ---------------------------
def getPosition(window, turn, list):
    mouse = window.getMouse()
    xPos = mouse.getX()
    yPos = mouse.getY()

    bX = checkCoordBig(xPos)
    bY = checkCoordBig(yPos)
    bbPos = bX + 3 * bY
    xTemp = xPos
    yTemp = yPos
    while (xTemp > 4):
        xTemp = xTemp / 3
    while (yTemp > 4):
        yTemp = yTemp / 3

    sX = checkCoordSmall(xTemp)
    sY = checkCoordSmall(yTemp)
    sbPos = sX + 3 * sY
    if sbPos <= 8 and bbPos <= 8:
        print([sbPos, bbPos])
        placeSym(xPos, yPos, turn, window, list)
    else:
        getPosition(window)

# Helper Function for Get Position
# ----------------------------
def checkCoordSmall(pos):
    if (1 <= pos <= 2):
        return 0
    elif (2 < pos <= 3):
        return 1
    elif (3 < pos <= 4):
        return 2
    else:
        return 100

# Helper Function for Get Position
# -----------------------------
def checkCoordBig(pos):
    if (1 <= pos <= 4):
        return 0
    elif (4 < pos <= 7):
        return 1
    elif (7 < pos <= 10):
        return 2
    else:
        return 100


# Function for drawing x's and o's to GUI
#-------------------
def placeSym(xPos, yPos, turn, window, list):
    posX = round(xPos - .5) + .5
    posY = round(yPos - .5) + .5
    if turn == 1:
        ex1 = Line(Point(posX - .4, posY + .4), Point(posX + .4, posY - .4))
        ex2 = Line(Point(posX - .4, posY - .4), Point(posX + .4, posY + .4))
        ex1.draw(window)
        ex2.draw(window)
        list.append(ex1)
        list.append(ex2)
    elif turn == 0:
        oh = Circle(Point(posX, posY), .3)
        oh.draw(window)
        list.append(oh)




main()
