import matplotlib.pyplot as plt

def grey1(a):
    plt.imshow(a, cmap = 'Greys')
    plt.xticks([])
    plt.yticks([])
    plt.show()

def grey2(a):
    plt.imshow(a, cmap = 'gray')
    plt.xticks([])
    plt.yticks([])
    plt.show()