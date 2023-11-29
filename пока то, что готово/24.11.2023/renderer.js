// Чтение файла init.json
const path = require('path');

const fs = require('fs');

fs.readFile(path.join(__dirname, '/init.json'), 'utf-8', (err, data) => {
    if (err) {
        console.error("An error occurred while reading the file:", err);
        return;
    }

    // Парсинг JSON-строки в объект
    const initData = JSON.parse(data);

    // Получение контейнера для полей ввода
    const container = document.getElementById('inputFields');

    // Отрисовка полей ввода
    Object.entries(initData.input_parameters).forEach(([key, value]) => {
        // Создание элемента input и добавление его в контейнер
        const input = document.createElement('input');
        input.id = key;
        input.placeholder = value.discription;
        container.appendChild(input);

        // Создание элемента br и добавление его в контейнер
        const br = document.createElement('br');
        container.appendChild(br);
    });

    // Отрисовка полей выбора
    Object.entries(initData.output_options).forEach(([key, options]) => {
        // Создание элемента select и добавление его в контейнер
        const select = document.createElement('select');
        select.id = key;
        container.appendChild(select);

        // Создание элементов option и добавление их в select
        options.forEach(option => {
            const optionElement = document.createElement('option');
            optionElement.value = option;
            optionElement.text = option;
            select.appendChild(optionElement);
        });

        // Создание элемента br и добавление его в контейнер
        const br = document.createElement('br');
        container.appendChild(br);
    });
});

// Сохранение введенных данных в файл input.json при нажатии на кнопку
document.getElementById('saveButton').addEventListener('click', () => {
    const data = {
        input_parameters: {},
        output_options: {},
    };

    // Сбор введенных данных
    document.querySelectorAll('input').forEach(input => {
        let value = input.value;

        // Проверка на число
        if (!isNaN(value)) {
            value = Number(value);
        }

        // Проверка на комплексное число
        else if (/^[0-9]+[+-][0-9]+j$/.test(value.replace(/\s/g, ''))) {
            value = value.replace(/\s/g, '');
        }

        data.input_parameters[input.id] = value;
    });

    // Сбор выбранных опций
    document.querySelectorAll('select').forEach(select => {
        data.output_options[select.id] = select.value;
    });

    // Запись данных в файл input.json
    fs.writeFile(path.join(__dirname, '/input.json'), JSON.stringify(data), err => {
        if (err) {
            console.error("An error occurred while writing the file:", err);
        }
    });

    // Вывод введенных данных
    const output = document.getElementById('output');
    output.textContent = 'Entered: ' + JSON.stringify(data);
});
