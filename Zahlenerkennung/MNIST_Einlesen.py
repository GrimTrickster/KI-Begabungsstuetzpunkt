import numpy
import matplotlib.pyplot

file = open("MNIST\mnist_train.csv")
datalist = file.readlines()

file.close()

#Zerlegt eine Zeile in ein Array
line_seperated = datalist[0].split(',')

#Umwandlung String => Float ==> 28x28 Matrix
image_array = numpy.asfarray(line_seperated[1:]).reshape((28, 28))

print(image_array)

#Darstellung
matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
matplotlib.pyplot.show()