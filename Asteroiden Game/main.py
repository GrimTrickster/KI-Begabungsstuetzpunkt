import numpy
import matplotlib.pyplot as plt

# Position data
pixels = []

# Temporary horizontal data
pixel_y = []

# Temporary variable 0 = Nichts 1 = Asteroid
pixelMode = 0


# Player (Start) Coordinates
playerX = 9
playerY = 5


# Sets Player at start-position
def setPlayer(playerXCoordinate, playerYCoordinate):
    pixels[playerXCoordinate][playerYCoordinate] = 2


def generateRow():
    pixelRow = []
    for y in range(0, 10):
        pixel_mode = numpy.random.choice([0, 1], p=[0.8, 0.2])
        pixelRow.append(pixel_mode)
    return pixelRow


def generateGame():
    global pixels
    for x in range(0, 10):
        pixels.append(generateRow())
    setPlayer(playerX, playerY)


def nextStep(playerStep):
    global playerY
    global playerX

    for i in range(0, 9):
        pixels[9 - i] = pixels[8 - i]
    pixels[0] = generateRow()

    if playerStep == "up":
        if not checkCollision(playerX - 1, playerY):
            # Jetzige Position zurücksetzen (Spieler entfernen
            pixels[playerX][playerY] = 0
            # Bei keiner Kollision weitersetzen
            setPlayer(playerX - 1, playerY)
        else:
            # TODO: Remove Test Code
            pixels[playerX][playerY] = 0
            setPlayer(playerX - 1, playerY)


def checkCollision(playerXCoordinates, playerYCoordinates):
    # Collision = True | NoCollision = False
    if pixels[playerXCoordinates][playerYCoordinates] == 1:
        print("You loose")
        return True
    else:
        print("Ok")
        return False


generateGame()

# fig = plt.figure()
# ax = plt.subplot(1, 1, 1)
fig, ax = plt.subplots()
im = ax.imshow(pixels, interpolation=None, cmap='Greys')


plt.pause(1)

for sth in range(0, 10):
    nextStep('up')

    im.set_data(pixels)
    im.draw(fig.canvas.renderer)
    plt.pause(2)
