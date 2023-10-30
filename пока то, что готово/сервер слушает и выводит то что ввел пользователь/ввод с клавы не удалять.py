import numpy as np
import matplotlib.pyplot as plt

print('Введите значение показателя преломления внешней среды: ')
n_ext = float(input())

print('Введите количество слоев в блоке: ')
layers = int(input())

layers_parameters = []
for i in range(layers):
    n_layer = float(input(f'Введите показатель преломления {i + 1}-го слоя: '))
    d_layer = float(input(f'Введите толщину {i + 1}-го слоя в метрах: ')) * 10**(-9)
    layers_parameters.append([n_layer, d_layer])

print('Введите количество блоков в структуре: ')
blocks = int(input())

print('Введите начальную границу диапазона длин волн (в нм): ')
wl_start = float(input())

print('Введите конечную границу диапазона длин волн (в нм): ')
wl_stop = float(input())

def layer_matrix(n_layer, d_layer, wl):
    m = np.zeros((2, 2), 'complex')
    m[0, 0] = np.cos(2 * np.pi * n_layer / wl * d_layer)
    m[0, 1] = (np.sin(2 * np.pi * n_layer / wl * d_layer) / n_layer) * 1j
    m[1, 0] = (np.sin(2 * np.pi * n_layer / wl * d_layer) * n_layer) * 1j
    m[1, 1] = np.cos(2 * np.pi * n_layer / wl * d_layer)
    return m

def block_matrix(wl):
    m = layer_matrix(layers_parameters[layers - 1][0], layers_parameters[layers - 1][1], wl)
    for k in reversed(range(layers - 1)):
        m = np.dot(m, layer_matrix(layers_parameters[k][0], layers_parameters[k][1], wl))
    return m

def S(wavelen):
    m = np.linalg.matrix_power(block_matrix(wavelen), blocks)
    return m

def R(l):
    return abs((S(l)[0][1] * n_ext ** 2 + (S(l)[0][0] - S(l)[1][1]) * n_ext - S(l)[1][0]) / (
            S(l)[0][1] * n_ext ** 2 - (S(l)[0][0] + S(l)[1][1]) * n_ext + S(l)[1][0])) ** 2

def T(l):
    return abs((2 * n_ext) / (S(l)[0][1] * n_ext ** 2 - (S(l)[0][0] + S(l)[1][1]) * n_ext + S(l)[1][0])) ** 2

wl_data = np.linspace(wl_start, wl_stop, 1001)

T_data = list(map(T, wl_data*1e-9))
R_data = list(map(R, wl_data*1e-9))

plt.figure()
plt.plot(wl_data, T_data, color='purple')
plt.title('Спектр пропускания слоистой структуры')
plt.xlabel('Длина волны, нм')
plt.ylabel('Коэффициент пропускания')
plt.grid()
plt.show()
