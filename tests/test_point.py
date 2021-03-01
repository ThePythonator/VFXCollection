from .. import Point

def test_point_default_values():
    point = Point.Point()
    assert point.x == 0 and point.y == 0