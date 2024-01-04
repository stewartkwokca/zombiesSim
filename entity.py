import screen
import random
import pygame

DEFAULT_ENTITY_SIZE = (10, 10)
ICON_DIMS = (150, 150)

RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Entity():
    def __init__(self, x, y, infected=False):
        self.x = x
        self.y = y

        self.WIDTH = 20
        self.HEIGHT = 20
        self.SPEED = 10

        self.infected=infected

    def tick(self):
        self.move()
        self.stayInBounds()

    def move(self):
        self.x += random.randint(-1*self.SPEED, self.SPEED)
        self.y += random.randint(-1*self.SPEED, self.SPEED)

    def stayInBounds(self):
        self.x = max(min(self.x, screen.WIDTH-20), 20)
        self.y = max(min(self.y, screen.HEIGHT-20), 20)

    def render(self, window):
        if self.infected:
            pygame.draw.rect(window, RED, ((self.x - self.WIDTH / 2, self.y - self.HEIGHT / 2), (self.WIDTH, self.HEIGHT)))
        else:
            pygame.draw.rect(window, GREEN, ((self.x - self.WIDTH / 2, self.y - self.HEIGHT / 2), (self.WIDTH, self.HEIGHT)))

    def collision(self, other):
        return abs(self.x - other.x) <= self.WIDTH and abs(self.y - other.y) <= self.HEIGHT


