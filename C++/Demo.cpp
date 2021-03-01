#include "Demo.hpp"

int main() {
    Point<int> p = Point<int>(5, 6);
    p = p + Point<int>(1, 2);
    // p is now Point<int>(6, 8)
    
    return 0;
}