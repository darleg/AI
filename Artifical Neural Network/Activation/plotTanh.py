from numpy import linspace, exp, tanh
from pylab import plot, xlabel, ylabel, title, legend, grid, show

# Generate data points
x = linspace(-5, 5, 100)
y = tanh(x)
# Plot the function
plot(x, y, label='Tanh Function')
xlabel('x')
ylabel('tanh(x)')
title('Tanh Function used for Activation')
legend()
grid(True)
show()
