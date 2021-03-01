from .. import Point

def test_point_default_values():
    point = Point.Point()
    assert point.x == 0 and point.y == 0
    
def test_point_custom_values_normal():
    point = Point.Point(8, 27)
    assert point.x == 8 and point.y == 27
    
def test_point_custom_values_negative():
    point = Point.Point(8, -27)
    assert point.x == 8 and point.y == -27
    
def test_point_custom_values_float():
    point = Point.Point(8.57, 27.25)
    assert point.x == 8.57 and point.y == 27.25
    
def test_point_point_addition():
    point = Point.Point(8, 27) + Point.Point(9, 4)
    assert point.x == 17 and point.y == 31
    
def test_point_point_subtraction():
    point = Point.Point(8, 27) - Point.Point(9, 4)
    assert point.x == -1 and point.y == 23
    
def test_point_point_multiplication():
    point = Point.Point(8, 27) * Point.Point(9, 4)
    assert point.x == 72 and point.y == 108
    
def test_point_point_truedivision():
    point = Point.Point(8, 27) / Point.Point(4, 9)
    assert point.x == 2 and point.y == 3
    
def test_point_point_floordivision():
    point = Point.Point(8, 27) // Point.Point(3, 4)
    assert point.x == 2 and point.y == 6
    
def test_point_point_modulus():
    point = Point.Point(8, 27) % Point.Point(3, 4)
    assert point.x == 2 and point.y == 3
    
def test_point_scalar_addition():
    point = Point.Point(8, 27) + 5
    assert point.x == 13 and point.y == 32
    
def test_point_scalar_subtraction():
    point = Point.Point(8, 27) - 5
    assert point.x == 3 and point.y == 22
    
def test_point_scalar_multiplication():
    point = Point.Point(8, 27) * 5
    assert point.x == 40 and point.y == 135
    
def test_point_scalar_truedivision():
    point = Point.Point(8, 27) / 5
    assert point.x == 1.6 and point.y == 5.4
    
def test_point_scalar_floordivision():
    point = Point.Point(8, 27) // 5
    assert point.x == 1 and point.y == 5
    
def test_point_scalar_modulus():
    point = Point.Point(8, 27) % 5
    assert point.x == 3 and point.y == 2
    
def test_point_list_addition():
    point = Point.Point(8, 27) + [1, 5]
    assert point.x == 9 and point.y == 32
    
def test_point_list_subtraction():
    point = Point.Point(8, 27) - [1, 5]
    assert point.x == 7 and point.y == 22
    
def test_point_list_multiplication():
    point = Point.Point(8, 27) * [1, 5]
    assert point.x == 8 and point.y == 135
    
def test_point_list_truedivision():
    point = Point.Point(8, 27) / [1, 5]
    assert point.x == 8 and point.y == 5.4
    
def test_point_list_floordivision():
    point = Point.Point(8, 27) // [1, 5]
    assert point.x == 8 and point.y == 5
    
def test_point_list_modulus():
    point = Point.Point(8, 27) % [1, 5]
    assert point.x == 0 and point.y == 2
    
def test_point_tuple_addition():
    point = Point.Point(8, 27) + (1, 5)
    assert point.x == 9 and point.y == 32
    
def test_point_tuple_subtraction():
    point = Point.Point(8, 27) - (1, 5)
    assert point.x == 7 and point.y == 22
    
def test_point_tuple_multiplication():
    point = Point.Point(8, 27) * (1, 5)
    assert point.x == 8 and point.y == 135
    
def test_point_tuple_truedivision():
    point = Point.Point(8, 27) / (1, 5)
    assert point.x == 8 and point.y == 5.4
    
def test_point_tuple_floordivision():
    point = Point.Point(8, 27) // (1, 5)
    assert point.x == 8 and point.y == 5
    
def test_point_tuple_modulus():
    point = Point.Point(8, 27) % (1, 5)
    assert point.x == 0 and point.y == 2