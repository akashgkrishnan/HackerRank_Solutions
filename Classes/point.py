from math import sqrt
class Point:
    def __init__(self, x, y):
        self.xCord = x
        self.yCord = y

    def getX(self):
        return self.xCord
    def getY(self):
        return self.yCord

    def shif(self, x_inc, y_inc):
        self.xCord += x_inc
        self.yCord += y_inc

    def __eq__(self, rhsPoint):
        return self.xCord == rhsPoint.xCord and self.yCord == rhsPoint.yCord

    def distance(self, Point2):
        xDiff = self.getX() - Point2.getX()
        yDiff = self.getY() - Point2.getY()
        return sqrt(xDiff ** 2 + yDiff ** 2)
