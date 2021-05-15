# used for the individual squares in the visual side of the code
import pygame
from XY import XYobject
from boundsChecker import boundChecker


class GridSquare:
    position = None
    currentState = 0
    gap = 30

    def __init__(self, pos):
        if not isinstance(pos, XYobject):
            raise TypeError("the pos was not a XY class object")
        self.position = pos

    def display(self, win , rightMouse, leftMouse, mousePos):
        returnValue = 0

        utilty = boundChecker()
        if utilty.checkIfInBounds(self.position, XYobject(self.gap, self.gap), mousePos) == True and rightMouse == True:
            self.currentState = 2
            returnValue = 1
        if utilty.checkIfInBounds(self.position, XYobject(self.gap, self.gap), mousePos) == True and leftMouse == True:
            self.currentState = 3
            returnValue = 3

        # state 0,1,2,3
        # not being used square (state 0)
        if (self.currentState == 0):
            pygame.draw.rect(win, (30, 30, 30), (self.position.getX()
                                                  , self.position.getY(), self.gap,self.gap))
        # path square (state 1)
        elif (self.currentState == 1):
            pygame.draw.rect(win, (245, 169, 59), (self.position.getX()
                                                  , self.position.getY(), self.gap,self.gap))
        # start of path square (state 2)
        elif (self.currentState == 2):
            pygame.draw.rect(win, (255, 15, 0), (self.position.getX()
                                                  , self.position.getY(), self.gap,self.gap))
        # end of path square (state 3)
        else:
            pygame.draw.rect(win, (25, 255, 0), (self.position.getX()
                                                  , self.position.getY(), self.gap,self.gap))

        return returnValue



    def changeState (self,state):
        if not isinstance(state, int):
            raise TypeError("the state was not a integer")

        if (state > 3 or state < 0):
            raise TypeError("the state was not a integer")

        self.currentState = state
