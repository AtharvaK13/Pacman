import pygame
from interfaces import Movable
from interfaces import Drawable

class Ghost(Movable, Drawable):
    def __init__(self, position, speed, size=(20, 20)):
        self.position = pygame.Vector2(position)
        self.speed = speed
        self.size = size
        self.original_sprite = pygame.image.load('assets/redghost.png')
        self.sprite = pygame.transform.scale(self.original_sprite, self.size)

    def move(self, target_position):
        pass

    def can_move(self, delta, collision_manager, walls):
        future_rect = self.get_rect().move(delta.x, delta.y)
        for wall in walls:
            if future_rect.colliderect(wall.get_rect()):
                return False
        return True


    def draw(self, screen):
        screen.blit(self.sprite, self.position)

    def get_rect(self):
        return self.sprite.get_rect(topleft=self.position)

    