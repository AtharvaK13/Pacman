import pygame

from interfaces import Movable
from interfaces import Drawable


class Pacman(Movable, Drawable):
    def __init__(self, position, speed, size=(20, 20)):
        self.position = pygame.Vector2(position)
        self.speed = speed
        self.size = size

        self.original_sprite = pygame.image.load('assets/pacman.png')
        self.sprite = pygame.transform.scale(self.original_sprite, self.size)

    def move(self, direction, collision_manager, walls):
        # Store desired direction
        self.direction = direction
        # Calculate new position
        delta = pygame.Vector2(0, 0)
        if direction == 'up':
            delta.y = -self.speed
        elif direction == 'down':
            delta.y = self.speed
        elif direction == 'left':
            delta.x = -self.speed
        elif direction == 'right':
            delta.x = self.speed

        # Check for collision
        if self.can_move(delta, collision_manager, walls):
            self.position += delta

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