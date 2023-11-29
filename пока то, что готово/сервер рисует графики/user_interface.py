# -*- coding: utf8 -*-
import json
import initialization
import time
import matplotlib.pyplot as plt
import transfer_matrix_with_init
import os

initialization.init()
folder_path = "C:\\Users\\Тимур\\Transfer_Matrix\\temp"

def set_type(type: str, val: str):
    match type:
        case 'string':
            return val
        case 'int':
            return int(val)
        case 'float':
            return float(val)

def clear_temp():
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f'Ошибка при удалении файла {file_path}. {e}')


"""Чтобы не вводить параметры вручную"""

n_list = ['1.46', '2.2+0.001j']
d_list = [120, 80]
dict_of_values = {'n_ext': '1', 'num_of_layers': 2, 'num_of_blocks': 8, 'wl_start': 400, 'wl_stop': 1400}

"""Открываем файл с параметрами инициализации"""

with open("init.json", "r") as file:
    init_data = json.load(file)

"""Анализируем входные параметры"""

data = init_data['input_parameters'].copy()
input_parameters = init_data['input_parameters'].copy()

for key in input_parameters:
    if input_parameters[key]['type'] == 'list':
        size = input_parameters[key]['size']
        list = []
        for i in range(data[size]):
            # n = input()
            # d = float(input())
            n = n_list[i]
            d = d_list[i]
            print(n, d)
            time.sleep(0.3)
            list.append([n, d])
        data[key] = list
    else:
        # value = input(input_parameters[key]['discription'])
        print(input_parameters[key]['discription'], end=' ')
        value = dict_of_values[key]
        data[key] = set_type(input_parameters[key]['type'], value)
        print(value)
        time.sleep(0.3)

print("-" * 30)
print(data)

"""Обрабатываем параметры выхода"""

for key in init_data['output_options']:
    variants = init_data['output_options'][key]
    print(f'Выберите одну из опций: {variants}')

    # output_option = input(f'Выберите одну из опций: {variants} \n')
    # output_option = 'T'

    output_option = "T"
    time.sleep(0.1)
    print(output_option)
    match output_option:
        case 'R':
            title = "Спектр отражения слоистой структуры"
            label = "Коэффициент отражения"
        case 'T':
            title = "Спектр пропускания слоистой структуры"
            label = "Коэффициент пропускания"

data['output_option'] = output_option

"""Отправляем вход на ядро"""

with open("temp\\input_data.json", "w") as file:
    json.dump(data, file, indent=2)

transfer_matrix_with_init.run()

"""Получаем выход с ядра"""

with open("temp\\output.json", "r") as file:
    output_data = json.load(file)

"""Отрисовываем выход"""

plt.figure()
plt.plot(output_data['x'], output_data['y'], color='purple')
plt.title(title)
plt.xlabel('Длина волны, нм')
plt.ylabel(label)
plt.grid()
plt.show()

clear_temp()