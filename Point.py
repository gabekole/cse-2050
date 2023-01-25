class Point:
    """
    Contains a point defined by (x, y)

    Comparisons are defined for "<", ">" and "==" operators
    Comparisons between points compare their distances from the origin

    Examples:
        Point(1, 1) < Point(1, 2) # True
        Point(-10, -5) > Point(3, 6) # True
        Point(1, 1) == Point(-1, -1) # True
        Point(2, 3) == Point(3, 2) # True

        Point(5, -7) < Point(2, 3) # False
        Point(-1, 3) > Point(5, 0) # False
        Point(2, 3) == Point(0, 0) # False

    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __gt__(self, other):
        return isinstance(other, Point) and self.dist_from_origin() > other.dist_from_origin()
    def __lt__(self,other):
        return isinstance(other, Point) and self.dist_from_origin() < other.dist_from_origin()
    def __eq__(self,other):
        return isinstance(other, Point) and self.dist_from_origin() == other.dist_from_origin()
    def dist_from_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def __str__(self):
        return 'Point('+ str(self.x) + ', ' + str(self.y) + ')'
    

# ^^^Implement class and functionality above (remember to include docstrings!)
# vvvImplement tests below

if __name__ == '__main__':
    # All tests should use `assert`, not `print`
    
    ##### test init #####
    p1 = Point(3, 4)
    p2 = Point(-6, 8)
    p3 = Point(-6, 8)
    p4 = Point(-3, -4)

    # assert correct x
    assert p1.x == 3
    assert p2.x == -6
    assert p3.x == -6
    assert p4.x == -3

    # assert correct y
    assert p1.y == 4
    assert p2.y == 8
    assert p3.y == 8
    assert p4.y == -4

    ##### test lt #####
    assert p1 < p2 # Expected True (e.g `p1 < p2`)
    assert not p2 < p1 # Expected False (e.g. `not p1 < p2`)
    assert not p2 < p3 # Expected False (same)
    assert not p1 < p4 # Expected false (same distance)

    ##### test gt #####
    assert p2 > p1 # Expected True (e.g `p1 > p2`)
    assert not p1 > p2 # Expected False (e.g. `not p1 > p2`)
    assert p2 > p1 # Expected true
    assert p3 > p4 # Expected true, greater distance
    assert not p3 > p2 # Expected false since same disatance

    ##### test eq #####
    assert p1 == p4 # Expected True (e.g `p1 == p2`)
    assert p2 == p3 # Expected True (same distance)
    assert p1 != p2 # Expected true (e.g. `not p1 == p2`)
    assert p2 != p4 # Expected true since different

    
    ##### test str #####
    assert str(p1) == "Point(3, 4)"
    assert str(p2) == "Point(-6, 8)"
    assert str(p3) == "Point(-6, 8)"
    assert str(p4) == "Point(-3, -4)"
    assert str(Point(9, 10)) == "Point(9, 10)"

    ##### test dist_from_origin() #####
    
    assert p1.dist_from_origin() == 5
    assert p2.dist_from_origin() == 10
    assert p3.dist_from_origin() == 10
    assert p4.dist_from_origin() == 5
