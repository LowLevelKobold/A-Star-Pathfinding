# used to generate the board for movement
# needed to update movemnt and convert map nodes to char
#plus a feature to check nodes neighbours
from XY import XYobject
from AStartNodes import nodeAstar

class GenerateBoard:
    board= []
    row = []
    position = None
    goalPoistion = None

    def __init__(self, boardSizeInput, startingPosition ,targetPosition):
        # checks for incorrect datatypes being used
        if not isinstance(boardSizeInput, XYobject):
            raise TypeError("the board size was not a XY class object")
        elif not isinstance(targetPosition, XYobject):
            raise TypeError("the targetPosition was not a XY class object")
        elif not isinstance(startingPosition, XYobject):
            raise TypeError("the StartingPositon was not a XY class object")

        # checks to see if all entered positions are legal
        elif boardSizeInput.getX() <= 0 or boardSizeInput.getY() <= 0:
            raise SyntaxError("lhe board size is in the negatives ")


        # creates the board an place the position token and target token on the board
        else:

            # set the player position and target position affter they have been checkd
            self.position = startingPosition
            self.goalPoistion = targetPosition
            for i in range(boardSizeInput.getX()):
                for u in range(boardSizeInput.getY()):
                    if (i == startingPosition.getY() and u == startingPosition.getX()):
                        self.row.append(nodeAstar(XYobject(u, i), targetPosition, False, True))
                    elif (i == targetPosition.getY() and u == targetPosition.getX()):
                        self.row.append(nodeAstar(XYobject(u, i), targetPosition, True, False))
                    else:
                        self.row.append(nodeAstar(XYobject(u, i), targetPosition, False, False))
                self.board.append(self.row.copy())
                self.row.clear()
                
            #assignes neighbours
            for p in range(len(self.board)):
                for l in range(len(self.board[0])):

                    nUp = None
                    nDown = None
                    nLeft = None
                    nRight = None


                    if (p != 0 ):
                        nUp = XYobject(l,(p-1))

                    if (p != len(self.board)-1):
                        nDown =  XYobject(l,(p+1))

                    if (l != 0):
                        nLeft = XYobject((l-1),p)

                    if (l != len(self.board[0])-1):
                        nRight = XYobject((l+1),p)

                    self.board[p][l].setNeighbours(nUp, nDown, nLeft, nRight)

    # return the data of the provided node 
    def getNodesNeighbours(self, position):
        if not isinstance(position, XYobject):
            raise TypeError("the given position was not a XY class object")

        holdNodes = self.board[position.getY()][position.getX()].getNeighbours()
        return holdNodes

    def printBoard(self):
        hold = []
        for i in range(len(self.board)):
            for u in range(len(self.board[0])):
                hold.append(self.board[i][u].getState())
            print(hold)
            hold.clear()

    def setStartAndGoal(self, targetPosition, startingPosition):
        if not isinstance(targetPosition, XYobject):
            raise TypeError("the targetPosition was not a XY class object")
        elif not isinstance(startingPosition, XYobject):
            raise TypeError("the StartingPositon was not a XY class object")

        self.position = startingPosition
        self.goalPoistion = targetPosition



    def getStart(self):
        return self.position

    def getGoal(self):
        return self.goalPoistion

    def getPosition(self, position):
        return self.board[position.getY()][position.getX()]

    def getLenWid(self):
        return len(self.board[0]), len(self.board)

    #anything bellow here is for testing purposes
    def getBoard(self):
        textBoard = []
        textRow = []
        for i in range(len(self.board)):
            for u in range(len(self.board[0])):
                textRow.append(self.board[i][u].getState())
            textBoard.append(textRow.copy())
            textRow.clear()
        return textBoard

    def clearBoard(self):
        self.board.clear()
        self.position = None
        self.row.clear()




