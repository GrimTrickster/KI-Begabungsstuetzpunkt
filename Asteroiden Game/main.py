import numpy
import matplotlib.pyplot

import time

#pixels

pixels = []
pixel_y = []
pixelmode = 0
#0 = Nichts
#1 = Asteroid

#player
playerx = 9
playery = 5


def setPlayer():
    pixels[playerx][playery] = 2


def gameGenerator():
    global pixel_y
    for x in range(0, 10):
        for y in range(0, 10):
            # pixel_mode = numpy.random.randint(0, 2)
            pixel_mode = numpy.random.choice([0, 1], p=[0.7, 0.3])

            pixel_y.append(pixel_mode)

        pixels.append(pixel_y)
        pixel_y = []
    setPlayer()

def nextStep(playerStep):
    global playery

    lastPixel = pixels[9]
    for i in range(0, 9):
        pixels[9 - i] = pixels[8 - i]
    pixels[0] = lastPixel

    #Welche Richtung?
    if playerStep == 1:
        playery += 1
    elif playerStep == -1:
        playery -= 1
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
