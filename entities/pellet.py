import pygame

from interfaces import Drawable

class Pellet(Drawable):
    def __init__(self, position):
        self.position = pygame.Vector2(position)
        self.sprite = pygame.image.load('assets/pellet.png')

    def draw(self, screen):
        screen.blit(self.sprite, self.position)

    def get_rect(self):
        return self.sprite.get_rect(topleft=self.position)
