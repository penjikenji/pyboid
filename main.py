from p5 import *
from boid import *
#import numpy

flock = [Boid() for x in range(50)] # setup boids 

# setup p5 canvas
def setup():
    size(1080, 720)

# draw onto canvas
def draw():
    background(30, 30, 47)

    # If the mouse is pressed, then add a boid
    if mouse_is_pressed:
        flock.append(Boid())
    
    # If key is pressed, then remove a boid
    if key_is_pressed:
        flock.pop(len(flock) - 1)

    # For each boid that's drawn, make it flock and update onto canvas
    for boid in flock:
        boid.edges()
        boid.flock(flock)
        boid.show()
        boid.update()

# Running p5
if __name__ == "__main__":
    run()