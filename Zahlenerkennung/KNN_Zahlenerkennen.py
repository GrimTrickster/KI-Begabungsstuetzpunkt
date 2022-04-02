# numpy enthält zahlreiche mathematische Operationen
import numpy
import matplotlib.pyplot

file = open("MNIST\mnist_train.csv")
datalist = file.readlines()

file.close()

# scipy.special enthält die sigmoid-Funktion expit()
import scipy.special


# Klassendefinition des KNN
class neuralNetwork:

    # "Konstruktor" der Klasse
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # Attribute festlegen - Neuronenanzahl der Input-, Verdeckten und Ausgabe-Schicht
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # Definition und Initialisierung der Matrixen mit den Gewichten
        # wih enthält die Gewichte von INPUT->HIDDEN
        # who enthält die Gewichte von HIDDEN->OUTPUT
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        # Festlegung der Lernrate
        self.lr = learningrate

        # Festlegung der Aktivierungsfunktion
        self.activation_function = lambda x: scipy.special.expit(x)

        pass

    # Das KNN trainieren
    def train(self, inputs_list, targets_list):
        # Umwandeln der INPUT-Liste in eine Feld/Matrix (2D)
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))

        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))

        pass

    # query the neural network
    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


# number of input, hidden and output nodes
input_nodes = 784
hidden_nodes = 200
output_nodes = 10

# learning rate is 0.3
learning_rate = 0.3

# create instance of neural network
KNN = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)


x = 0
for record in datalist:
    ## Datenaufbereitung

    #Zerlegt eine Zeile in ein Array
    line_seperated = record.split(',')

    #Umwandlung String => Float
    inputs = ((numpy.asfarray(line_seperated[1:])) / 255.0 * 0.99) + 0.01

    ##Datenaufbereitung der Targets
    targets = numpy.zeros(output_nodes) + 0.01
    targets[int(line_seperated[0])] = 0.99

    KNN.train(inputs, targets)
    x = x + 1
    print(x)
    if (x == 10000):
        break

line_seperated = datalist[2].split(',')
inputs = numpy.asfarray(line_seperated[1:])


print(KNN.query(inputs))