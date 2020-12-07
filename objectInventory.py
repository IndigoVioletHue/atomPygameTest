import createObject
moveableObjects = None
staticObjects = None
BLACK = (0,0,0)
WHITE = (255,255,255) #defining it because currently, during the only build, these are most of the colours to be used.

def createAllMoveable(screen):
    moveableObjects = []
    player = createObject.newMoveable((0,0,0), 50, 75) #player object creation
    player.setParams(615, 450)
    player.setColor(BLACK)
    moveableObjects.append(player)
    
    return moveableObjects

def createAllStatic(screen):
    staticObjects = []
    #(color, width, height, x, y, screen)
    land = createObject.newStatic((124,124,124), 2560, 120, 0, 650, screen) #land object in the middle, might ditch this idea.
    staticObjects.append(land)
    land.isGround()

    land2 = createObject.newStatic((200,124,200), 1280, 120, 1280, 650, screen) #right land
    staticObjects.append(land2)
    land2.isGround()

    leftLand = createObject.newStatic((124,200,124), 1280, 120, -1280, 650, screen) #left land
    staticObjects.append(leftLand)
    leftLand.isGround()

    platform = createObject.newStatic((124,124,124), 300, 50, 50, 480, screen) #platform
    staticObjects.append(platform)

    platform2 = createObject.newStatic((124,124,124), 300, 50, 250, 280, screen) #another platform2
    staticObjects.append(platform2)

    platform3 = createObject.newStatic((124,124,124), 300, 50, 450, 80, screen) #another platform2
    staticObjects.append(platform3)

    platform4 = createObject.newStatic((124,124,124), 300, 50, 450, -80, screen) #another platform2
    staticObjects.append(platform4)

    text1 = createObject.newText("5000", 36, (124,124,124))

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
