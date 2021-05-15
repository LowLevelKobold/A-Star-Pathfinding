#this is used to generate multiple custom buttons

from XY import XYobject
from boundsChecker import boundChecker
import pygame

class Button:

    xyPosition = None
    xySize = None
    clicked = False

    def __init__(self, XYPosition, XYSize):

        # checks for incorrect datatypes being used
        if not isinstance(XYPosition, XYobject):
            raise TypeError("the XYPosition was not a XY class object")
        if not isinstance(XYSize, XYobject):
            raise TypeError("the XYSize was not a XY class object")

        self.xyPosition = XYPosition
        self.xySize = XYSize



    def display(self,windowToDisplayOn, mousePos, mouseClicked):

        utilty = boundChecker()
        # clicked
        if utilty.checkIfInBounds(self.xyPosition,self.xySize,mousePos) == True and mouseClicked == True:
            pygame.draw.rect(windowToDisplayOn, (245, 179, 83),
                             (self.xyPosition.getX(), self.xyPosition.getY()
                              , self.xySize.getX(), self.xySize.getY()))

            if (self.clicked == True):
                self.clicked = False
                return True
        # hover
        elif (utilty.checkIfInBounds(self.xyPosition,self.xySize,mousePos) == True and mouseClicked == False):
            pygame.draw.rect(windowToDisplayOn, (245, 169, 59),
                             (self.xyPosition.getX(), self.xyPosition.getY()
                              , self.xySize.getX(), self.xySize.getY()))
            self.clicked = True

        # base
        else:
            pygame.draw.rect(windowToDisplayOn, (247, 159, 31),
                             (self.xyPosition.getX(), self.xyPosition.getY()
                              , self.xySize.getX(), self.xySize.getY()))
            self.clicked = False
        return False




