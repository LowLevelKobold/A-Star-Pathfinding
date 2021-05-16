# used as the main visual canvas

import pygame

from AStarPathFinding import AstarPathFinding
from Button import Button
from GenerateBoard import GenerateBoard
from XY import XYobject
from GridSquare import GridSquare


class VisualElement:
    whiteColor = (230, 230, 230)

    def __init__(self, boardSize, widthOfBoard, lengthOfBoard):
        trackerWidth = 3
        trackerLength = 3
        gap = 30
        
        color = (100,100,100)

        pygame.init()

        win = pygame.display.set_mode((666, 505))

        win.fill(color)
        pygame.display.set_caption("A star pathfinding")

        # text setup
        pygame.display.set_caption('Show Text')
        font = pygame.font.Font(None,  32)
        fontSmall = pygame.font.Font(None, 22)
        fontForWeights = pygame.font.Font(None, 16)

        start,text =self.textGenertor(font, XYobject (107, 30), 'Draw')
        clearTex, text1 =self.textGenertor(font, XYobject(329, 30), 'Clear')
        reset, text2 = self.textGenertor(font, XYobject(551, 30), 'Reset')
        startPosText, text3 = self.textGenertor(fontSmall, XYobject(97, 75), 'Start Position: NA, NA')
        endPosText, text4 = self.textGenertor(fontSmall, XYobject(317,  75), 'End Position: NA , NA')
        totalText, text5 = self.textGenertor(fontSmall, XYobject(531,   75), 'Path Length: NA')

        # text for


        loop = True
        runNeedClear = False
        startPoint = None
        targetPoint = None

        buttonSize = XYobject(190,40)

        startButton = Button(XYobject(17,  10), XYobject(buttonSize.getX(), buttonSize.getY()))
        clearButton = Button(XYobject(237, 10), XYobject(buttonSize.getX(), buttonSize.getY()))
        reloadButton = Button(XYobject(457,10), XYobject(buttonSize.getX(), buttonSize.getY()))

        holdVisBoard = []
        temp = []
        holdBoard = GenerateBoard(boardSize)

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

            holdWeights = holdBoard.getWeights()

            pygame.draw.rect(win, (115, 115, 115), (0, 0, 666, 104))

            # grid display
            for i in range(lengthOfBoard):
                for u in range(widthOfBoard):
                    if (holdVisBoard[i][u].display(win, rightMouse, leftMouse, mousePos, holdWeights[u][i], fontForWeights) == 1):
                        if (targetPoint != None):
                            holdVisBoard[targetPoint.getX()][targetPoint.getY()].changeState(0)
                            holdVisBoard[targetPoint.getX()][targetPoint.getY()].display(win, rightMouse, leftMouse,
                                                                                         mousePos, holdWeights[u][i], fontForWeights)

                            if (runNeedClear == True):
                                for l in range(len(holdPath)):
                                    holdVisBoard[holdPath[l].getX()][holdPath[l].getY()].changeState(0)
                                holdPath.clear()
                                runNeedClear = False
                                startPosText, text3 = self.textGenertor(fontSmall, XYobject(97, 75),
                                                                        'Start Position: NA, NA')
                                totalText, text5 = self.textGenertor(fontSmall, XYobject(531, 75), 'Path Length: NA')


                        targetPoint = XYobject(i, u)
                        tempText = "End Position X:" + str(i+1) + " Y:" + str(u+1)
                        endPosText, text4 =self.textGenertor(fontSmall, XYobject(317,  75)
                                                                , tempText)

                    if (holdVisBoard[i][u].display(win, rightMouse, leftMouse, mousePos ,holdWeights[u][i], fontForWeights) == 3):
                        if (startPoint != None):
                            holdVisBoard[startPoint.getX()][startPoint.getY()].changeState(0)
                            holdVisBoard[startPoint.getX()][startPoint.getY()].display(win, rightMouse, leftMouse,
                                                                                       mousePos, holdWeights[u][i], fontForWeights)
                            if (runNeedClear == True):
                                for l in range(len(holdPath)):
                                    holdVisBoard[holdPath[l].getX()][holdPath[l].getY()].changeState(0)
                                holdPath.clear()
                                runNeedClear = False
                                endPosText, text4 = self.textGenertor(fontSmall, XYobject(317, 75),
                                                                      'End Position: NA , NA')
                                totalText, text5 = self.textGenertor(fontSmall, XYobject(531, 75), 'Path Length: NA')

                        startPoint = XYobject(i, u)
                        tempText = "Start Position X:" + str(i+1) + " Y:" + str(u+1)
                        startPosText, text3 = self.textGenertor(fontSmall, XYobject(97, 75)
                                                                , tempText)


        # buttons bar
            if (clearButton.display(win, mousePos, leftMouse) == True):
                for i in range(lengthOfBoard):
                    for u in range(widthOfBoard):
                        holdVisBoard[i][u].changeState(0)

                # reset points
                startPoint = None
                targetPoint = None

                # rest text
                startPosText, text3 = self.textGenertor(fontSmall, XYobject(97, 75), 'Start Position: NA, NA')
                endPosText, text4 = self.textGenertor(fontSmall, XYobject(317, 75), 'End Position: NA , NA')
                totalText, text5 = self.textGenertor(fontSmall, XYobject(531, 75), 'Path Length: NA')

            if (reloadButton.display(win, mousePos, leftMouse) == True):
                holdBoard.clearBoard()
                del holdBoard
                holdBoard = GenerateBoard(boardSize)

                for i in range(lengthOfBoard):
                    for u in range(widthOfBoard):
                        holdVisBoard[i][u].changeState(0)

                # reset points
                startPoint = None
                targetPoint = None

                #reset text
                startPosText, text3 = self.textGenertor(fontSmall, XYobject(97, 75), 'Start Position: NA, NA')
                endPosText, text4 = self.textGenertor(fontSmall, XYobject(317, 75), 'End Position: NA , NA')
                totalText, text5 = self.textGenertor(fontSmall, XYobject(531, 75), 'Path Length: NA')


            if (startButton.display(win, mousePos, leftMouse) == True
                    and startPoint != None and targetPoint != None):


                for i in range(lengthOfBoard):
                    for u in range(widthOfBoard):
                        holdVisBoard[i][u].changeState(0)

                holdBoard.setStartAndGoal(targetPoint, startPoint)
                holdAlgo = AstarPathFinding(holdBoard)
                holdPath = holdAlgo.lookForPath()

                tempText = "Path Length: " + str(len(holdPath) -1)
                totalText, text5 = self.textGenertor(fontSmall, XYobject(531, 75), tempText)

                # keeps the weight consistant
                holdWeights = holdBoard.getWeights()
                holdBoard.clearBoard()

                del holdBoard
                del holdAlgo
                holdBoard = GenerateBoard(boardSize)
                holdBoard.changesWeight(holdWeights.copy())

                holdWeights.clear()

                for l in range(len(holdPath)):
                    holdVisBoard[holdPath[l].getX()][holdPath[l].getY()].changeState(1)

                runNeedClear = True

#

# buttons text display

            win.blit(text, start)
            win.blit(text1, clearTex)
            win.blit(text2, reset)
            win.blit(text3, startPosText)
            win.blit(text4, endPosText)
            win.blit(text5, totalText)



    def textGenertor(self, font, xy, text):
        textValue = font.render(str(text), True, self.whiteColor, None)
        hold = textValue.get_rect()
        hold.center = (xy.getX(), xy.getY())
        return hold, textValue



