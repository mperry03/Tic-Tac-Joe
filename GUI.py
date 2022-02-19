from graphics import *

def main():
    win = GraphWin("Tic-Tac-Joe", 800, 800)
    win.setCoords(0, 0, 11, 11)
    BB_line1 = Line(Point(4, 1), Point(4, 10))
    BB_line2 = Line(Point(7, 1), Point(7, 10))
    BB_line3 = Line(Point(1, 4), Point(10, 4))
    BB_line4 = Line(Point(1, 7), Point(10, 7))
    BB_line1.draw(win)
    BB_line2.draw(win)
    BB_line3.draw(win)
    BB_line4.draw(win)

    win.getMouse()
    win.close()

main()


