import createObject
global staticObjects
BLACK = (0,0,0)
WHITE = (255,255,255) #defining it because currently, during the only build, these are most of the colours to be used.

def createAllMoveable(screen):
    moveableObjects = []
    player = createObject.newMoveable() #player object creation
    player.setParams(75, 50, 615, 450)
    player.setColor(BLACK)
    player.drawChar(screen)
    moveableObjects.append(player)
    
    return moveableObjects

def createAllStatic(screen):
    staticObjects = []
    land = createObject.newStatic() #land object in the middle, might ditch this idea.
    staticObjects.append(land)
    land.setParams(120, 1280, 0, 650)
    land.setColor((124,124,124))
    land.isGround()

    land2 = createObject.newStatic() #right land
    staticObjects.append(land2)
    land2.setParams(120, 1280, 1280, 650)
    land2.setColor((200,124,200))
    land2.isGround()

    leftLand = createObject.newStatic() #left land
    staticObjects.append(leftLand)
    leftLand.setParams(120, 1280, -1280, 650)
    leftLand.setColor((124,200,124))
    leftLand.isGround()

    platform = createObject.newStatic() #platform
    staticObjects.append(platform)
    platform.setParams(50, 300, 50, 480)
    platform.setColor((124,124,124))

    platform2 = createObject.newStatic() #another platform2
    staticObjects.append(platform2)
    platform2.setParams(50, 300, 250, 280)
    platform2.setColor((124,124,124))

    platform3 = createObject.newStatic() #another platform2
    staticObjects.append(platform3)
    platform3.setParams(50, 300, 450, 80)
    platform3.setColor((124,124,124))


    land.drawChar(screen) #drawing all of the land characters, as originally it was done every gametick,
    land2.drawChar(screen)#before the newStatic class had a tick function
    leftLand.drawChar(screen)
    platform.drawChar(screen)
    platform2.drawChar(screen)
    platform3.drawChar(screen)
    return staticObjects


class init:

    def __init__(self, screen):
        global staticObjects, moveableObjects
        staticObjects = createAllStatic(screen)
        moveableObjects = createAllMoveable(screen)

    def getStatic(self):
        return staticObjects

    def getMoveable(self):
        return moveableObjects
