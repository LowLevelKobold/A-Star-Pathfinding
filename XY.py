# utility class that stores and updates XY values to avoid using excesive amounts of arrays
class XYobject:
    X = None
    Y = None

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def setX(self, newX):
        self.X = newX

    def setY(self, newY):
        self.Y = newY

    def setBoth(self, newX, newY):
        self.X = newX
        self.Y = newY

    def __lt__(self, other):
        return self.X+self.Y < other.X+other.Y

    #for testing purposes
    def checkForEqual(self, positionToCompare):
        if not isinstance(positionToCompare, XYobject):
            raise TypeError("the given positions is not a XY class object")

        print("currentX:", self.X, " checkX:", positionToCompare.getX())
        print("currentY:", self.Y, " checkY:", positionToCompare.getY())
        print("                                                         ")
        if self.X == positionToCompare.getX() and self.Y == positionToCompare.getY():
            return True
        else:
            return False