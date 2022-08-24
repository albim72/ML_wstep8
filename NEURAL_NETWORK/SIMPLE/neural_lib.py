import numpy as np

class SimpleNeuralNetwork:

    #konstruktor->definicja -> losowanie trzech wag (0,1)
    def __init__(self):
        np.random.seed(1)
        self.weights = 2*np.random.random((3,1)) - 1

    #definicja funckji propagacji - sigmoid
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    #różniczka z funckji sigmoid
    def d_sigmoid(self,x):
        return x*(1-x)

    #funkcja treningu, funkcja propagacji i fuunkcja propagacji wstecznej

    def train(self,train_input,train_output,train_iters):
        for _ in range(train_iters):
            propagation_result = self.propagation(train_input)
            self.backward_propagation(propagation_result,train_input,train_output)

    def propagation(self,inputs):
        return self.sigmoid(np.dot(inputs.astype(float),self.weights))

    def backward_propagation(self,propagation_result,train_input,train_output):

        error = train_output - propagation_result
        self.weights += np.dot(train_input.T, error*self.d_sigmoid(propagation_result))



