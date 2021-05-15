#for the actually algorithmy
from GenerateBoard import GenerateBoard
from PriorityQueue import PriorityQueue
from XY import XYobject

class AstarPathFinding:
    currentBoard = None

    def __init__(self, board):
        # check to make sure the correct datatype is being given
        if not isinstance(board, GenerateBoard):
            raise TypeError("the board  was not a GenerateBoard class object")
        else:
            self.currentBoard = board

    def lookForPath(self):
        # this genertate the ques then asignes the first node to it
        holdStart = self.currentBoard.getStart()
        currentCanidate = None

        openlist = PriorityQueue()
        closedList = PriorityQueue()
        closedListTraker = 1

        # deal with a generation problem where if the algorithym is called more then once it  rembers previouse calls
        if (openlist.checkSize() > 1):
            openlist.clear()
            closedList.clear()

        openlist.push(holdStart, 1)

        #this is where the algorithym will atempt to find the correct path
        while openlist.checkSize() > 0:
            if currentCanidate != None:
                # tracls the closed list so it can determine if a object was used by it and for display purposes latter on
                closedList.push(currentCanidate, closedListTraker)
                closedListTraker = closedListTraker +1

            currentCanidate = openlist.pull()

            # reached goal returns list of positiosn to be converted into visual elements
            if (self.currentBoard.getGoal().getY() == currentCanidate.getY())and(self.currentBoard.getGoal().getX() == currentCanidate.getX()):
                finalPath = []
                finalPath.append(self.currentBoard.getGoal())
                holdParent = self.currentBoard.getPosition(self.currentBoard.getGoal()).getParents()
                while (holdParent != None):
                    finalPath.append(holdParent)
                    holdParent =  self.currentBoard.getPosition(holdParent).getParents()

                finalPath.append(self.currentBoard.getStart())
                return finalPath

            # adding new neighbour nodes to que
            else:
                hold = self.currentBoard.getNodesNeighbours(currentCanidate)
                for i in range(len(hold)):

                    if( openlist.checkIfInQueue(hold[i]) == False and closedList.checkIfInQueue(hold[i]) == False):
                        self.currentBoard.getPosition(hold[i]).setCarryOverWeight(
                            self.currentBoard.getPosition(currentCanidate).getWeightAndCarryOver())

                        self.currentBoard.getPosition(hold[i]).setParent(currentCanidate)

                        weightToBeUsed = self.currentBoard.getPosition(hold[i]).getDisPlusWeight()
                        openlist.push(hold[i], weightToBeUsed)
