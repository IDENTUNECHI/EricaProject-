import pygame, os
from vector import Vector
from game_object import GameObject

class Player(GameObject):
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load(os.path.join('assets', 'player.png'))
        self.position.x = game.WIDTH / 2
        self.position.y = game.HEIGHT / 2
        
    def tick(self):
        self.position.x += 2
