import numpy
import matplotlib.pyplot as plt


#Position data
pixels = []

#Temporary horizontal data
pixel_y = []

#Temporary variable 0 = Nichts 1 = Asteroid
pixelMode = 0


#Player (Start) Coordinates
playerX = 9
playerY = 5


#Sets Player at start-position
def setPlayer():
    pixels[playerX][playerY] = 2


#Generate random Game Data
def gameGenerator():
    global pixel_y
    global pixels
    pixels = []

    # multiple horizontal lines
    for x in range(0, 10):
        # 1 horizontal line
        for y in range(0, 10):
            # Asteroid or not (with probability)
            pixel_mode = numpy.random.choice([0, 1], p=[0.7, 0.3])

            #set temporary horizontal line
            pixel_y.append(pixel_mode)

        #Add all lines to big data
        pixels.append(pixel_y)
        pixel_y = []
    setPlayer()


def nextStep(playerStep):
    #To change variables outside functions: global
    global playerY

    lastPixels = pixels[9]
    for i in range(0, 9):
        pixels[9 - i] = pixels[8 - i]
    pixels[0] = lastPixels

    #Welche Richtung?
    if playerStep == 1:
        playerY += 1
    elif playerStep == -1:
        playerY -= 1
    setPlayer()
    checkCollision()


def checkCollision():
    return


gameGenerator()

fig = plt.figure()
ax = plt.subplot(1, 1, 1)
im = ax.imshow(pixels, interpolation=None, cmap='Greys')

plt.pause(1)


for sth in range(0, 10):
    nextStep(-1)

    im.set_data(pixels)
    im.draw(fig.canvas.renderer)
    plt.pause(0.5)
