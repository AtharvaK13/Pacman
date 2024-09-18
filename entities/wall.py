import pygame
from interfaces import Drawable

class Wall(Drawable):
    def __init__(self, position, size=(20,20)):
        self.position = position
        self.size = size
        self.original_sprite = pygame.image.load('assets/wall.jpg')
        self.sprite = pygame.transform.scale(self.original_sprite, size)


    def draw(self, screen):
        screen.blit(self.sprite, self.position)

    def get_rect(self):
        return self.sprite.get_rect(topleft=self.position)
