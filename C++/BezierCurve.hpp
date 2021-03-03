#pragma once

#include <vector>
#include "Point.hpp"

namespace VFXCollection {

    Point2D<double> bezier_curve(std::vector<Point2D<double>>, double);

    class BezierCurve {
    public:
        BezierCurve();
        BezierCurve(std::vector<Point2D<double>>, double=1);

        void reset();

        bool is_started();
        bool is_finished();
        bool is_running();
        
        void start(double);

        void update(double);
        Point2D<double> calculate();

    protected:
        std::vector<Point2D<double>> nodes;
        double t, max_t;
    };

}