#pragma once

#include <cmath>

namespace VFXCollection {

    template <typename T>
    class Point2D {
    public:
        T x, y;

        Point2D();
        Point2D(T, T);

        T magnitude();

        Point2D<T> operator+(const Point2D<T>& other) { return Point2D<T>(x + other.x, y + other.y); }
        Point2D<T> operator-(const Point2D<T>& other) { return Point2D<T>(x - other.x, y - other.y); }
        Point2D<T> operator*(const Point2D<T>& other) { return Point2D<T>(x * other.x, y * other.y); }
        Point2D<T> operator/(const Point2D<T>& other) { return Point2D<T>(x / other.x, y / other.y); }
        
        Point2D<T> operator+(T other) { return Point2D<T>(x + other, y + other); }
        Point2D<T> operator-(T other) { return Point2D<T>(x - other, y - other); }
        Point2D<T> operator*(T other) { return Point2D<T>(x * other, y * other); }
        Point2D<T> operator/(T other) { return Point2D<T>(x / other, y / other); }
        
        Point2D<T> operator%(int other) { return Point2D<T>(x % other, y % other); }
        
        bool operator==(const Point2D<T>& other) { return x == other.x && y == other.y; }
        bool operator!=(const Point2D<T>& other) { return !(x == other.x && y == other.y); }
    };

}