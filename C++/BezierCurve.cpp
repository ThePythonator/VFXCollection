#include "BezierCurve.hpp"

template <typename T>
Point<T> bezier_curve(std::vector<Point<T>> nodes, double ratio) {
    if (nodes.size() == 0) {
        return Point<T>(0, 0);
    }
    else if (nodes.size() == 1) {
        return nodes[0];
    }

    std::vector<Point<T>> new_nodes;

    for (uint8_t i = 0; i < nodes.size() - 1; i++) {
        new_nodes.push_back(nodes[i] + (nodes[i + 1] - nodes[i]) * ratio);
    }

    return bezier_curve(new_nodes, ratio);
}

template <typename T>
BezierCurve<T>::BezierCurve() {
    t = 0;
    max_t = 1;
}

template <typename T>
BezierCurve<T>::BezierCurve(std::vector<Point<T>> nodes, double max_t) {
    this->nodes = nodes;
    t = 0;
    this->max_t = max_t;
}

template <typename T>
void BezierCurve<T>::start(double dt) {
    reset()
    t += dt;
}

template <typename T>
void BezierCurve<T>::update(double dt) {
    if (is_running()) {
        t += dt;

        if (t > max_t) {
            t = max_t;
        }
    }
}

template <typename T>
Point<T> BezierCurve<T>::calculate() {
    return bezier_curve(nodes, t / max_t);
}