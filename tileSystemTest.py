import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1280, 720), vsync=1)
pygame.display.set_caption('Test 1234567890') 
screen.fill((255,255,255))
clock = pygame.time.Clock()
FPS = 60

background = pygame.Surface([1280,720])

pygame.display.update()

class newTile:
    def __init__(self, color, width, height, x, y, tileID): #initialising all the variables.
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
#        self.image = pygame.image.load(tileID+".png").convert_alpha()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(screen, color, (x,y,width,height))
        
    def getImage(self):
        return self.image

    def getRects():
        return True

onScr = []
for i in range(128):
    temp = newTile((124,124,124), 10, 20, i*10, 700, 0)
    onScr.append((temp.getImage(), (temp.rect.x, temp.rect.y)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                onScr.rect.move_ip(5,0)

    

    screen.fill((0,0,0))
    background.blits(onScr)
    screen.blit(background, (0,0))
    pygame.display.update()
    clock.tick(60)
