#include "BezierCurve.hpp"

namespace VFXCollection {

    Point2D<double> bezier_curve(std::vector<Point2D<double>> nodes, double ratio) {
        if (nodes.size() == 0) {
            return Point2D<double>(0, 0);
        }
        else if (nodes.size() == 1) {
            return nodes[0];
        }

        std::vector<Point2D<double>> new_nodes;

        for (uint8_t i = 0; i < nodes.size() - 1; i++) {
            new_nodes.push_back(nodes[i] + (nodes[i + 1] - nodes[i]) * ratio);
        }

        return bezier_curve(new_nodes, ratio);
    }

    BezierCurve::BezierCurve() {
        t = 0;
        max_t = 1;
    }

    BezierCurve::BezierCurve(std::vector<Point2D<double>> nodes, double max_t) {
        this->nodes = nodes;
        t = 0;
        this->max_t = max_t;
    }

    void BezierCurve::start(double dt) {
        reset();
        t += dt;
    }

    void BezierCurve::update(double dt) {
        if (is_running()) {
            t += dt;

            if (t > max_t) {
                t = max_t;
            }
        }
    }

    Point2D<double> BezierCurve::calculate() {
        return bezier_curve(nodes, t / max_t);
    }

}