import matplotlib.pyplot as plt
import numpy as np

def plot_graph(data):
    input1 = float(data['input1'])
    input2 = float(data['input2'])

    x = np.linspace(0, 10, 100)
    y = np.sin(input1 * x) * np.exp(-input2 * x)

    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('График')
    plt.grid(True)
    plt.show()
