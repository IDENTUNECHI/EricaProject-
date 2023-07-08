from vector import Vector
import pygame

class GameObject:

    position = Vector(0, 0)
    rotation = 0
    image = None
    width = 60
    height = 60

    def __init__(self):
        pass
    
    def tick(self):
        pass

    def render(self, game):
        if self.image == None:
            return

        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        game.screen.blit(self.image, (self.position.x - self.width/2, self.position.y - self.height / 2))
        
