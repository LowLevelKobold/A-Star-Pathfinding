from XY import XYobject
from GenerateBoard import GenerateBoard
from AStarPathFinding import AstarPathFinding
from VisualMain import VisualElement
holdBoard = None


def setup():
    boardSize = XYobject(20, 12)
    hold = VisualElement(boardSize, 20 , 12)


if __name__ == '__main__':
    setup()
