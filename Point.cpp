#include "Point.hpp"

template <typename T>
dPoint<T>::dPoint() {
    x = y = 0;
}

template <typename T>
dPoint<T>::dPoint(T x, T y) {
    this->x = x;
    this->y = y;
}

template <typename T>
T dPoint<T>::magnitude() {
    return std::sqrt(x * x + y * y);
}