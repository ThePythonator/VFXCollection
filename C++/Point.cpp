#include "Point.hpp"

namespace VFXCollection {

    template <typename T>
    Point2D<T>::Point2D() {
        x = y = 0;
    }

    template <typename T>
    Point2D<T>::Point2D(T x, T y) {
        this->x = x;
        this->y = y;
    }

    template <typename T>
    T Point2D<T>::magnitude() {
        return std::sqrt(x * x + y * y);
    }

}