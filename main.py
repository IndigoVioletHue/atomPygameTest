#Main file, so just drawing the stages and intialising all the objects that'll be used.
#I can see a lot of rewriting potential in this code. Swag B)
import pygame, createObject

BLACK = (0,0,0)
WHITE = (255,255,255) #defining it because currently, during the only build, these are most of the colours to be used.
screen = pygame.display.set_mode((1280, 720)) #Setting Screen
pygame.display.set_caption('Drawing') #Window Name
screen.fill(WHITE)#Fills white to screen
clock = pygame.time.Clock()
FPS = 60 #60FPS 4K Realtime RayTracing B)))))))))))))))

player = createObject.newMoveable() #player object creation
player.setParams(50, 50, 615, 600)
player.setColor(BLACK)
player.drawChar(screen)

land = createObject.newStatic() #land object in the middle, might ditch this idea.
land.setParams(120, 1280, 0, 650 )
land.setColor((124,124,124))

land2 = createObject.newStatic() #right land
land2.setParams(120, 1280, 1280, 650)
land2.setColor((200,124,200))

land3 = createObject.newStatic() #left land
land3.setParams(120, 1280, -1280, 650)
land3.setColor((124,200,124))

land.drawChar(screen) #drawing all of the land characters, as originally it was done every gametick,
land2.drawChar(screen)#before the newStatic class had a tick function
land3.drawChar(screen)

staticObjects = [land, land2, land3] #another reason to do the land differently, i'd have to have a long as heck list.

pygame.init() #intialising pygame
pygame.display.init()
pygame.display.update()

#Loop
running = True
while running: #main gameloop. Kinda stolen?
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: #keydown event handling
            if event.key == pygame.K_w:
                player.inJump()
            elif event.key == pygame.K_a:
                if player.rect.x <= 200:
                    continue
                else:
                    player.setVelX(-5)
                    player.KDPX()
            elif event.key == pygame.K_d:
                if player.rect.x >= 1080:
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
        if player.rect.x >= 1080: #if the player x is a certain number, move the land.
            staticObjects[i].setX(5)
            staticObjects[i].KDPX()
        elif player.rect.x <= 200:
            staticObjects[i].setX(-5)
            staticObjects[i].KDPX()
    pygame.display.update()
