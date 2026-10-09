#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// activation function
double af(double x) {
    return 1.0 / (1.0 + exp(-x)); // Sigmoid
}

// slope of activation function
double saf(double x) {
    return x * (1.0 - x);  // drivative of sigmoid
}

// iN:  input Nodes
// hN:  hidden Nodes
// oN:  output Nodes
// iL:  input Layer
// hL:  hidden Layer
// oL:  output Layer
// wIH: weights Input Hidden
// wHO: weights Hidden Output
// w:   weight
// lR:  learning Rate
// oE:  output Errors
// hE:  hidden Errors
class FNN {
private:
    int iN, hN, oN;
    vector<double> iL, hL, oL;
    vector<vector<double>> wIH, wHO;
    double lR;

public:
    FNN(int iN, int hN, int oN, double lR = 0.1)
        : iN(iN), hN(hN), oN(oN), lR(lR) {
        iL.resize(iN);
        hL.resize(hN);
        oL.resize(oN);

        // Initialize weights with random values
        wIH.resize(iN, vector<double>(hN));
        wHO.resize(hN, vector<double>(oN));

        srand(time(0));
        for (auto& row : wIH)
            for (auto& w : row)
                w = ((double)rand() / RAND_MAX) * 2 - 1; // Random values between -1 and 1

        for (auto& row : wHO)
            for (auto& w : row)
                w = ((double)rand() / RAND_MAX) * 2 - 1; // Random values between -1 and 1
    }

    void feedforward(const vector<double>& inputs) {
        iL = inputs;

        for (int i = 0; i < hN; ++i) {
            hL[i] = 0.0;
            for (int j = 0; j < iN; ++j) {
                hL[i] += iL[j] * wIH[j][i];
            }
            hL[i] = af(hL[i]);
        }

        for (int i = 0; i < oN; ++i) {
            oL[i] = 0.0;
            for (int j = 0; j < hN; ++j) {
                oL[i] += hL[j] * wHO[j][i];
            }
            oL[i] = af(oL[i]);
        }
    }

    void backpropagate(const vector<double>& targets) {
        vector<double> oE(oN);
        for (int i = 0; i < oN; ++i)
            oE[i] = targets[i] - oL[i];

        vector<double> hE(hN);
        for (int i = 0; i < hN; ++i) {
            hE[i] = 0.0;
            for (int j = 0; j < oN; ++j)
                hE[i] += oE[j] * wHO[i][j];
            hE[i] *= saf(hL[i]);
        }

        for (int i = 0; i < hN; ++i)
            for (int j = 0; j < oN; ++j)
                wHO[i][j] += lR * oE[j] * hL[i];

        for (int i = 0; i < iN; ++i)
            for (int j = 0; j < hN; ++j)
                wIH[i][j] += lR * hE[j] * iL[i];
    }

    void train(const vector<double>& inputs, const vector<double>& targets, int epochs) {
        for (int epoch = 0; epoch < epochs; ++epoch) {
            feedforward(inputs);
            backpropagate(targets);
        }
    }

    vector<double> predict(const vector<double>& inputs) {
        feedforward(inputs);
        return oL;
    }
};

int main() {
    FNN fnn(3, 4, 1); // 3 input nodes, 4 hidden nodes, 1 output node

    // Training data for a simple problem (e.g., XOR with an additional input)
    vector<vector<double>> trainingInputs = { {0, 0, 0}, {0, 0, 1}, {0, 1, 0}, {0, 1, 1}, {1, 0, 0}, {1, 0, 1}, {1, 1, 0}, {1, 1, 1} };
    vector<vector<double>> trainingOutputs = { {0}, {1}, {1}, {0}, {1}, {0}, {0}, {1} };

    // Train the neural network
    for (int i = 0; i < trainingInputs.size(); ++i)
        fnn.train(trainingInputs[i], trainingOutputs[i], 10000);

    // Test the neural network
    for (int i = 0; i < trainingInputs.size(); ++i) {
        vector<double> output = fnn.predict(trainingInputs[i]);
        cout << trainingInputs[i][0] << " " << trainingInputs[i][1] << " " << trainingInputs[i][2] << " => " << output[0] << endl;
    }

    return 0;
}

