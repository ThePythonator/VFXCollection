#pragma once

#include <cmath>

template <typename T>
class dPoint {
public:
    T x, y;

    dPoint();
    dPoint(T, T);

    T magnitude();

    dPoint<T> operator+(const dPoint<T>& other) { return dPoint<T>(x + other.x, y + other.y); }
    dPoint<T> operator-(const dPoint<T>& other) { return dPoint<T>(x - other.x, y - other.y); }
    dPoint<T> operator*(const dPoint<T>& other) { return dPoint<T>(x * other.x, y * other.y); }
    dPoint<T> operator/(const dPoint<T>& other) { return dPoint<T>(x / other.x, y / other.y); }
    
    dPoint<T> operator+(T other) { return dPoint<T>(x + other, y + other); }
    dPoint<T> operator-(T other) { return dPoint<T>(x - other, y - other); }
    dPoint<T> operator*(T other) { return dPoint<T>(x * other, y * other); }
    dPoint<T> operator/(T other) { return dPoint<T>(x / other, y / other); }
    
    dPoint<T> operator%(int other) { return dPoint<T>(x % other, y % other); }
    
    bool operator==(const dPoint<T>& other) { return x == other.x && y == other.y; }
    bool operator!=(const dPoint<T>& other) { return !(x == other.x && y == other.y); }
};