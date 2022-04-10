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
    global pixels
    global playerX
    global playerY

    pixels[playerXCoordinate][playerYCoordinate] = 2
    playerX = playerXCoordinate
    playerY = playerYCoordinate


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
    global pixels

    for i in range(0, 9):
        pixels[9 - i] = pixels[8 - i]
    pixels[0] = generateRow()

    if playerStep == "up":
        if not checkAsteroidCollision(playerX - 1, playerY) and not checkBorderCollision(playerX - 1, playerY):
            # Jetzige Position zurücksetzen (Spieler entfernen)
            # Fall-Bewegung vorbeugen
            try:
                pixels[playerX + 1][playerY] = 0
            except IndexError:
                pixels[playerX][playerY] = 0

            # Bei keiner Kollision weitersetzen
            setPlayer(playerX - 1, playerY)
        else:
            # TODO: Remove Test Code
            try:
                pixels[playerX + 1][playerY] = 0
            except IndexError:
                pixels[playerX][playerY] = 0
            setPlayer(playerX, playerY)

    elif playerStep == "down":
        if not checkAsteroidCollision(playerX + 1, playerY) and not checkBorderCollision(playerX + 1, playerY):
            pixels[playerX][playerY] = 0
            setPlayer(playerX + 1, playerY)
        else:
            # TODO: Remove Test Code
            pixels[playerX][playerY] = 0
            setPlayer(playerX, playerY)

    elif playerStep == "left":
        if not checkAsteroidCollision(playerX, playerY - 1) and not checkBorderCollision(playerX, playerY - 1):
            # Jetzige Position zurücksetzen (Spieler entfernen)
            # Fall-Bewegung vorbeugen
            try:
                pixels[playerX + 1][playerY] = 0
            except IndexError:
                pixels[playerX][playerY] = 0

            # Bei keiner Kollision weitersetzen
            setPlayer(playerX, playerY - 1)
        else:
            # TODO: Remove Test Code
            try:
                pixels[playerX + 1][playerY] = 0
            except IndexError:
                pixels[playerX][playerY] = 0
            setPlayer(playerX, playerY)

    elif playerStep == "right":
        if not checkAsteroidCollision(playerX, playerY + 1) and not checkBorderCollision(playerX, playerY + 1):
            # Jetzige Position zurücksetzen (Spieler entfernen)
            try:
                pixels[playerX + 1][playerY] = 0
            except IndexError:
                pixels[playerX][playerY] = 0
            # Bei keiner Kollision weitersetzen
            setPlayer(playerX, playerY + 1)
        else:
            # TODO: Remove Test Code
            try:
                pixels[playerX + 1][playerY] = 0
            except IndexError:
                pixels[playerX][playerY] = 0
            setPlayer(playerX, playerY)

    else:
        pixels[playerX][playerY] = 0
        setPlayer(playerX, playerY)


def checkAsteroidCollision(playerXCoordinates, playerYCoordinates):
    # Collision = True | NoCollision = False

    # Wegen prüfen möglicher zukünftiger Werte, die nicht existieren könnten:
    try:
        if pixels[playerXCoordinates][playerYCoordinates] == 1:
            print("You loose")
            return True
        else:
            print("Ok")
            return False
    except IndexError:
        pass


def checkBorderCollision(playerXCoordinates, playerYCoordinates):
    # Collision = True | NoCollision = False

    #  Zukünftiger Wert außerhalb Array
    if playerYCoordinates == -1 or playerYCoordinates == 10 or playerXCoordinates == -1 or playerXCoordinates == 10:
        return True
    else:
        return False


generateGame()

# fig = plt.figure()
# ax = plt.subplot(1, 1, 1)
fig, ax = plt.subplots()
im = ax.imshow(pixels, interpolation=None, cmap='Greys')

pattern = ['up', 'up', 'left', 'left', 'up', 'right', 'right', 'right', 'right', 'right', 'down', 'down']

plt.pause(1)

for iterations in range(0, len(pattern)):
    nextStep(pattern[iterations])

    im.set_data(pixels)
    im.draw(fig.canvas.renderer)
    plt.pause(2)
