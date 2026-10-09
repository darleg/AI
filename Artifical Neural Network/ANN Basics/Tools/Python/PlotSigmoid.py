from numpy import linspace, exp
from pylab import plot, xlabel, ylabel, title, show

def sm(data):
    return 1/(1 + exp(-data))

data = linspace(-5, 5, 200)

plot(data, sm(data))
xlabel("data")
ylabel("Sigmoid(data)")
title("Sigmoid funtion used for Activation")
show()
