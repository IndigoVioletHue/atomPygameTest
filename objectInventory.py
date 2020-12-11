
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
    staticObjects = []
    chunk_width = 10
    screen_width = screen.get_width()
    prev_y = 650 #actually starting y in this context but needs a starting value
    #(color, width, height, x, y, screen)
    with open('chunks.txt', 'w+') as f:
        for i in range(0, screen_width+(chunk_width*2), chunk_width):
            staticObjects.append("(" + str(i) + "," + str(prev_y) + ")") #getting a list of all the chunks to be made along the bottom of the screen
            f.write("(" + str(i) + "," + str(prev_y) + ");")
            staticObjects[i//chunk_width] = createObject.newStatic((124,124,124), chunk_width, 720-prev_y, i, prev_y, screen)
            staticObjects[i//chunk_width].isGround()
            prev_y = random.randint(prev_y-5,prev_y+5)
            if prev_y >= 720: prev_y = 710
    f.close()
#
#    with open('chunk_data/chunk1.txt', 'w+') as f:
#        prev_y = random.randint(prev_y-1,prev_y+1)
#        for i in range(0, screen_width+(chunk_width*2), chunk_width):
#            f.write("(" + str(i) + "," + str(prev_y) + ");")
#            prev_y = random.randint(prev_y-1,prev_y+1)
#            if prev_y >= 720: prev_y = 710
#    f.close()

#    with open('chunk_data/chunk-1.txt', 'w+') as f:
#        x = open('chunk_data/chunk0.txt','r')
#        x = x.read()
#        x = x.split(";")
#        y = x[0]
#        y.split(",")
#        prev_y = int(y[1])

#        for i in range(screen_width+(chunk_width*2), 0 , -(chunk_width)):
#            f.write("(" + str(i) + "," + str(prev_y) + ");")
#            prev_y = random.randint(int(prev_y)-1,int(prev_y)+1)
#            if prev_y >= 720: prev_y = 710
#    f.close()

#    platform = createObject.newStatic((124,124,124), 300, 50, 50, 480, screen) #platform
#    staticObjects.append(platform)

#    platform2 = createObject.newStatic((124,124,124), 300, 50, 250, 280, screen) #another platform2
#    staticObjects.append(platform2)

#    platform3 = createObject.newStatic((124,124,124), 300, 50, 450, 80, screen) #another platform2
#    staticObjects.append(platform3)

#    platform4 = createObject.newStatic((124,124,124), 300, 50, 450, -80, screen) #another platform2
#    staticObjects.append(platform4)

#    text1 = createObject.newText("5000", 36, (124,124,124))


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