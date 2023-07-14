import pygame, os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)

FPS = 60

IMAGE_PLAYER = pygame.image.load(os.path.join('assets', 'player.png'))

def tick():
    pass

def render():
    WIN.fill(WHITE)

    WIN.blit(IMAGE_PLAYER, (300, 100))
    
    pygame.display.update()
    

def main():

    clock = pygame.time.Clock()

    run = True
    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        tick()
        render()
        
    pygame.quit()

if __name__ == "__main__":
    main()
