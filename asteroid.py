import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen, color="gray"):
        pygame.draw.circle(
            screen,
            color,
            (int(self.position.x), int(self.position.y)),
            self.radius,
            LINE_WIDTH,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        for i in range(2):
            new_asteroid = Asteroid(
                self.position.x,
                self.position.y,
                new_radius,
            )
            velocity = self.velocity.rotate(angle if i == 0 else -angle)
            new_asteroid.velocity = velocity * 1.2
        

