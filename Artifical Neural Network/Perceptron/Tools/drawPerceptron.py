import matplotlib.pyplot as plt

def drawPerceptron():
    fig, ax = plt.subplots()

    # Draw the input layer
    iL = ['x1', 'x2', 'x3']
    ws = ['w1', 'w2', 'w3']
    for i, (iN, w) in enumerate(zip(iL, ws)):
        ax.text(0.15, 0.8 - i * 0.3, iN, size=15, ha='center')
        ax.text(0.30, 0.80 - i * 0.2, w, size=10, ha='center')
        ax.plot([0.2, 0.5], [0.8 - i * 0.3, 0.7], 'k-')
    # Draw circles around input nodes
    for i in range(len(iL)):
        ax.add_patch(plt.Circle((0.15, 0.8 - i * 0.3), 0.05, fill=True, color='lightblue'))

    # Draw the summation node
    ax.add_patch(plt.Circle((0.54, 0.7), 0.05, fill=True, color='coral'))
    ax.text(0.54, 0.7, '∑', size=15, ha='center', va='center')

    # Draw the activation function
    ax.add_patch(plt.Circle((0.69, 0.7), 0.05, fill=True, color='violet'))
    ax.text(0.69, 0.7, '\u03C3', size=15, ha='center', va='center')
    ax.plot([0.59, 0.64], [0.7, 0.7], 'k-')

    # Draw the output layer
    ax.text(0.89, 0.7, 'Y', size=15, ha='center')
    ax.plot([0.74, 0.84], [0.7, 0.7], 'k-')
    ax.add_patch(plt.Circle((0.89, 0.7), 0.05, fill=True, color='cyan'))

    

    # Draw the bias term
    ax.text(0.54, 0.9, 'b', size=15, ha='center')
    ax.plot([0.54, 0.54], [0.86, 0.75], 'k-')
    # Draw circle around bias node
    ax.add_patch(plt.Circle((0.54, 0.9), 0.05, fill=True, color='lightgreen'))

    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

drawPerceptron()
