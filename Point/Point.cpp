#include "Point.hpp"

template <typename T>
Point<T>::Point() {
    x = y = 0;
}

template <typename T>
Point<T>::Point(T x, T y) {
    this->x = x;
    this->y = y;
}

template <typename T>
T Point<T>::magnitude() {
    return std::sqrt(x * x + y * y);
}