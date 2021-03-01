# Import dependencies
import pygame, sys

# Import VFXCollection files
import Point
import BezierCurve

# A simple function to render a point/circle in pygame
def render_point(screen, point, colour, radius):
    pygame.draw.circle(screen, colour, [point.x, point.y], radius)

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
   Point.Point(40, 40),
   Point.Point(60, 160),
   Point.Point(180, 80),
   Point.Point(200, 200)
]
# Total time curve takes to complete, in seconds
max_t = 2

# Create a window and set the caption
screen = pygame.display.set_mode((240,240))
pygame.display.set_caption("VFXCollection Demo")

# Create a clock to limit framerate and calculate delta-time
clock = pygame.time.Clock()

# Create an instance of the VFXCollection BezierCurve class
bezier_curve = BezierCurve.BezierCurve(nodes, max_t)

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

    # Update the bezier_curve instance
    bezier_curve.update(dt)

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

    # Update the display
    pygame.display.flip()
