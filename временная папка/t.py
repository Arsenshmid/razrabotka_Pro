import matplotlib.pyplot as plt
import numpy as np

def plot_function(a, b):
    x = np.linspace(a, b, 100)
    y = x**2
    plt.plot(x, y)
    plt.show()

a = float(input("Введите начальное значение x: "))
b = float(input("Введите конечное значение x: "))
plot_function(a, b)
