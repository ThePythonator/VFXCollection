from ..Point import Point

p = Point.Point(5, 6)
p = p + Point.Point(1, 2)
# p is now Point(6, 8)
assert p == Point.Point(6, 8)