from p5 import *
#import numpy
import random

class Boid():
    def __init__(self):
        self.position = Vector(random.randrange(0, 1080), random.randrange(0, 720))
        self.velocity = Vector.random_2D()
        self.velocity.magnitude = random.uniform(2, 4)
        self.acceleration = Vector(0, 0)

        self.max_force = 5 # Force of which boids will flock together
        self.max_speed = 4 # Boid max speed
        
    # Align boids
    def align(self, boids):
        steer = Vector(0, 0)
        max_distance = 50
        total = 0

        # If a boid is near another, then steer towards it
        for bird in boids:
            dist = distance(self.position, bird.position)
            if (bird != self and dist < max_distance):
                steer += bird.velocity
                total += 1

        # Average out boid speed with group to follow
        if total > 0:
            steer /= total
            steer.magnitude = self.max_speed
            steer -= self.velocity
            steer.limit(self.max_force)
            
        return steer

    # Stick to flock
    def cohesion(self, boids):
        steer = Vector(0, 0)
        stick_force = 50
        count = 0
        for bird in boids:
            dist = distance(self.position, bird.position)
            if (bird != self and dist < stick_force):
                steer += bird.velocity
                count += 1

        if count > 0:
            steer /= count
            steer -= self.position
            steer -= self.velocity
            self.velocity.magnitude = self.max_speed
            steer.limit(self.max_force)

        return steer

    # Separate from other boids
    def separation(self, boids):
        steer = Vector(0, 0)
        sep_force = 10
        count = 0

        # Find the vector difference and evade
        for bird in boids:
            dist = distance(self.position, bird.position)
            if (bird != self and dist < sep_force):
                diff_vector = Vector.__sub__(self.position, bird.position)
                diff_vector /= dist 
                steer += diff_vector
                count += 1

        if count > 0:
            steer /= count
            self.velocity.magnitude = self.max_speed
            steer -= self.velocity
            steer.limit(self.max_force)

        return steer

    # group boids together
    def flock(self, boids):
        # Apply boid rules
        alignment = self.align(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)
        self.acceleration += separation
        self.acceleration += alignment
        self.acceleration += cohesion

        # Reset to not add up acceleration too much
        self.acceleration.__mul__(0)

    # Boids can never leave the canvas
    def edges(self):
        if self.position.x > 1080:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = 1080
        
        if self.position.y > 720:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = 720

    # Update location and limit speed of boids
    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration
        self.velocity.limit(self.max_speed)

    # Show boids using circles
    def show(self):
        fill(255)
        circle((self.position.x, self.position.y), 10)


