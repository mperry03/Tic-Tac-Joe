from graphics import *

def main():

    win = GraphWin("Tic-Tac-Joe", 800, 800)
    win.setCoords(0, 0, 11, 11)
    startWindow(win)

def startWindow(window):
    start_Title = Text(Point(5.5, 9.5), 'Menu')
    start_Title.setStyle('bold')
    start_Title.setSize(36)
    multiPlayer = Rectangle(Point(4, 4), Point(7, 7))
    multiPlayer.draw(window)
    start_Title.draw(window)
    if window.getMouse():
        start_Title.undraw()
        gameWindow(window)

def helpWindow(window):
    help_Title = Text(Point(5.5, 9.5), 'Help Menu')
    help_Title.setStyle('bold')
    help_Title.setSize(36)
    help_Title.draw(window)

def gameWindow(window):
    BB_line1 = Line(Point(4, 1), Point(4, 10))
    BB_line2 = Line(Point(7, 1), Point(7, 10))
    BB_line3 = Line(Point(1, 4), Point(10, 4))
    BB_line4 = Line(Point(1, 7), Point(10, 7))

    BB = [BB_line1, BB_line2, BB_line3, BB_line4]
    for item in BB:
        item.setWidth(3)
        item.draw(window)

    SB = []
    for k in range(3):
        for j in range(3):
            for i in range(2):
                line = Line(Point(3 * j + 2 + i, 3 * k + 1.25), Point(3 * j + 2 + i, 3 * k + 3.75))
                SB.append(line)
                line = Line(Point(3 * j + 1.25, 3 * k + 2 + i), Point(3 * j + 3.75, 3 * k + 2 + i))
                SB.append(line)

    for item in SB:
        item.setWidth(3)
        item.draw(window)

    title = Text(Point(5.5, 10.5), 'Ultimate Tic-Tac-Toe')
    title.setStyle('bold')
    title.setSize(24)
    title.draw(window)

    window.getMouse()
    #window.close()

main()


