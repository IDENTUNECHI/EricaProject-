import pygame, os
from player import Player

class Game:
    def __init__(self):
        self.screen = None
        self.running = False
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.CONST_FRAME = 60
        self.WIDTH = 800
        self.HEIGHT = 600

        self.player = Player(self)

    def tick(self):
        self.player.tick()

    def render(self):
        self.screen.fill("white")

        self.player.render(self)
        
    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        if self.running:
            return

        self.running = True
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
        pygame.init()
        pygame.display.set_caption("window")
        
        while self.running:
            
            self.get_event()

            self.tick()
            self.render()

            pygame.display.update()
            pygame.display.flip()

            self.delta_time = self.clock.tick(self.CONST_FRAME) / 1000
