import numpy
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from time import sleep


def nextStep():
    newImData = numpy.array([[2, 2], [2, 2]])
    im.set_data(newImData)
    im.draw(fig.canvas.renderer)
    plt.pause(1)


def submit(text):
    nextStep()
    print(text)


axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
textBox = TextBox(axbox, 'Submit: ', 'type sth')
textBox.on_submit(submit)

imData = numpy.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ])

fig = plt.figure()
ax = plt.subplot(1, 1, 1)
im = ax.imshow(imData)
