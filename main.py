from p5 import *
from boid import *
import numpy
from vispy.util import event

flock = [Boid() for x in range(10)]

def setup():
    size(1080, 720)

def draw():
    #this happens every time
    background(30, 30, 47)

    if mouse_is_pressed:
        flock.append(Boid())

    for boid in flock:
        boid.edges()
        boid.flock(flock)
        boid.show()
        boid.update()

if __name__ == "__main__":
    run()