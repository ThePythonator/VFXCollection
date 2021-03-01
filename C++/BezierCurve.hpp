#pragma once

#include <vector>
#include "Point.hpp"

template <typename T>
Point<T> bezier_curve(std::vector<Point<T>>, double);

template <typename T>
class BezierCurve {
public:
    BezierCurve();
    BezierCurve(std::vector<Point<T>>, double=1);

    void reset() { t = 0; }

    bool is_started() { return t > 0; }
    bool is_finished() { return t == max_t; }
    bool is_running() { return is_started() && !is_finished(); }
    
    void start(double);

    void update(double);
    Point<T> calculate();

protected:
    std::vector<Point<T>> nodes;
    double t, max_t;
};