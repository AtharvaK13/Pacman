import pygame

from entities.ghost import Ghost
from entities import Pacman
from entities import RedGhost
from managers.input_manager import InputManager
from managers.collision_manager import CollisionManager
from managers.level_manager import LevelManager
from utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL_FILE


class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.pacman = Pacman(position=(100,100), speed=5, size=(20, 20))
        self.ghosts = [RedGhost(position=(200, 200), speed=3, size=(20,20))]
        self.input_manager = InputManager()
        self.collision_manager = CollisionManager()
        self.level_manager = LevelManager(LEVEL_FILE)
        self.running = True
        self.score = 0

    def run(self):
        while self.running:
            self.handle_events()
            self.update_entities()
            self.check_collisions()
            self.render()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update_entities(self):
        direction = self.input_manager.get_direction()
        if direction:
            self.pacman.move(direction, self.collision_manager, self.level_manager.walls)
        for ghost in self.ghosts:
            ghost.move(self.pacman.position, self.collision_manager, self.level_manager.walls)

    def check_collisions(self):


        for pellet in self.level_manager.pellets[:]:
            if self.collision_manager.check_collision(pellet, self.pacman):
                self.level_manager.pellets.remove(pellet)
            self.score += 10

        for ghost in self.ghosts:
            if self.collision_manager.check_collision(ghost, self.pacman):
                print("You Died")
                self.running = False

    def render(self):
        self.screen.fill((0, 0, 0))
        self.level_manager.draw(self.screen)
        self.pacman.draw(self.screen)

        for ghost in self.ghosts:
            ghost.draw(self.screen)
        pygame.display.flip()
