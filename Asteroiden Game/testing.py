import numpy
import matplotlib.pyplot as plt
from time import sleep


def main():

    imData = numpy.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ])

    fig = plt.figure()
    ax = plt.subplot(1, 1, 1)
    im = ax.imshow(imData)

    plt.pause(1)

    newImData = numpy.array([[2, 2], [2, 2]])
    im.set_data(newImData)
    im.draw(fig.canvas.renderer)
    plt.pause(1)



main()