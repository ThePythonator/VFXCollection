import pygame, sys

import Point
import BezierCurve

def render_point(screen, point, colour, radius):
    pygame.draw.circle(screen, colour, [point.x, point.y], radius)

colours = [
    (255, 255, 255),
    (255, 0, 0),
    (255, 255, 0),
    (0, 0, 0)
]

# BezierCurve data
nodes = [ # Control nodes
   Point.Point(40, 40),
   Point.Point(60, 160),
   Point.Point(180, 80),
   Point.Point(200, 200)
]
max_t = 2 # seconds

screen = pygame.display.set_mode((240,240))
pygame.display.set_caption("VFXCollection Demo")

clock = pygame.time.Clock()

bezier_curve = BezierCurve.BezierCurve(nodes, max_t)

points = [] # used for tracking path

while True:
    # Update section
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bezier_curve.start(dt)
                points = []

    bezier_curve.update(dt)

    # Render section
    screen.fill(colours[3])


    if bezier_curve.is_running():
        points.append(bezier_curve.calculate())

    for point in points:
        render_point(screen, point, colours[0], 1)
        
    for point in bezier_curve.nodes:
        render_point(screen, point, colours[2], 1)
        
    render_point(screen, bezier_curve.calculate(), colours[1], 5)

    pygame.display.flip()
