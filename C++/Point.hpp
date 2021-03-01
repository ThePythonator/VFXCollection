#pragma once

#include <cmath>

template <typename T>
class Point {
public:
    T x, y;

    Point();
    Point(T, T);

    T magnitude();

    Point<T> operator+(const Point<T>& other) { return Point<T>(x + other.x, y + other.y); }
    Point<T> operator-(const Point<T>& other) { return Point<T>(x - other.x, y - other.y); }
    Point<T> operator*(const Point<T>& other) { return Point<T>(x * other.x, y * other.y); }
    Point<T> operator/(const Point<T>& other) { return Point<T>(x / other.x, y / other.y); }
    
    Point<T> operator+(T other) { return Point<T>(x + other, y + other); }
    Point<T> operator-(T other) { return Point<T>(x - other, y - other); }
    Point<T> operator*(T other) { return Point<T>(x * other, y * other); }
    Point<T> operator/(T other) { return Point<T>(x / other, y / other); }
    
    Point<T> operator%(int other) { return Point<T>(x % other, y % other); }
    
    bool operator==(const Point<T>& other) { return x == other.x && y == other.y; }
    bool operator!=(const Point<T>& other) { return !(x == other.x && y == other.y); }
};