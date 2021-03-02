import Particle, Point

class ParticleGenerator:
    def __init__(self, particle_gravity=Point.Point(0,0), particle_lifetime=1, generation_delay=1, _particle_generate=None, _particle_render=None, _custom_update=None):
        self.particles = []

        self.particle_gravity = particle_gravity
        self.particle_lifetime = particle_lifetime

        self.generation_timer = 0
        self.generation_delay = generation_delay

        self._particle_generate = _particle_generate
        self._particle_render = _particle_render

        # Note: if using a _custom_update function, you need to call particle_generator.custom_update(*args) every frame INSTEAD of particle_generator.update(*args)
        self._custom_update = _custom_update

        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.generation_timer = 0

    def is_running(self):
        return self.running

    def update(self, dt, *generate_args):
        if self.is_running():
            self.generation_timer += dt

            if self.generation_timer >= self.generation_delay:
                self.generation_timer -= self.generation_delay
                self.generate(*generate_args)

        to_remove = []
        for particle in self.particles:
            particle.update(dt)

            if particle.is_finished():
                to_remove.append(particle)

        for particle in to_remove:
            self.particles.remove(particle)
        
    def set_render(self, _particle_render):
        self._particle_render = _particle_render

    def render(self, *render_args):
        if self._particle_render is not None:
            for particle in self.particles:
                self._particle_render(particle, *render_args)

    def set_generate(self, _particle_generate):
        self._particle_generate = _particle_generate

    def generate(self, *generate_args):
        if self._particle_generate is not None:
            self.particles.append(self._particle_generate(self, *generate_args))
            
    def set_custom_update(self, _custom_update):
        self._custom_update = _custom_update

    def custom_update(self, *custom_update_args):
        if self._custom_update is not None:
            self._custom_update(*custom_update_args)