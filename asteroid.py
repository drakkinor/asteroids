import pygame # type: ignore
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            roid1_vector = self.velocity.rotate(angle)
            roid2_vector = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            roid1 = Asteroid(self.position.x, self.position.y, new_radius)
            roid1.velocity = roid1_vector * 1.2

            roid2 = Asteroid(self.position.x, self.position.y, new_radius)
            roid2.velocity = roid2_vector * 1.2


