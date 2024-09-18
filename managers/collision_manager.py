class CollisionManager:
    def check_collision(self, entity1, entity2):
        rect1 = entity1.get_rect()
        rect2 = entity2.get_rect()
        return rect1.colliderect(rect2)

    def prevent_movement_through_walls(self, entity, walls):
        future_rect = entity.get_future_rect()
        for wall in walls:
            if future_rect.colliderect(wall.get_rect()):
                return False

        return True
