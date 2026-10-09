import numpy as np

class Perceptron2in:
    def __init__(self, nInputs, lRate=0.01, epochs=1000):
        self.weights = np.zeros(nInputs + 1)  # +1 for the bias term
        self.lRate = lRate
        self.epochs = epochs

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return 1 if summation > 0 else 0

    def train(self, tInputs, labels):
        for _ in range(self.epochs):
            for inputs, label in zip(tInputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.lRate * (label - prediction) * inputs
                self.weights[0] += self.lRate * (label - prediction)

# Example usage
if __name__ == "__main__":
    tInputs = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
        ])
    labels = np.array([0, 0, 0, 1])  # AND gate two inputs

    perceptron = Perceptron2in(nInputs=2)
    perceptron.train(tInputs, labels)

    print(perceptron.predict(np.array([1, 1])))  # Output: 1
    print(perceptron.predict(np.array([0, 0])))  # Output: 0
