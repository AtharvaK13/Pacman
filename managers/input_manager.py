import pygame


class InputManager:
    def get_direction(self):
        keys = pygame.key.get_pressed()
        direction = None

        if keys[pygame.K_UP]:
            direction = "up"
        elif keys[pygame.K_DOWN]:
            direction = "down"
        elif keys[pygame.K_LEFT]:
            direction = "left"
        elif keys[pygame.K_RIGHT]:
            direction = "right"
        return direction
