# Simple forward propagation neural network
# three layers input, hidden and output

# sig   Sigmoid function
# slope slope or  derivative of Sigmoid function
# dti   dataset for training input
# dto   dataset for training output
# il    input layer
# hl    hidden layer
# ol    output layer
# sw0   synaptic weight0
# sw1   synaptic weight1
# olerr output layer error
# oldlt output layer delta
# hlerr hidden layer error
# hldlt hidden layer delta

from numpy import exp, array, random, dot, transpose

def sig(x):
    return 1/(1 + exp(-x))

def slope(x):
    return x*(1-x)
    
    
dti = array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])               
dto = array([[0],[1],[1],[0]])
random.seed(1)
sw0 = 2*random.random((3,4)) - 1
sw1 = 2*random.random((4,1)) - 1

for i in range(10000):
    # start of the forward propagation
    il = dti
    hl = sig(dot(il,sw0))
    ol = sig(dot(hl,sw1))
    # backpragation follows
    olerr = dto - ol                     # calculate the output layer error
    oldlt = olerr*slope(ol)              # multiply the output error by the derivative of the sigmoid
    hlerr = oldlt.dot(transpose(sw1))    # calculate the hidden layer error that contribute the output layer
    hldlt = hlerr * slope(hl)            # multiply the hidden error by the derivative of the sigmoid
    sw1 += transpose(hl).dot(oldlt)      # adjust the synaptic weghts connecting hidden and output layers
    sw0 += transpose(il).dot(hldlt)      # adjust the synaptic weghts connecting inputo and hidden layers

print('Output')
print(ol)
