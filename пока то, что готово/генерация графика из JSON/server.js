const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/api/plotData', (req, res) => {
    const plotData = req.body; // Получаем данные от клиента
    fs.writeFileSync('plotData.json', JSON.stringify(plotData)); // Записываем данные в JSON-файл
    res.send('Данные успешно получены и сохранены.');
});

app.listen(port, () => {
    console.log(`Сервер запущен на порту ${port}`);
});
