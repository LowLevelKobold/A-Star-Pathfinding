# priority queue in order to make certin proccess easier
from XY import XYobject

class PriorityQueue:
    holdData= []# the data is
    holdValue= []# value is how the queue determins data positions

    def push(self, toAdd, valueToCheck):
        self.holdData.append(toAdd)
        self.holdValue.append(valueToCheck)

        if (len(self.holdData) != 0 and len(self.holdValue) != 0):
            holdNewValue, holdNewData = zip(*sorted(zip(self.holdValue, self.holdData)))
            self.holdData = list(holdNewData)
            self.holdValue = list(holdNewValue)

    def pull(self):
        holdVal = self.holdData[0]
        self.holdValue.pop(0)
        self.holdData.pop(0)
        return holdVal

    def checkIfInQueue(self, value):
        # this is a specilized check to deal with
        if isinstance(value, XYobject):
            for i in range(len(self.holdData)):
                if (self.holdData[i].getX() == value.getX() and self.holdData[i].getY() == value.getY()):
                    return True
            return False

        if (value in self.holdData):
            return True
        else:
            return False

# these are mainly used for testing purposes
    def peekPrint(self):
        for i in range(len(self.holdData)):
            print(self.holdData)

    def peekData(self):
        return self.holdData

    def checkSize(self):
        return len(self.holdData)

    def clear(self):
        self.holdData.clear()
        self.holdValue.clear()