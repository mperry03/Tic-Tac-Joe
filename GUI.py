from graphics import *
# from main.Board import *
import time
# import random
from main.tictacjoe import *


def main():
    # Create Window
    win = GraphWin("Tic-Tac-Joe", 800, 800)
    win.setCoords(0, 0, 11, 11)
    startWindow(win, 1)


# #######################__DRAW Start WINDOW__###################################
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

    # instantiate quit button
    # ---------------------
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

    # ------------------------
    playing = 1

    # Wait for user mouse click
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
            gameWindow(window, False)

        # Decides if you click on the AI button
        elif (4 <= x <= 7) and (5 <= y <= 6):
            clearScreen(start_Title, multiPlayer, multi_Text, playJoe, joe_Text, helps, help_Text)
            gameWindow(window, True)

        # Decides if you click on the help button
        elif (4 <= x <= 7) and (3 <= y <= 4):
            clearScreen(start_Title, multiPlayer, multi_Text, playJoe, joe_Text, helps, help_Text)
            helpWindow(window)

        else:
            playing = 1


# #######################__DRAW Help WINDOW__###################################
def helpWindow(window):
    help_Title = Text(Point(5.5, 9.5), 'Help Menu')
    help_Title.setStyle('bold')
    help_Title.setSize(36)
    help_Title.draw(window)

    # Import image of the rules and example
    rules_Image = Image(Point(5.5, 7), 'rules.png')
    rules_Image.draw(window)
    example_Image = Image(Point(5.5, 3), 'example.png')
    example_Image.draw(window)

    # Un-draw the help Window
    playing = 1
    while playing:
        playing = 0
        if quitCurrentScreen(window):
            help_Title.undraw()
            rules_Image.undraw()
            example_Image.undraw()
            startWindow(window, 0)

        else:
            playing = 1


# #######################__DRAW GAME WINDOW__###################################
# creates the game play window with the 9x9 tic-tac-toe board (very nice)
def gameWindow(window, ai):

    bigBoard = instantiate_board(1)
    joe = instantiate_AI()

    # Draw the big board
    BB_line1 = Line(Point(4, 1), Point(4, 10))
    BB_line2 = Line(Point(7, 1), Point(7, 10))
    BB_line3 = Line(Point(1, 4), Point(10, 4))
    BB_line4 = Line(Point(1, 7), Point(10, 7))

    # contains everything on game window
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

    # Make Target Boards
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

    # DRAW FILLERS AUTOMATICALLY WITH SHAPE?

    # Make Fillers
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
    drawn = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for box in fillers:
        box.setFill('white')
        box.setWidth(0)
        All.append(box)

    # Filler for completed game
    superFiller = Rectangle(Point(.9, 0), Point(10.2, 10.2))
    superFiller.setFill('white')
    superFiller.setWidth(0)
    All.append(superFiller)

    # Make Turn Statements
    turn_text1 = Text(Point(5.5, .75), 'It is P1s turn.')
    turn_text1.setSize(20)
    turn_text1.draw(window)
    turn_text2 = Text(Point(5.5, .75), 'It is P2s turn.')
    turn_text2.setSize(20)

    All.append(turn_text1)
    All.append(turn_text2)

    # Track the game to make updates to the boards
    turn = 1
    playing = 1
    while playing:
        vals = Point(0, 0)
        xPos = 0
        yPos = 0
        if (not ai) or (turn == 1):
            mouse = window.getMouse()
            xPos = mouse.getX()
            yPos = mouse.getY()
            vals = getPosition(xPos, yPos)
        if turn:
            player = 'X'
        else:
            player = 'O'
        if (vals.getX() <= 8 and vals.getY() <= 8) or (AI and player == 'O'):
            if (not ai) or (player == 'X'):
                place = [int(vals.getX()), int(vals.getY())]
            else:
                time.sleep(1 + random.random())
                place = joe.chooseMove(bigBoard)
                small = place[0]
                big = place[1]
                bY = big // 3
                bX = big % 3
                sY = small // 3
                sX = small % 3
                xPos = 3*bX + sX + 1.49
                yPos = 3*bY + sY + 1.49

            validMove = bigBoard.make_move(place, player)
            if validMove:
                turnStatement(window, turn, turn_text1, turn_text2)
                placeSym(xPos, yPos, turn, window, All)
                statusArray = bigBoard.get_board_states()
                decidedBoard(window, fillers, drawn, statusArray, All)
                winStatus = bigBoard.get_state()
                validBoards = bigBoard.get_valid_boards()
                targetBoard(window, targets, validBoards)
                playing = checkWin(window, superFiller, winStatus, targets, All, joe)
                turn = (turn + 1) % 2

        # Un-draw the Game Window
        elif (9 <= xPos <= 10) and (10.25 <= yPos <= 10.75):
            rect = Rectangle(Point(.9, 0), Point(10.2, 10.2))
            rect.setWidth(0)
            rect.setFill('white')
            rect.draw(window)
            for item in All:
                playing = 0
                item.undraw()
                End = False
            rect.undraw()
            startWindow(window, 0)

    End = True
    while End:
        mouse = window.getMouse()
        xPos = mouse.getX()
        yPos = mouse.getY()
        if (9 <= xPos <= 10) and (10.25 <= yPos <= 10.75):
            rect = Rectangle(Point(.9, 0), Point(10.2, 10.2))
            rect.setWidth(0)
            rect.setFill('white')
            rect.draw(window)
            for item in All:
                playing = 0
                item.undraw()
            End = False
            rect.undraw()
            startWindow(window, 0)

# Connect Back End to Front End by Returning [sb,bb]
# should be edited to implement user turn ^ drawing to screen
# ---------------------------


# Get position of mouse click
def getPosition(xPos, yPos):

    bX = checkCoordBig(xPos)
    bY = checkCoordBig(yPos)
    bbPos = bX + 3 * bY
    xTemp = xPos
    yTemp = yPos
    while xTemp > 4:
        xTemp = xTemp - 3
    while yTemp > 4:
        yTemp = yTemp - 3

    sX = checkCoordSmall(xTemp)
    sY = checkCoordSmall(yTemp)
    sbPos = sX + 3 * sY

    return Point(sbPos, bbPos)


# Helper Function for Get Position
# ----------------------------
def checkCoordSmall(pos):
    if 1 <= pos <= 2:
        return 0
    elif 2 < pos <= 3:
        return 1
    elif 3 < pos <= 4:
        return 2
    else:
        return 100


# Helper Function for Get Position
# -----------------------------
def checkCoordBig(pos):
    if 1 <= pos <= 4:
        return 0
    elif 4 < pos <= 7:
        return 1
    elif 7 < pos <= 10:
        return 2
    else:
        return 100


# Function for drawing x's and o's to GUI
# -------------------
def placeSym(xPos, yPos, turn, window, ls):
    posX = round(xPos - .5) + .5
    posY = round(yPos - .5) + .5
    if turn == 1:
        draw_shape(window, posX, posY, .3, 4, 'X', ls)
    elif turn == 0:
        draw_shape(window, posX, posY, .3, 4, 'O', ls)


# Determines if the quit button was clicked
def quitCurrentScreen(window):

    quit_position = window.getMouse()
    quit_x = quit_position.getX()
    quit_y = quit_position.getY()

    return (9 <= quit_x <= 10) and (10.25 <= quit_y <= 10.75)


# Clears screen of shapes and text
def clearScreen(start_Title, multiPlayer, multi_Text, playJoe, joe_Text, helps, help_Text):
    start_Title.undraw()
    multiPlayer.undraw()
    multi_Text.undraw()
    playJoe.undraw()
    joe_Text.undraw()
    helps.undraw()
    help_Text.undraw()


# Prints whose turn it is
def turnStatement(window, turn, turn_text1, turn_text2):
    if turn == 1:
        turn_text1.undraw()
        turn_text2.draw(window)
    elif turn == 0:
        turn_text2.undraw()
        turn_text1.draw(window)


# Highlights the playable boards
def targetBoard(window, targetArray, playables):
    for i in range(9):
        targetArray[i].undraw()
        if playables[i]:
            targetArray[i].draw(window)


# Updates the boards with the symbols for each player
def decidedBoard(window, fillerArray, fillerDrawn, boardStates, ls):
    for i in range(9):
        if boardStates[i] != '_':
            print(boardStates[i])
            if fillerDrawn[i] == 0:
                fillerArray[i].draw(window)
                fillerDrawn[i] = 1
            yPos = (i // 3)*3 + 2.5
            xPos = (i % 3)*3 + 2.5

            # Adds a red X to board for player 1
            if boardStates[i] == 'X':
                draw_shape(window, xPos, yPos, 1.25, 8, 'X', ls)

            # Adds a blue O to board for player 2
            elif boardStates[i] == 'O':
                draw_shape(window, xPos, yPos, 1.25, 8, 'O', ls)

            # Adds a dash through small board if the game is drawn
            else:
                draw_shape(window, xPos, yPos, 1, 8, 'T', ls)


def checkWin(window, fill, status, targets, ls, joe):
    val = 1
    if status != '_':
        time.sleep(1)
        val = 0
        joe.setState(False)
        fill.draw(window)
        for box in targets:
            box.undraw()
        draw_shape(window, 5.5, 5.5, 3, 10, status, ls)

        if status == 'X':
            Win = Text(Point(5.5, 1.75), 'Player One Wins!')

        elif status == 'O':
            Win = Text(Point(5.5, 1.75), 'Player Two Wins!')

        else:
            Win = Text(Point(5.5, 1.75), 'Its a Draw!')

        ls.append(Win)
        Win.setSize(34)
        Win.draw(window)

    return val


def draw_shape(window, xPos, yPos, scale, width, shape, ls):
    # draw a background
    if shape == 'X':
        ex1 = Line(Point(xPos - scale, yPos + scale), Point(xPos + scale, yPos - scale))
        ex2 = Line(Point(xPos + scale, yPos + scale), Point(xPos - scale, yPos - scale))
        ls.append(ex1)
        ls.append(ex2)
        ex1.setWidth(width)
        ex2.setWidth(width)
        ex1.setOutline('red')
        ex2.setOutline('red')
        ex1.draw(window)
        ex2.draw(window)
    elif shape == 'O':
        oh = Circle(Point(xPos, yPos), scale)
        oh.setWidth(width)
        oh.setOutline('blue')
        oh.draw(window)
        ls.append(oh)
    else:
        dash = Line(Point(xPos-scale, yPos), Point(xPos+scale, yPos))
        dash.setWidth(width)
        dash.draw(window)
        ls.append(dash)


main()
