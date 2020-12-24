
import createObject, random
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
    chunk_width = 10
    screen_width = screen.get_width()
    prev_y = 650 #actually starting y in this context but needs a starting value
    staticObjects = {}
    for i in range(6):
        chunkToGen = 'C_'+str(i) #chunk _ (number)
        staticObjects[chunkToGen] = [] #dictionary of all the rect values in the chunks
        start_x = -960+(320*i) 
        for j in range(0, 320, 10):
            #color, width, height, x, y, screen
            staticObjects[chunkToGen].append((124,124,124), chunk_width, 720-prev_y, start_x + j, prev_y, screen)
            prev_y = random.randint(prev_y-3,prev_y+3)
            if prev_y >= 720: prev_y = 710
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