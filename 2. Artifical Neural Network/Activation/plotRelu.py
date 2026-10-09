from numpy import linspace, maximum
from pylab import plot, xlabel, ylabel, title, legend, grid, show

# ReLU function
def relu(x):
    return maximum(0, x)

# Plot the function
x = linspace(-5, 5)
y = relu(x)

# Plotting
plot(x, y, label='ReLU Function',)
xlabel('Input')
ylabel('Output')
title('ReLU Function for Activation')
grid(True)
show()
