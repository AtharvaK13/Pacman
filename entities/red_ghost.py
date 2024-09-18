import pygame
from entities import Ghost


class RedGhost(Ghost):
    def move(self, target_position, collision_manager, walls):
        # Implement chasing behavior towards Pac-Man
        direction_vector = target_position - self.position
        if direction_vector.length() != 0:
            direction_vector = direction_vector.normalize()
        delta = direction_vector * self.speed

        if self.can_move(delta, collision_manager, walls):
            self.position += delta
        else:
            # Try alternative movement (e.g., random movement)
            self.try_alternative_move(collision_manager, walls)

    def try_alternative_move(self, collision_manager, walls):
        pass
