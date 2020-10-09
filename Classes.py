import pygame, createObject

BLACK = (0,0,0)
WHITE = (255,255,255)
screen = pygame.display.set_mode((1280, 720)) #Setting Screen
pygame.display.set_caption('Drawing') #Window Name
screen.fill(WHITE)#Fills white to screen
clock = pygame.time.Clock()
FPS = 60

player = createObject.newMoveable()
player.setParams(50, 50, 615, 600)
player.setColor(BLACK)
player.drawChar(screen)

land = createObject.newStatic()
land.setParams(120, 1280, 0, 650 )
land.setColor((124,124,124))

land2 = createObject.newStatic()
land2.setParams(120, 1280, 1280, 650)
land2.setColor((200,124,200))

land3 = createObject.newStatic()
land3.setParams(120, 1280, -1280, 650)
land3.setColor((124,200,124))

land.drawChar(screen)
land2.drawChar(screen)
land3.drawChar(screen)

staticObjects = [land, land2, land3]

pygame.init()
pygame.display.init()
pygame.display.update()

#Loop
running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.inJump()
            elif event.key == pygame.K_a:
                if player.rect.x <= 200:
                    for i in range(len(staticObjects)):
                        staticObjects[i].setX(5)
                        staticObjects[i].KDPX()
                    continue
                else:
                    player.setVelX(-5)
                    player.KDPX()
            elif event.key == pygame.K_d:
                if player.rect.x >= 1080:
                    for i in range(len(staticObjects)):
                        staticObjects[i].setX(-5)
                        staticObjects[i].KDPX()
                    continue
                else:
                    player.setVelX(5)
                    player.KDPX()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.KUPY()
                for i in range(len(staticObjects)):
                    staticObjects[i].setX(0)
                    staticObjects[i].KUPX()
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                player.KUPX()
                for i in range(len(staticObjects)):
                    staticObjects[i].setX(0)
                    staticObjects[i].KUPX()
        elif event.type == pygame.QUIT:
            running = False
            pygame.quit()


    screen.fill(WHITE)
    clock.tick(FPS)
    player.tick()
    for i in range(len(staticObjects)):
        staticObjects[i].tick()
    pygame.display.update()
