# Very Simple neural network with backpropagation
# only two layers input and output

# sm    Sigmoid function
# slope slope or  derivative of Sigmoid function
# dti   dataset for training input
# dto   dataset for training output
# il    input layer
# ol    output layer
# sw    synaptic weights
# err   error
# dlt   delta 

from numpy import exp, array, random, dot, transpose

def sm(data):
    return 1/(1 + exp(-data))

def slope(data):
    return data*(1-data)
    
dti = array([  [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])           
dto = array([[0,0,1,1]]).T
random.seed(1)
sw = 2*random.random((3,1)) - 1

for i in range(10000):
    # start of the forword propagation
    il = dti
    ol = sm(dot(il,sw))
    # backpropagation follows
    err = dto - ol               # calculate the output error 
    dlt = err * slope(ol)        # multiply the error by the derivative of the sigmoid
    sw += dot(transpose(il),dlt) # adjust the synaptic weghts connecting the input and output layers

print ("Output")
print (ol)
