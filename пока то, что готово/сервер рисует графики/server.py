from flask import Flask, request, jsonify
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

def your_function_to_process_data(data):
    # Извлеките параметры из данных
    n_ext = float(data['n_ext'])
    layers = int(data['layers'])
    layers_parameters = data['layers_parameters']
    blocks = int(data['blocks'])
    wl_start = float(data['wl_start'])
    wl_stop = float(data['wl_stop'])

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

    # Создайте результаты
    result = {
        'x': wl_data.tolist(),
        'y': T_data,
        # Добавьте другие параметры, если они нужны
    }

    return result

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    result = your_function_to_process_data(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)