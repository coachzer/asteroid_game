

import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen, color="yellow"):
        pygame.draw.circle(
            screen,
            color,
            (int(self.position.x), int(self.position.y)),
            SHOT_RADIUS,
        )

    def update(self, dt):
        self.position += self.velocity * dt