import Point

def get_distance(start, end):
    return [end[0] - start[0], end[1] - start[1]]


def bezier_curve(nodes, ratio):
    if len(nodes) == 0:
        return Point.Point(0, 0)
    elif len(nodes) == 1:
        return nodes[0]

    new_nodes = []

    for i in range(len(nodes) - 1):
        new_nodes.append(nodes[i] + ((nodes[i + 1] - nodes[i]) * ratio))
    
    return bezier_curve(new_nodes, ratio)

class BezierCurve:
    def __init__(self, nodes, max_t=1):
        self.nodes = nodes
        self.t = 0
        self.max_t = max_t

    def reset(self):
        self.t = 0
    
    def is_started(self):
        return self.t > 0

    def is_finished(self):
        return self.t == self.max_t

    def is_running(self):
        return self.is_started() and not self.is_finished()

    def start(self, dt):
        self.reset()
        self.t += dt

    def update(self, dt):
        if self.is_running():
            self.t += dt

            if self.t > self.max_t:
                self.t = self.max_t

    def calculate(self):
        return bezier_curve(self.nodes, self.t / self.max_t)