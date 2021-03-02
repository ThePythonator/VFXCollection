#include "Demo.hpp"

int main() {
    VFXCollection::Point<int> p = VFXCollection::Point<int>(5, 6);
    p = p + VFXCollection::Point<int>(1, 2);
    // p is now VFXCollection::Point<int>(6, 8)
    
    return 0;
}