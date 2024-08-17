import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity*dt)

    def split(self):
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        angle = random.random() * 30 + 20

        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

        asteroid1.velocity = self.velocity.rotate(angle) * 1.2
        asteroid2.velocity = self.velocity.rotate(-angle) * 1.2
