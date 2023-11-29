import json

def get_user_input(param_info):
    param_type = param_info["type"]
    param_description = param_info["description"]
    
    if param_type == "dict":
        key_type = param_info["key_type"]
        value_type = param_info["value_type"]
        
        user_input = {}
        print(param_description)
        
        for _ in range(3):  # Максимальное количество элементов в словаре
            key = input(f"Введите ключ ({key_type}): ")
            if key == "":
                break  # Пользователь завершил ввод
            value = input(f"Введите значение ({value_type}): ")
            user_input[key] = value
    
    elif param_type == "list":
        element_type = param_info["element_type"]
        
        user_input = []
        print(param_description)
        
        for _ in range(5):  # Максимальное количество элементов в списке
            element = input(f"Введите элемент списка ({element_type}): ")
            if element == "":
                break  # Пользователь завершил ввод
            user_input.append(element)
    
    else:
        user_input = input(param_description + f" ({param_type}): ")
    
    return user_input

def main():
    with open("input_parameters.json", "r") as file:
        input_params = json.load(file)

    user_data = {}

    for param_name, param_info in input_params.items():
        user_input = get_user_input(param_info)
        user_data[param_name] = user_input

    print("\nПолученные пользовательские данные:")
    print(json.dumps(user_data, indent=2))

if __name__ == "__main__":
    main()
