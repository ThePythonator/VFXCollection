def get_distance(start, end):
    return [end[0] - start[0], end[1] - start[1]]


def bezier_curve(nodes, ratio):
    if len(nodes) == 0:
        return 0
    elif len(nodes) == 1:
        return nodes[0]

    newNodes = []
    for i in range(len(nodes) - 1):
        node = list(nodes[i])
        dist = get_distance(nodes[i], nodes[i+1])

        node[0] += ratio * dist[0]
        node[1] += ratio * dist[1]

        newNodes.append(node)
    
    return bezier_curve(newNodes, ratio)

class BezierCurve:
    def __init__(self, nodes, maxT=1):
        self.nodes = nodes
        self.t = 0
        self.maxT = maxT

    def reset(self):
        self.t = 0
    
    def is_started(self):
        return self.t > 0

    def is_finished(self):
        return self.t == self.maxT

    def is_running(self):
        return self.is_started() and not self.is_finished()

    def update(self, dt):
        if self.is_running():
            self.t += dt

            if self.t > self.maxT:
                self.t = self.maxT

    def calculate(self):
        return bezier_curve(self.nodes, self.t / self.maxT)