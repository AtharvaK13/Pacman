import pygame

from entities import Wall
from entities import Pellet

class LevelManager:
    def __init__(self, level_file):
        self.level_data = []
        self.walls = []
        self.pellets = []
        self.load_level(level_file)

    def load_level(self, level_file):
        with open(level_file, 'r') as file:
            self.level_data = [line.strip() for line in file]
        self.create_entities()

    def create_entities(self):
        for x, row in enumerate(self.level_data):
            for y, char in enumerate(row):
                position = (x * 20, y * 20)
                if char == 'W':
                    self.walls.append(Wall(position))
                elif char == 'P':
                    self.pellets.append(Pellet(position))

    def draw(self, screen):
        for wall in self.walls:
            wall.draw(screen)
        for pellet in self.pellets:
            pellet.draw(screen)