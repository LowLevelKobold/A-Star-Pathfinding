# a individual node for the algorithm
from XY import XYobject
import random as r
import math

class nodeAstar:
    weightOfPosition = 0
    carryOverWeight = 0
    distanceToTarget = 0

    parent = None

# these should be XY positions not Nodes
    neighboursTop = None
    neighboursBottom = None
    neighboursLeft = None
    neighboursRight = None

    isTarget = False
    isCurrent = False


    def __init__(self,currentPosition, targetPosition, currentNode , targetNode ):
        if not isinstance(currentPosition, XYobject) and not isinstance(targetPosition, XYobject):
            raise TypeError("a distance entered was not a XYObject ")

        self.isTarget = targetNode
        self.isCurrent = currentNode
        self.weightOfPosition = r.randint(1,10)
        self.distanceToTarget = math.sqrt(
            ((currentPosition.getY() - targetPosition.getY())**2) + ((currentPosition.getX() - targetPosition.getX())**2))

    def getDistanceToTarget(self):
        return self.distanceToTarget



    def getWeight(self):
        return self.weightOfPosition

    def getWeightAndCarryOver(self):
        return self.weightOfPosition + self.carryOverWeight

    def getDisPlusWeight(self):
        return self.distanceToTarget + self.weightOfPosition + self.carryOverWeight

    def setNeighbours(self, up, down, left, right ):
        self.neighboursTop = up
        self.neighboursBottom = down
        self.neighboursLeft = left
        self.neighboursRight = right

    # used in the main algorithmy to backtrack which way the algothym followed
    def setParent(self, currentParent):
        if not isinstance(currentParent, XYobject):
            raise TypeError("Current Parent is not a XYobject")
        else:
            self.parent = currentParent


    # set the parents for tracking


    def getParents(self):
        return self.parent

    # used to carry over weight from there parent node
    def setCarryOverWeight(self, previouseWeight):
        self.carryOverWeight = previouseWeight


    def getNeighbours(self):
        toReturn = []
        hold = [self.neighboursTop, self.neighboursBottom, self.neighboursRight, self.neighboursLeft]
        for i in range(len(hold)):
            if (hold[i] != None):
                toReturn.append(hold[i])
        return toReturn

    def getState(self):
        if self.isCurrent == True:
            return "T"
        elif self.isTarget == True:
            return "P"
        else:
            return str(self.weightOfPosition)


