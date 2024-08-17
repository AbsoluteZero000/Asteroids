import pygame
from shot import Shot
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_DELAY


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.delay = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.delay -= dt

        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt

        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt

        if keys[pygame.K_w]:
            self.position += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt

        if keys[pygame.K_s]:
            self.position -= pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt

        if keys[pygame.K_SPACE]:
            self.shoot()
    def shoot(self):
        if(self.delay <= 0):
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.delay = PLAYER_SHOOT_DELAY
