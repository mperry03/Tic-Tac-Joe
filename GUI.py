from graphics import *
from main.Board import *
import time

def main():

    win = GraphWin("Tic-Tac-Joe", 800, 800)
    win.setCoords(0, 0, 11, 11)
    startWindow(win, 1)

def startWindow(window, first):


    # Set the title for the start menu
    start_Title = Text(Point(5.5, 9.5), 'Ultimate Tic-Tac-Toe')
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
    helps = Rectangle(Point(4, 3), Point(7, 4))
    helps.draw(window)
    help_Text = Text(Point(5.5, 3.5), 'Rules')
    help_Text.setSize(30)
    help_Text.draw(window)

    # Draws start menu
    start_Title.draw(window)

    #instantiate quit button
    #---------------------
    if first:
        quit_Text = Text(Point(9.5, 10.5), 'Quit')
        quit_Text.setTextColor('red')
        quit_Text.setSize(18)
        quit_Text.setStyle('bold')
        quit_Text.draw(window)

        quit_Box = Rectangle(Point(9, 10.25), Point(10, 10.75))
        quit_Box.setOutline('red')
        quit_Box.draw(window)
        first = 0
    #------------------------
    playing = 1

    while playing:
        playing = 0
        mouse = window.getMouse()
        x = mouse.getX()
        y = mouse.getY()

        if (9 <= x <= 10) and (10.25 <= y <= 10.75):
            window.close()

        # Decides if you click on the multiplayer button
        elif (4 <= x <= 7) and (7 <= y <= 8):
            clearScreen(start_Title, multiPlayer, multi_Text, playJoe, joe_Text, helps, help_Text)
            gameWindow(window)


        # Decides if you click on the AI button
        elif (4 <= x <= 7) and (5 <= y <= 6):
            clearScreen(start_Title, multiPlayer, multi_Text, playJoe, joe_Text, helps, help_Text)
            gameWindow(window)
            ## ENABLE AI CAPABILITY

        # Decides if you click on the help button
        elif (4 <= x <= 7) and (3 <= y <= 4):
            clearScreen(start_Title, multiPlayer, multi_Text, playJoe, joe_Text, helps, help_Text)
            helpWindow(window)

        else:
            playing = 1



def helpWindow(window):
    #Create title for help menu
    help_Title = Text(Point(5.5, 9.5), 'Help Menu')
    help_Title.setStyle('bold')
    help_Title.setSize(36)
    help_Title.draw(window)

    #Import image of the rules
    rules_Image = Image(Point(5.5, 5.5), 'rules.png')
    rules_Image.draw(window)

    # Undraw the help Window
    playing = 1
    while playing:
        playing = 0
        if quitCurrentScreen(window):
            help_Title.undraw()
            rules_Image.undraw()
            startWindow(window, 0)

        else:
            playing = 1



########################__DRAW GAME WINDOW__###################################

# creates the game play window with the 9x9 tic-tac-toe board (very nice)
def gameWindow(window):

    bigBoard = instantiate_board(1)


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
    All.append(title)

    #Make Target Boards
    target0 = Rectangle(Point(1, 1), Point(4, 4))
    target1 = Rectangle(Point(4, 1), Point(7, 4))
    target2 = Rectangle(Point(7, 1), Point(10, 4))
    target3 = Rectangle(Point(1, 4), Point(4, 7))
    target4 = Rectangle(Point(4, 4), Point(7, 7))
    target5 = Rectangle(Point(7, 4), Point(10, 7))
    target6 = Rectangle(Point(1, 7), Point(4, 10))
    target7 = Rectangle(Point(4, 7), Point(7, 10))
    target8 = Rectangle(Point(7, 7), Point(10, 10))
    targets = [target0, target1, target2, target3, target4, target5, target6, target7, target8]
    for box in targets:
        box.setOutline('light green')
        box.setWidth(6)
        All.append(box)

    #Make Fillers
    dither = .1
    filler0 = Rectangle(Point(1+dither, 1+dither), Point(4-dither, 4-dither))
    filler1 = Rectangle(Point(4+dither, 1+dither), Point(7-dither, 4-dither))
    filler2 = Rectangle(Point(7+dither, 1+dither), Point(10-dither, 4-dither))
    filler3 = Rectangle(Point(1+dither, 4+dither), Point(4-dither, 7-dither))
    filler4 = Rectangle(Point(4+dither, 4+dither), Point(7-dither, 7-dither))
    filler5 = Rectangle(Point(7+dither, 4+dither), Point(10-dither, 7-dither))
    filler6 = Rectangle(Point(1+dither, 7+dither), Point(4-dither, 10-dither))
    filler7 = Rectangle(Point(4+dither, 7+dither), Point(7-dither, 10-dither))
    filler8 = Rectangle(Point(7+dither, 7+dither), Point(10-dither, 10-dither))
    fillers = [filler0, filler1, filler2, filler3, filler4, filler5, filler6, filler7, filler8]
    for box in fillers:
        box.setFill('white')
        #box.setOutline('black')
        box.setWidth(0)
        All.append(box)

    superFiller = Rectangle(Point(.9,0),Point(10.2,10.2))
    superFiller.setFill('white')
    superFiller.setWidth(0)
    All.append(superFiller)


    #Make Turn Statements
    turn_text1 = Text(Point(5.5, .75), 'It is P1s turn.')
    turn_text1.setSize(20)
    turn_text1.draw(window)
    turn_text2 = Text(Point(5.5, .75), 'It is P2s turn.')
    turn_text2.setSize(20)

    All.append(turn_text1)
    All.append(turn_text2)

    turn = 1
    playing = 1
    while playing:
        mouse = window.getMouse()
        xPos = mouse.getX()
        yPos = mouse.getY()
        vals = getPosition(xPos, yPos)
        if turn:
            player = 'X'
        else:
            player = 'O'
        if vals.getX() <= 8 and vals.getY() <= 8:
            place = [int(vals.getX()),int(vals.getY())]
            validMove = bigBoard.make_move(place, player)
            if validMove:
                turnStatement(window, turn, turn_text1, turn_text2)
                placeSym(xPos, yPos, turn, window, All)
                statusArray = bigBoard.get_subboard_states()
                decidedBoard(window, fillers, statusArray, All)
                winStatus = bigBoard.get_state()
                validBoards = bigBoard.get_valid_boards()
                targetBoard(window, targets, validBoards)
                checkWin(window, superFiller, winStatus, targets, All)
                turn = (turn + 1) % 2


        # Undraw the Game Window
        elif (9 <= xPos <= 10) and (10.25 <= yPos <= 10.75):
            for item in All:
                playing = 0
                item.undraw()
            startWindow(window, 0)


# Connect Back End to Front End by Returning [sb,bb]
# should be edited to impliment user turn ^ drawing to screen
# ---------------------------
def getPosition(xPos, yPos):

        bX = checkCoordBig(xPos)
        bY = checkCoordBig(yPos)
        bbPos = bX + 3 * bY
        xTemp = xPos
        yTemp = yPos
        while (xTemp > 4):
            xTemp = xTemp - 3
        while (yTemp > 4):
            yTemp = yTemp - 3

        sX = checkCoordSmall(xTemp)
        sY = checkCoordSmall(yTemp)
        sbPos = sX + 3 * sY

        return Point(sbPos, bbPos)

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
        ex1 = Line(Point(posX - .3, posY + .3), Point(posX + .3, posY - .3))
        ex2 = Line(Point(posX - .3, posY - .3), Point(posX + .3, posY + .3))
        ex1.setWidth(4)
        ex2.setWidth(4)
        ex1.setOutline('red')
        ex2.setOutline('red')
        ex1.draw(window)
        ex2.draw(window)
        list.append(ex1)
        list.append(ex2)
    elif turn == 0:
        oh = Circle(Point(posX, posY), .3)
        oh.setWidth(4)
        oh.setOutline('blue')
        oh.draw(window)
        list.append(oh)

def quitCurrentScreen(window):

    quit_position = window.getMouse()
    quit_x = quit_position.getX()
    quit_y = quit_position.getY()

    return (9 <= quit_x <= 10) and (10.25 <= quit_y <= 10.75)

def clearScreen(start_Title, multiPlayer, multi_Text, playJoe, joe_Text, helps, help_Text):
    start_Title.undraw()
    multiPlayer.undraw()
    multi_Text.undraw()
    playJoe.undraw()
    joe_Text.undraw()
    helps.undraw()
    help_Text.undraw()

def turnStatement(window, turn, turn_text1, turn_text2 ):
    if turn==1:
        turn_text1.undraw()
        turn_text2.draw(window)
    elif turn==0:
        turn_text2.undraw()
        turn_text1.draw(window)


def targetBoard(window, targetArray, playables):
    for i in range(9):
        targetArray[i].undraw()
        if playables[i]:
            targetArray[i].draw(window)


def decidedBoard(window, fillerArray, boardStates, list):
    for i in range(9):
        if boardStates[i] != '_':
            fillerArray[i].undraw()
            fillerArray[i].draw(window)
            yPos = (i // 3)*3 + 2.5
            xPos = (i % 3)*3 + 2.5

            if boardStates[i] == 'X':
                c = 1.25
                ex1 = Line(Point(xPos-c,yPos+c),Point(xPos+c,yPos-c))
                ex2 = Line(Point(xPos+c,yPos+c),Point(xPos-c,yPos-c))
                list.append(ex1)
                list.append(ex2)
                ex1.setWidth(8)
                ex2.setWidth(8)
                ex1.setOutline('red')
                ex2.setOutline('red')
                ex1.draw(window)
                ex2.draw(window)

            elif boardStates[i] == 'O':
                oh = Circle(Point(xPos,yPos),1.25)
                list.append(oh)
                oh.setWidth(8)
                oh.setOutline('blue')
                oh.draw(window)
            else:
                dash = Line(Point(xPos-1,yPos), Point(xPos+1, yPos))
                list.append(dash)
                dash.setWidth(8)
                dash.draw(window)


def checkWin(window, fill, status, targets, list):
    if status != '_':
        time.sleep(1)
        fill.draw(window)
        for box in targets:
            box.undraw()
        if status == 'X':
            ex1 = Line(Point(2.5,8.5),Point(8.5,2.5))
            ex2 = Line(Point(2.5,2.5),Point(8.5,8.5))
            ex1.setWidth(10)
            ex2.setWidth(10)
            ex1.setOutline('red')
            ex2.setOutline('red')
            ex1.draw(window)
            ex2.draw(window)
            list.append(ex1)
            list.append(ex2)
            xWin = Text(Point(5.5, 1.75), 'Player One Wins!')
            list.append(xWin)
            xWin.setSize(34)
            xWin.draw(window)
        elif status == 'O':
            oh = Circle(Point(5.5,5.5),3)
            oh.setWidth(10)
            oh.setOutline('blue')
            oh.draw(window)
            list.append(oh)
            oWin = Text(Point(5.5, 1.75), 'Player Two Wins!')
            list.append(oWin)
            oWin.setSize(34)
            oWin.draw(window)
        else:
            dash = Line(Point(2.5, 5.5), Point(8.5, 5.5))
            dash.setWidth(10)
            dash.draw(window)
            list.append(dash)
            draw = Text(Point(5.5, 1.75), 'Its a Draw!')
            list.append(draw)
            draw.setSize(34)
            draw.draw(window)




main()
