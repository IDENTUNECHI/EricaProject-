import pygame, os, random

#constants
pygame.init()
pygame.camera.init()

WIDTH, HEIGHT = 600 / 2 * 3, 400 / 2 * 3
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF, 32)
CAMEAR = pygame.camera.Camera

WHITE = (255, 255, 255)

FPS = 60
MS = 60

def load_image(name):
    return pygame.image.load(os.path.join('assets', name)).convert_alpha()

# mathf
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, v):
        return ((v.x - self.x) ** 2 + (v.y - self.y) ** 2)

#gameobject
class GameObject:
    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.width = MS
        self.height = MS
        self.image = None
        self.flip_x = False
        self.flip_y = False

    def tick(self):
        pass
        
    def render(self, WIN):
        if self.image == None:
            return
        
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.flip(self.image, self.flip_x, self.flip_y)

        WIN.blit(self.image, (self.position.x - self.width / 2, self.position.y - self.height / 2))
   
#player
class Player(GameObject):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.images = []

        for i in range(6):
            self.images.append(load_image('player' + str(i + 1) + '.png'))

        self.gv = 0
        self.xv = 0
        self.on_ground = False
        self.jump_force = 10
        
        self.animation_index = 0
        self.animation_timer = 0

        self.collision_box = [self.width // 2, self.height]

    def gravity(self):
        self.gv += 0.5

        self.position.y += self.gv
        
        collision_result = self.check_collision()

        if collision_result[0]:
            self.gv = 0
            self.position.y = collision_result[1].position.y - MS
            self.on_ground = True

    def check_collision(self):
        for brick in bricks:
            if abs(brick.position.x - self.position.x) < self.collision_box[0] / 2 + MS / 2 and abs(brick.position.y - self.position.y) < self.collision_box[1] / 2 + MS/2:
                return [True, brick]
            
        return [False, None]
        
    def jump(self):
        if not self.on_ground:
            return
        self.on_ground = False
        self.gv = -self.jump_force

    def animation(self):

        if abs(round(self.xv)) > 0:

            if self.xv >= 0:
                self.flip_x = False
            else:
                self.flip_x = True

            self.animation_timer += 0.2

            if self.animation_timer >= 1:
                self.animation_timer = 0
                self.animation_index += 1

                if self.animation_index > 5:
                    self.animation_index = 0
        else:
            self.animation_index = 0

        self.image = self.images[self.animation_index]
            
    def tick(self):
        self.gravity()

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            self.jump()

        target_xv = 0
        if key[pygame.K_a]:
            target_xv -= 4
        if key[pygame.K_d]:
            target_xv += 4

        self.xv += (target_xv - self.xv) / 2

        backup_x = self.position.x

        self.position.x += self.xv
        if self.check_collision()[0]:
            self.position.x = backup_x

        self.animation()

#brick
class Brick(GameObject):

    def __init__(self, x, y):
        super().__init__(x, y)
        
        self.image = load_image('brick' + str(random.randrange(1, 4)) + '.png')
        self.crop = (0, 0, MS // 3, MS)

class BackgroundBrick(GameObject):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.image = load_image('background_brick' + str(random.randrange(1, 3)) + '.png')
        print('background_brick' + str(random.randrange(1, 3)) + '.png')

#objects
obj_player = Player(0, 200)
bricks = []
background_bricks = []

def init():
    for i in range(20):
        bricks.append(Brick(i * MS, HEIGHT - MS / 3 * 2))
        if i == 5:
            bricks.append(Brick(i * MS, HEIGHT - MS / 3 * 2 - MS))



    for i in range(40):
        for j in range(30):
            background_bricks.append(BackgroundBrick(i * MS, j * MS))

def tick():
    obj_player.tick()

def render():
    WIN.fill(WHITE)

    for background_brick in background_bricks:
        background_brick.render(WIN)

    #render gamma for darkness
    gamma = pygame.Surface((1000,750), pygame.SRCALPHA)
    gamma.fill((0, 0, 0, 180))
    WIN.blit(gamma, (0,0))

    obj_player.render(WIN)
    
    for brick in bricks:
        brick.render(WIN)
    
    pygame.display.update()
    

def main():

    clock = pygame.time.Clock()

    run = True

    init()
    
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
