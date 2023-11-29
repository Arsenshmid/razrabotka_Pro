import numpy as np
import matplotlib.pyplot as plt
import json

"""

Структура входных данных:

complex n_ext - показатель преломления внешней среды
int num_of_layers - количество слоев в элементарной ячейке
int num_of_blocks - количество элементарных ячеек в структуре
layers_parameters - список (или массив) размера num_of_layers из пар чисел [complex n, float d], где
                    n - показатель преломления слоя, d - толщина слоя (в нанометрах)
float wl_start и wl_stop - границы отображаемого диапазона длин волн в нм

Все передается в виде .json файла
Выход:

График зависимости коэффициента пропускания (либо отражения, для этого нужно заменить T_data на R_data в 102 строке)
от длины волны падающего (ортогонально) излучения

Примечание: 

В приницпе можно внести во входные данные параметр, определяющий, какой именно спектр (R(w) или T(w)) нас интересует

"""


def layer_matrix(n_layer, d_layer, wl):
    m = np.zeros((2, 2), 'complex')
    m[0, 0] = np.cos(2 * np.pi * n_layer / wl * d_layer)
    m[0, 1] = (np.sin(2 * np.pi * n_layer / wl * d_layer) / n_layer) * 1j
    m[1, 0] = (np.sin(2 * np.pi * n_layer / wl * d_layer) * n_layer) * 1j
    m[1, 1] = np.cos(2 * np.pi * n_layer / wl * d_layer)
    return m


# построим матрицу переноса через блок
def block_matrix(wl):
    m = layer_matrix(layers_parameters[layers - 1][0], layers_parameters[layers - 1][1], wl)
    for k in reversed(range(layers - 1)):
        m = np.dot(m, layer_matrix(layers_parameters[k][0], layers_parameters[k][1], wl))
        return m


# построим матрицу переноса через всю структуру

def S(wavelen):
    m = np.linalg.matrix_power(block_matrix(wavelen), blocks)
    return m


# построим спектры пропускания и отражения
def run():
    with open("temp\\input_data.json", "r") as file:
        input_data = json.load(file)

    n_ext = complex(input_data['n_ext'])

    global layers
    layers = input_data['num_of_layers']
    global blocks
    blocks = input_data['num_of_blocks']

    global layers_parameters
    layers_parameters = []

    for [eps, d] in input_data['layers_parameters']:
        layers_parameters.append([complex(eps), d * 1e-9])

    wl_start = input_data['wl_start']
    wl_stop = input_data['wl_stop']
    output_option = input_data['output_option']

    # print("  Мы в ядре")
    # print("  Полученные данные")
    # print(f"  {n_ext = }")
    # print(f"  {layers = }")
    # print(f"  {blocks = }")
    # print(f"  {wl_start = }, {wl_stop = }")
    # print('  layers parameters:')
    # for i,[eps, d] in enumerate(layers_parameters):
    #     print(f"  {i+1}. {eps = :.2f}, {d = :.2f}")
    # print()

    R = lambda l: abs((S(l)[0][1] * n_ext ** 2 + (S(l)[0][0] - S(l)[1][1]) * n_ext - S(l)[1][0]) / (
            S(l)[0][1] * n_ext ** 2 - (S(l)[0][0] + S(l)[1][1]) * n_ext + S(l)[1][0])) ** 2

    T = lambda l: abs((2 * n_ext) / (S(l)[0][1] * n_ext ** 2 - (S(l)[0][0] + S(l)[1][1]) * n_ext + S(l)[1][0])) ** 2

    wl_data = np.linspace(wl_start, wl_stop, 1001)
    x_data = list(wl_data)
    match output_option:
        case 'R':
            R_data = list(map(R, wl_data * 1e-9))
            output = {'x': x_data, 'y': R_data}
        case 'T':
            T_data = list(map(T, wl_data * 1e-9))
            output = {'x': x_data, 'y': T_data}

    with open("temp\\output.json", "w") as file:
        json.dump(output, file, indent=2)

# plt.figure()
# plt.plot(wl_data, T_data, color='purple')
# plt.title('Спектр пропускания слоистой структуры')
# plt.xlabel('Длина волны, нм')
# plt.ylabel('Коэффициент пропускания')
# plt.grid()
# plt.show()
