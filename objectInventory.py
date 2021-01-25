
import createObject, random
global chunk_width
chunk_width = 1
moveableObjects = None
staticObjects = None
BLACK = (0,0,0)
WHITE = (255,255,255) #defining it because currently, during the only build, these are most of the colours to be used.

def createAllMoveable(screen):
    moveableObjects = []
    player = createObject.newMoveable((0,0,0), 50, 75) #player object creation
    player.setParams(615, 450)
    player.setColor((124,124,124))
    moveableObjects.append(player)
    
    return moveableObjects

def createAllStatic(screen):
    screen_width = screen.get_width()
    chunk_width = 1
    prev_y = 650 #actually starting y in this context but needs a starting value
    diff = 1
    staticObjects = {}
    with open('chunks.txt', 'w+') as f:
        for j in range(-1280, screen_width*2, chunk_width):
            f.write(str(j) + "," + str(prev_y) + ";")
            #color, width, height, x, y, screen
            temp = createObject.newStatic((124,124,124), chunk_width, 720-prev_y, j, prev_y, screen)
            staticObjects.update({j: temp} )
            prev_y = random.randint(prev_y-diff, prev_y+diff)
            if prev_y > 710: prev_y = 710

    return staticObjects


class init:

    def __init__(self, screen):
        global staticObjects, moveableObjects
        moveableObjects = createAllMoveable(screen)
        staticObjects = createAllStatic(screen)


    def getStatic(self):
        return staticObjects

    def getMoveable(self):
        return moveableObjects

if __name__ == '__main__':
    class screen:
        def __init__(self):
            self.width = 1280

    testscreen = screen
    testscreen.__init__(testscreen)
    staticObjects = []
    chunk_width = 10
    for i in range(0, screen.width+chunk_width, chunk_width):
        staticObjects.append(str("land_chunk_"+str(i)))
    print(staticObjects)