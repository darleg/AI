import matplotlib.pyplot as plt

def drawPerceptron():
    fig, ax = plt.subplots()
    
    # Number of nuerons in layers
    iL = 3
    hL = 4
    # Start Points for drawing
    ixStart = 0.1
    iyStart = 0.8
    hxStart = 0.41
    hyStart = 0.9
    oxStart = 0.71
    oyStart = 0.6
    yHead   = 1.0
    
    # Draw input layer
    for i in range(iL):
        ax.add_patch(plt.Circle((ixStart, iyStart - i * 0.2), 0.05, fill=False, color='lightblue'))
        ax.text(ixStart, iyStart - i * 0.2, i, size=15, ha='center')
    # Draw hidden layer
    for i in range(hL):
        ax.add_patch(plt.Circle((hxStart, hyStart - i * 0.2), 0.05, fill=False, color='coral'))
        ax.text(hxStart, hyStart - i * 0.2, i, size=15, ha='center')
        
    # Draw the output layer
    ax.add_patch(plt.Circle((oxStart, oyStart), 0.05, fill=False, color='violet'))
    
    ax.text(0.71, 0.6, '0', size=15, ha='center')

    # Headings
    ax.text(ixStart, yHead, 'Input', size=15, ha='center')
    ax.text(hxStart, yHead, 'Hidden', size=15, ha='center')
    ax.text(oxStart, yHead, 'Output', size=15, ha='center')

    # Make Connections
    # connect hidden layer to output layer
    hoxLineStart = hxStart + 0.05
    hoxLineEnd   = oxStart - 0.05
    for i in range(hL):
        ax.plot([hoxLineStart, hoxLineEnd], [hyStart - i * 0.2, 0.6], 'g-', lw=0.5)

    # connect input layer to hidden layer
    ihxLineStart = ixStart + 0.05
    ihxLineEnd   = hxStart - 0.05
    for i in range(hL):
        hyEnd = hyStart - i * 0.2
        for i in range(iL):
            ax.plot([ihxLineStart, ihxLineEnd], [iyStart - i * 0.2, hyEnd], 'g-', lw=0.5)
            
            
    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

drawPerceptron()
