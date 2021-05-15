from XY import XYobject

class boundChecker:

    def checkIfInBounds(self, boxPos, boxSize, checkPos):
        if not isinstance(boxPos, XYobject):
            raise TypeError("the boxPos was not a XY class object")
        if not isinstance(boxSize, XYobject):
            raise TypeError("the boxSize was not a XY class object")
        if not isinstance(checkPos, XYobject):
            raise TypeError("the checkPos was not a XY class object")

        if ((boxPos.getX() < checkPos.getX() and checkPos.getX() < boxPos.getX()+boxSize.getX()) and
        (boxPos.getY() < checkPos.getY() and checkPos.getY() < boxPos.getY()+boxSize.getY())):
            return True
        else:
            return False