from point import Point
class Line:
    def __init__(self, pointA, pointB):
        self._pointA = pointA
        self._pointB = pointB

    def getPointA(self):
        return self._pointA

    def getPointB(self):
        return self._pointB

    def length(self):
        return self._pointA.distance(self._pointB)

    def isVertical(self):
        return self._pointA.getX() == self._pointB.getX()

    def slope(self):
        if self.isVertical():
            return None
        else:
            run = self._pointA.getX() - self._pointB.getX()
            rise = self._pointA.getY() - self._pointB.getY()
            return rise//run
B = Point(10, 20)
A = Point(10, 20)
AB = Line(A, B)
print(AB.slope())
print(AB.length())
print(A == B)
C = Point(0,0)
print(C == Point(0, 0))
