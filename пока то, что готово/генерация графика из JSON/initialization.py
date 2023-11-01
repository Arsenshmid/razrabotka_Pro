import json


def init():
    init_data = {
        "input_parameters": {
            'n_ext': {'type': 'string', 'discription': 'Enter the refractive index of the external environment in the format 1+2j: \n'},
            'num_of_layers': {'type': 'int', 'discription': 'Enter the number of layers in the unit cell: \n'},
            'num_of_blocks': {'type': 'int', 'discription': 'Enter the number of elementary cells in the structure: \n'},
            'layers_parameters': {'type': 'list',
                                  'discription': 'a list (or array) of the size num_of_layers of pairs [string n, float d], where n is the refractive index of the layer (in the format 1+2 j), d is the thickness of the layer (in nanometers): \n',
                                  'size':'num_of_layers'},
            'wl_start': {'type': 'float',
                         'discription': 'Enter the left border of the displayed wavelength range in nm: \n'},
            'wl_stop': {'type': 'float',
                        'discription': 'Enter the right border of the displayed wavelength range in nm: \n'}
        },
        "output_options": {'spectrum_type': ['R', 'T']}
    }

    with open("temp\\init.json", "w") as file:
        json.dump(init_data, file, indent=2)


