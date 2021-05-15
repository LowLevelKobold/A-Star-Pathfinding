import unittest
from XY import XYobject
from GenerateBoard import GenerateBoard
from AStartNodes import nodeAstar
from PriorityQueue import PriorityQueue


class MyTestCase(unittest.TestCase):

    def testGettersXY(self):
        # testing the X Y object classes getters
        hold = XYobject(5, 20)
        self.assertEqual(hold.getY(), 20)
        self.assertEqual(hold.getX(), 5)

    def testSetters(self):
        #testing the X Y object classes setters
        hold = XYobject(0, 0)
        hold.setY(10)
        self.assertEqual(hold.getY(), 10)
        self.assertEqual(hold.getX(), 0)

        hold.setX(11)
        self.assertEqual(hold.getY(), 10)
        self.assertEqual(hold.getX(), 11)

        hold.setBoth(20, 20)
        self.assertEqual(hold.getY(), 20)
        self.assertEqual(hold.getX(), 20)

    def testBoardGeneration(self):
        # testing of the GenerateBoard class
        '''
        note this test has passed but due to a visual changes for latter on
        testing it will fail at the moment. This may be edited in final
        however for the moment it is not. Note the edit can be
        done by replacing  str(self.weightOfPosition) with '#' in AstartNodes
        in getstate
        '''
        toCompare = [["P", "#", "#"], ["#", "#", "#"], ["#", "#", "T"]]
        size = XYobject(3, 3)
        start = XYobject(0, 0)
        target = XYobject(2, 2)
        hold = GenerateBoard(size, start, target)
        self.assertEqual(hold.getBoard(), toCompare)
        hold.clearBoard()

    def testSyntaxErros(self):
        #test to determine if the syntax errors are triggering correctly in the generate board class
        size = XYobject(0, 0)
        start = XYobject(1, 1)
        target = XYobject(3, 3)
        self.assertRaises(SyntaxError, GenerateBoard, size, start, target)

        size = XYobject(5, 5)
        start = XYobject(1, -2)
        target = XYobject(3, 3)
        self.assertRaises(SyntaxError, GenerateBoard, size, start, target)

        size = XYobject(5, 5)
        start = XYobject(1, 2)
        target = XYobject(3, -3)
        self.assertRaises(SyntaxError, GenerateBoard, size, start, target)

        size = XYobject(5, 5)
        start = XYobject(1, 55)
        target = XYobject(3, 3)
        self.assertRaises(SyntaxError, GenerateBoard, size, start, target)

        size = XYobject(5, 5)
        start = XYobject(1, 2)
        target = XYobject(3, 55)
        self.assertRaises(SyntaxError, GenerateBoard, size, start, target)

        size = XYobject(5, 5)
        start = XYobject(55, 1)
        target = XYobject(3, 3)
        self.assertRaises(SyntaxError, GenerateBoard, size, start, target)

        size = XYobject(5, 5)
        start = XYobject(1, 2)
        target = XYobject(55, 3)
        self.assertRaises(SyntaxError, GenerateBoard, size, start, target)


    def testTypeErrors(self):
        # test to determine if the type errors are triggering correctly in the generate board class
        size = XYobject(5, 5)
        start = XYobject(1, 2)
        target = XYobject(3, 3)
        self.assertRaises(TypeError, GenerateBoard, 5, start, target)
        self.assertRaises(TypeError, GenerateBoard, size, 5, target)
        self.assertRaises(TypeError, GenerateBoard, size, start, 5)

    def testEuclidanDistance(self):
        #testing euclidian math that is used by the A star nodes
        start = XYobject(5, 10)
        end = XYobject(2, 5)
        hold = nodeAstar(start, end, False, False)
        self.assertAlmostEqual(5.830951894845301, hold.getDistanceToTarget())

    def testNeighbours(self):
        #testing if nodes can find there neighbours
        size = XYobject(3, 3)
        start = XYobject(0, 0)
        target = XYobject(2, 2)
        hold = GenerateBoard(size, start, target)

        # y movements
        t1 = XYobject(1,0)
        t2 = XYobject(1,2)

        # X movements
        t3 = XYobject(2,1)
        t4 = XYobject(0,1)

        listOfNodes = hold.getNodesNeighbours(XYobject(1,1))

        h1 = listOfNodes[0]
        h2 = listOfNodes[1]
        h3 = listOfNodes[2]
        h4 = listOfNodes[3]

        self.assertEqual(h1.checkForEqual(t1), True)
        self.assertEqual(h2.checkForEqual(t2), True)
        self.assertEqual(h3.checkForEqual(t3), True)
        self.assertEqual(h4.checkForEqual(t4), True)


    def testOffsetNeighboursOne(self):
        size = XYobject(3, 3)
        start = XYobject(0, 0)
        target = XYobject(2, 2)
        hold = GenerateBoard(size, start, target)

        t1 = XYobject(0,0)
        t2 = XYobject(0,2)
        t3 = XYobject(1,1)

        listOfNodes = hold.getNodesNeighbours(XYobject(0,1))

        h1 = listOfNodes[0]
        h2 = listOfNodes[1]
        h3 = listOfNodes[2]

        self.assertEqual(h1.checkForEqual(t1), True)
        self.assertEqual(h2.checkForEqual(t2), True)
        self.assertEqual(h3.checkForEqual(t3), True)

    def testOffsetNeighboursTwo(self):
        size = XYobject(3, 3)
        start = XYobject(0, 0)
        target = XYobject(2, 2)
        hold = GenerateBoard(size, start, target)

        # y movements
        t2 = XYobject(1, 1)

        # X movements
        t3 = XYobject(2, 0)
        t4 = XYobject(0, 0)

        listOfNodes = hold.getNodesNeighbours(XYobject(1,0))

        h2 = listOfNodes[0]
        h3 = listOfNodes[1]
        h4 = listOfNodes[2]

        self.assertEqual(h2.checkForEqual(t2), True)
        self.assertEqual(h3.checkForEqual(t3), True)
        self.assertEqual(h4.checkForEqual(t4), True)

# testing priority Queue
    def testOfPriorityQueue(self):
        data = 1
        data1 = 3
        data2 = 2

        holdQueue = PriorityQueue()
        holdQueue.push(data, 1)
        holdQueue.push(data1, 3)
        holdQueue.push(data2, 2)

        self.assertEqual(holdQueue.checkSize(), 3)
        self.assertEqual(holdQueue.peekData(), [1,2,3])

        holdPull = holdQueue.pull()
        self.assertEqual(holdPull, 1)

        self.assertEqual(holdQueue.checkSize(), 2)
        self.assertEqual(holdQueue.peekData(), [2, 3])

    def testTwoOfPriorityQueue(self):
        data = 1
        data1 = 3
        data2 = 2

        holdQueue = PriorityQueue()
        holdQueue.push(data, 1)
        holdQueue.push(data1, 3)
        holdQueue.push(data2, 2)

        self.assertEqual(True, holdQueue.checkIfInQueue(3))
        self.assertEqual(False, holdQueue.checkIfInQueue(99))
        self.assertEqual(False, holdQueue.checkIfInQueue(22))

if __name__ == '__main__':
    unittest.main()
