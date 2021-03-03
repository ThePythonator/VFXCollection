#include "Demo.hpp"

int main() {
    VFXCollection::Point2D<int> p = VFXCollection::Point2D<int>(5, 6);
    p = p + VFXCollection::Point2D<int>(1, 2);
    // p is now VFXCollection::Point2D<int>(6, 8)

    VFXCollection::BezierCurve b;
    return 0;
}