
from numpy import exp, array, random, dot, sum, transpose

# activation function
def af(x):
    return 1 / (1 + exp(-x))  # Sigmoid

# slope of activation function
def saf(x):
    return x * (1 - x) # drivative of Sigmoid

# Forward Neraul Network Class
# iN:  Input Nodes
# hN:  Hidden Nodes
# oN:  Output Nodes
# hL:  hidden Layers
# lR:  learning Rate
# ws:  weights
# bs:  biases

class FNN:
    def __init__(self, iN, hN, oN, hL=4, lR=0.1):
        self.iN = iN
        self.hN = hN
        self.oN = oN
        self.hL = hL
        self.lR = lR
        
        # Initialize weights and biases
        self.ws = []
        self.bs = []
        
        # Input to first hidden layer
        self.ws.append(random.uniform(size=(self.iN, self.hN)))
        self.bs.append(random.uniform(size=(1, self.hN)))
        
        # Hidden layers
        for _ in range(hL - 1):
            self.ws.append(random.uniform(size=(self.hN, self.hN)))
            self.bs.append(random.uniform(size=(1, self.hN)))
        
        # Last hidden layer to output layer
        self.ws.append(random.uniform(size=(self.hN, self.oN)))
        self.bs.append(random.uniform(size=(1, self.oN)))

    def feedforward(self, inputs):
        self.activations = [inputs]
        
        # Calculate activations for each layer
        for i in range(self.hL + 1):
            net_input = dot(self.activations[-1], self.ws[i]) + self.bs[i]
            activation = af(net_input)
            self.activations.append(activation)
        
        return self.activations[-1]

    def backpropagate(self, inputs, expected_output):
        output_error = expected_output - self.activations[-1]
        deltas = [output_error * saf(self.activations[-1])]
        
        # Calculate error deltas for each layer
        for i in reversed(range(self.hL)):
            error = deltas[-1].dot(self.ws[i + 1].T)
            delta = error * saf(self.activations[i + 1])
            deltas.append(delta)
        
        deltas.reverse()
        
        # Update weights and biases
        for i in range(self.hL + 1):
            self.ws[i] += self.activations[i].T.dot(deltas[i]) * self.lR
            self.bs[i] += sum(deltas[i], axis=0, keepdims=True) * self.lR

    def train(self, inputs, expected_output, iterations):
        for _ in range(iterations):
            self.feedforward(inputs)
            self.backpropagate(inputs, expected_output)

    def predict(self, inputs):
        return self.feedforward(inputs)

# Example usage with XOR problem
inputs = array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
expected_output = array([[0], [1], [1], [0], [1], [0], [0], [1]])

# Create a neural network with 3 input nodes, 4 hidden layers with 4 nodes each, and 1 output node
fnn = FNN(iN=3, hN=4, oN=1)

# Train the neural network
fnn.train(inputs, expected_output, iterations=10000)

# Test the neural network
output = fnn.predict(inputs)
print("Predicted Output:")
print(output)
