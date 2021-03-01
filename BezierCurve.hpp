#pragma once

#include <vector>
#include "Point.hpp"

template <typename T>
dPoint<T> bezier_curve(std::vector<dPoint<T>>, double);

template <typename T>
class BezierCurve {
public:
    BezierCurve();
    BezierCurve(std::vector<dPoint<T>>, double=1);

    void reset() { t = 0; }

    bool is_started() { return t > 0; }
    bool is_finished() { return t == max_t; }
    bool is_running() { return is_started() && !is_finished(); }

    void update(double);
    dPoint<T> calculate();

protected:
    std::vector<dPoint<T>> nodes;
    double t, max_t;
};