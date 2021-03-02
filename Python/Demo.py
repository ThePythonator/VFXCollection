# Import dependencies
import pygame, sys, math, random

# Import VFXCollection files
import Point
import Particle
import BezierCurve
import ParticleGenerator

# A simple function to render a point/circle in pygame
def render_point(screen, point, colour, radius):
    pygame.draw.circle(screen, colour, [point.x, point.y], radius)

# A simple function to be passed to the particle system
def render_particle(particle, screen):
    render_point(screen, particle.position, particle.colour, particle.size)

# A simple function to create a Particle, to be passed to the particle system
def generate_particle(generator, position, speed, colours, size):
    # Get a random angle
    angle = random.randint(0, 360)
    # Calculate the particle velocity using that angle
    velocity = Point.Point2D(speed * math.cos(angle), speed * math.sin(angle))
    # Create a particle
    return Particle.Particle(position, velocity=velocity, gravity=generator.particle_gravity, lifetime=generator.particle_lifetime, colour=random.choice(colours), size=size)

# Some simple RGB values to use as colours
colours = [
    (255, 255, 255),    # White
    (255, 0, 0),        # Red
    (255, 255, 0),      # Yellow
    (0, 0, 0)           # Black
]

# BezierCurve setup data
# Control nodes - try changing them and see what happens!
nodes = [
   Point.Point2D(40, 40),
   Point.Point2D(60, 160),
   Point.Point2D(180, 80),
   Point.Point2D(200, 200)
]
# Total time curve takes to complete, in seconds
max_t = 2

# Define a Point2D() to spawn particles at
particle_spawn = Point.Point2D(360, 120)

# Create a window and set the caption
screen = pygame.display.set_mode((480,240))
pygame.display.set_caption("VFXCollection Demo")

# Create a clock to limit framerate and calculate delta-time
clock = pygame.time.Clock()

# Create an instance of the VFXCollection BezierCurve class
bezier_curve = BezierCurve.BezierCurve(nodes, max_t)

# Create an instance of the VFXCollection ParticleGenerator class
particle_generator = ParticleGenerator.ParticleGenerator(particle_gravity=Point.Point2D(0,50), particle_lifetime=5, generation_delay=0.02, _particle_generate=generate_particle, _particle_render=render_particle)

# On startup, start everything so that people don't need to know what buttons to press in order to start anything
# Start the curve
bezier_curve.start(0.001) # since dt isn't defined yet, just pass a tiny value in instead
# Start the particle generator
particle_generator.start()

# Create an empty list of points to use to track the path of the curve over time.
points = []

# Main application loop
while True:

##### Update section #####
    
    # Get delta-time, limit the framerate to 60 FPS
    dt = clock.tick(60) / 1000

    # Handle events/keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # User has pressed X
            # Close the window
            pygame.quit()
            # Exit the program
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # User has pressed space
                # Start the curve
                bezier_curve.start(dt)
                # Clear the list of points
                points = []
            
            elif event.key == pygame.K_RETURN:
                # User has pressed return/enter
                if particle_generator.is_running():
                    # Stop and reset the particle generator
                    particle_generator.stop()
                    particle_generator.reset()

                else:
                    # Start the particle generator
                    particle_generator.start()

    # Update the bezier_curve instance
    bezier_curve.update(dt)

    # Update the particle_generator instance
    particle_generator.update(dt, particle_spawn, 50, [colours[0], colours[1], colours[2]], 3)

##### Render section #####

    # Fill the screen with a solid colour
    screen.fill(colours[3])

    # Add the main point to the path tracing points
    points.append(bezier_curve.calculate())

    # Display the path tracing points
    for point in points:
        render_point(screen, point, colours[0], 1)
        
    # Display the control points
    for point in bezier_curve.nodes:
        render_point(screen, point, colours[2], 2)
        
    # Display the main point
    render_point(screen, bezier_curve.calculate(), colours[1], 5)

    # Render the particles
    particle_generator.render(screen)

    # Update the display
    pygame.display.flip()
