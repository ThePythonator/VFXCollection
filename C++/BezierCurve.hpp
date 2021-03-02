#pragma once

#include <vector>
#include "Point.hpp"

namespace VFXCollection {

    template <typename T>
    Point2D<T> bezier_curve(std::vector<Point2D<T>>, double);

    template <typename T>
    class BezierCurve {
    public:
        BezierCurve();
        BezierCurve(std::vector<Point2D<T>>, double=1);

        void reset() { t = 0; }

        bool is_started() { return t > 0; }
        bool is_finished() { return t == max_t; }
        bool is_running() { return is_started() && !is_finished(); }
        
        void start(double);

        void update(double);
        Point2D<T> calculate();

    protected:
        std::vector<Point2D<T>> nodes;
        double t, max_t;
    };

}