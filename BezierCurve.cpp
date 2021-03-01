#include "BezierCurve.hpp"

template <typename T>
dPoint<T> bezier_curve(std::vector<dPoint<T>> nodes, double ratio) {
    if (nodes.size() == 0) {
        return dPoint(0, 0);
    }
    else if (nodes.size() == 1) {
        return nodes[0];
    }

    std::vector<dPoint<T>> newNodes;

    for (uint8_t i = 0; i < nodes.size() - 1; i++) {
        newNodes.push_back(nodes[i] + (nodes[i] - nodes[i + 1]) * ratio);
    }

    return bezier_curve(newNodes, ratio);
}

template <typename T>
BezierCurve<T>::BezierCurve() {
    t = 0;
    maxT = 1;
}

template <typename T>
BezierCurve<T>::BezierCurve(std::vector<dPoint<T>> nodes, double maxT) {
    this->nodes = nodes;
    t = 0;
    this->maxT = maxT;
}

template <typename T>
void BezierCurve<T>::update(double dt) {
    if (is_running()) {
        t += dt;

        if (t > maxT) {
            t = maxT;
        }
    }
}

template <typename T>
dPoint<T> BezierCurve<T>::calculate() {
    return bezier_curve(nodes, t / maxT);
}