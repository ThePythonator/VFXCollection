import Point

class Particle:
    def __init__(self, position=Point.Point2D(0,0), velocity=Point.Point2D(0,0), gravity=Point.Point2D(0,0), colour=(255,255,255), size=1, lifetime=1):
        self.position = position
        self.velocity = velocity
        self.gravity = gravity

        self.colour = colour
        self.size = size
        self.lifetime = lifetime

        self._custom_update = None

    def is_finished(self):
        return self.lifetime == 0

    def is_running(self):
        return not self.is_finished()

    def update(self, dt):
        if self.is_running():
            self.lifetime -= dt

            if self.lifetime < 0:
                self.lifetime = 0

            self.velocity += self.gravity * dt
            self.position += self.velocity * dt