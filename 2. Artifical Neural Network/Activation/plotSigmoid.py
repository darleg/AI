from numpy import linspace, exp
from pylab import plot, xlabel, ylabel, title, legend, grid, show

# Sigmoid function
def sig(x):
    return 1 / (1 + exp(-x))
# Generate data points
x = linspace(-5, 5, 100)
y = sig(x)
# Plot the function
plot(x, y, label='Sigmoid Function')
xlabel('x')
ylabel('sigmoid(x)')
title('Sigmoid Function used for Activation')
legend()
grid(True)
show()
