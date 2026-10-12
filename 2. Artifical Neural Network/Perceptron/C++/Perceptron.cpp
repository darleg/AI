// C++ Perceptron Implementation
//
// Implements the basic perceptron algorithm with weight initialization,
// prediction, and training.

#include <iostream>
#include <vector>
#include <cmath>

class Perceptron {
public:
    Perceptron(int numInputs, double learningRate = 0.1, int maxIterations = 1000)
        : learningRate(learningRate), maxIterations(maxIterations) {
        // Initialize weights (including bias) to zero
        weights.resize(numInputs + 1, 0.0);
    }

    // Predict output for given inputs
    int predict(const std::vector<double>& inputs) const {
        double sum = weights[0]; // bias
        for (size_t i = 0; i < inputs.size(); ++i) {
            sum += weights[i + 1] * inputs[i];
        }
        return (sum > 0) ? 1 : 0; // step activation
    }

    // Train using perceptron learning rule
    void train(const std::vector<std::vector<double>>& trainingData,
               const std::vector<int>& labels) {
        for (int iter = 0; iter < maxIterations; ++iter) {
            bool updated = false;
            for (size_t i = 0; i < trainingData.size(); ++i) {
                const std::vector<double>& inputs = trainingData[i];
                int prediction = predict(inputs);
                int target = labels[i];

                if (prediction != target) {
                    double error = target - prediction;
                    for (size_t j = 0; j < inputs.size(); ++j) {
                        weights[j + 1] += learningRate * error * inputs[j];
                    }
                    weights[0] += learningRate * error; // update bias
                    updated = true;
                }
            }
            if (!updated) break; // no more errors
        }
    }

private:
    std::vector<double> weights;
    double learningRate;
    int maxIterations;
};

int main() {
    // Example: AND gate (2 inputs)
    std::vector<std::vector<double>> data = {
        {0.0, 0.0}, {0.0, 1.0}, {1.0, 0.0}, {1.0, 1.0}
    };
    std::vector<int> labels = {0, 0, 0, 1};

    Perceptron p(2, 0.1, 1000);
    p.train(data, labels);

    std::cout << "AND gate predictions:\n";
    for (const auto& x : data) {
        std::cout << "(" << x[0] << ", " << x[1] << ") -> "
                  << p.predict(x) << "\n";
    }

    return 0;
}
