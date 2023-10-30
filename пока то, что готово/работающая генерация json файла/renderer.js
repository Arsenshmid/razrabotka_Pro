const fs = require('fs');  // Подключаем модуль для работы с файловой системой.

document.getElementById('generateButton').addEventListener('click', () => {
  let inputField = document.getElementById('inputField');  // Получаем доступ к текстовому полю.
  extractJsonFile(inputField.value);  // Вызываем функцию для создания JSON-файла на основе введенных данных.
});

function extractJsonFile(inputData) {
  let data = { text: inputData };  // Создаем объект данных для JSON с введенным текстом.
  fs.writeFile('output.json', JSON.stringify(data, null, 2), (err) => {
    if (err) throw err;  // Обрабатываем возможные ошибки при записи в файл.
    console.log('Data written to file');  // Выводим сообщение о завершении записи данных в файл.
  });
}
