import numpy
import matplotlib.pyplot

import time

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
    checkCollission()


def checkCollission():
    return


gameGenerator()


print(pixels)
matplotlib.pyplot.imshow(pixels, cmap='Greys', interpolation='None')
matplotlib.pyplot.show()


nextStep(-1)

print(pixels)


matplotlib.pyplot.imshow(pixels, cmap='Greys', interpolation='None')
matplotlib.pyplot.show()
