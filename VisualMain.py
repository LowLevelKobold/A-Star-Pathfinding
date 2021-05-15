# used as the main visual canvas

import pygame

from AStarPathFinding import AstarPathFinding
from Button import Button
from GenerateBoard import GenerateBoard
from XY import XYobject
from GridSquare import GridSquare


class VisualElement:

    def __init__(self, boardSize, widthOfBoard, lengthOfBoard):
        trackerWidth = 3
        trackerLength = 3
        gap = 30
        color = (100,100,100)
        whiteColor = (230,230,230)
        orangeColor = (247, 159, 31)

        pygame.init()
        win = pygame.display.set_mode((666, 505))
        win.fill(color)
        pygame.display.set_caption("A star pathfinding")

        # text
        pygame.display.set_caption('Show Text')

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('draw', True, whiteColor , orangeColor)
        start = text.get_rect()
        start.center = (81, 50)

        text1 = font.render('clear', True, whiteColor, orangeColor)
        clearTex = text1.get_rect()
        clearTex.center = (247, 50)

        text2 = font.render('maze', True, whiteColor, orangeColor)
        maze = text2.get_rect()
        maze.center = (414, 50)

        text3 = font.render('reset', True, whiteColor, orangeColor)
        reset = text3.get_rect()
        reset.center = (580, 50)


        loop = True
        runNeedClear = False
        startPoint = None
        targetPoint = None

        startButton = Button(XYobject(0, 0), XYobject(166, 103))
        clearButton = Button(XYobject(166, 0), XYobject(167, 103))
        mazeButton = Button(XYobject(333, 0), XYobject(166, 103))
        reloadButton = Button(XYobject(499, 0), XYobject(166, 103))
        holdVisBoard = []
        temp = []

        # generates the inital grid objects
        for i in range(lengthOfBoard):
            for u in range(widthOfBoard):
                temp.append(GridSquare(XYobject(0 + trackerWidth, 105 + trackerLength)))
                trackerWidth = trackerWidth + gap + 3
            holdVisBoard.append(temp.copy())
            temp.clear()
            trackerWidth = 3
            trackerLength = trackerLength + gap + 3

        # visual loop used to display objects
        while loop:
            pygame.time.delay(100)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    loop = False
            pygame.display.update()

            # mouse infomation
            mouseX, mouseY = pygame.mouse.get_pos()
            mousePos = XYobject(mouseX, mouseY)
            leftMouse, centerMouse, rightMouse = pygame.mouse.get_pressed()

            # grid display
            for i in range(lengthOfBoard):
                for u in range(widthOfBoard):
                    if (holdVisBoard[i][u].display(win, rightMouse, leftMouse, mousePos) == 1):
                        if (targetPoint != None):
                            holdVisBoard[targetPoint.getX()][targetPoint.getY()].changeState(0)
                            holdVisBoard[targetPoint.getX()][targetPoint.getY()].display(win, rightMouse, leftMouse,
                                                                                         mousePos)

                            if (runNeedClear == True):
                                for l in range(len(holdPath)):
                                    holdVisBoard[holdPath[l].getX()][holdPath[l].getY()].changeState(0)
                                holdPath.clear()
                                runNeedClear = False


                        targetPoint = XYobject(i, u)

                    if (holdVisBoard[i][u].display(win, rightMouse, leftMouse, mousePos) == 3):
                        if (startPoint != None):
                            holdVisBoard[startPoint.getX()][startPoint.getY()].changeState(0)
                            holdVisBoard[startPoint.getX()][startPoint.getY()].display(win, rightMouse, leftMouse,
                                                                                       mousePos)
                            if (runNeedClear == True):
                                for l in range(len(holdPath)):
                                    holdVisBoard[holdPath[l].getX()][holdPath[l].getY()].changeState(0)
                                holdPath.clear()
                                runNeedClear = False

                        startPoint = XYobject(i, u)


        # buttons bar
            if (clearButton.display(win, mousePos, leftMouse) == True):
                for i in range(lengthOfBoard):
                    for u in range(widthOfBoard):
                        holdVisBoard[i][u].changeState(0)
                startPoint = None
                targetPoint = None

            if (mazeButton.display(win, mousePos, leftMouse) == True
                    and startPoint != None and targetPoint != None):
                print("test 2")

            if (reloadButton.display(win, mousePos, leftMouse) == True
                    and startPoint != None and targetPoint != None):
                print("print 1")


            if (startButton.display(win, mousePos, leftMouse) == True
                    and startPoint != None and targetPoint != None):


                for i in range(lengthOfBoard):
                    for u in range(widthOfBoard):
                        holdVisBoard[i][u].changeState(0)

                holdBoard = GenerateBoard(boardSize, startPoint, targetPoint)
                holdAlgo = AstarPathFinding(holdBoard)
                holdPath = holdAlgo.lookForPath()

                holdBoard.clearBoard()

                del holdBoard
                del holdAlgo
     
                for l in range(len(holdPath)):
                    holdVisBoard[holdPath[l].getX()][holdPath[l].getY()].changeState(1)

                runNeedClear = True


            win.blit(text, start)
            win.blit(text1, clearTex)
            win.blit(text2, maze)
            win.blit(text3, reset)
