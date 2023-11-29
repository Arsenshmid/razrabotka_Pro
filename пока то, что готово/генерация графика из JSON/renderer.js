const { ipcRenderer } = require('electron');

document.getElementById('plotButton').addEventListener('click', () => {
    // Здесь можно собрать данные для графика и отправить их на сервер
    const plotData = { /* Ваши данные для графика */ };

    fetch('http://localhost:3000/api/plotData', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(plotData),
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Ошибка:', error));
});

ipcRenderer.on('plotData', (event, plotData) => {
    // Здесь можно использовать полученные данные для отрисовки графика в вашем UI
    console.log('Данные для графика:', plotData);
    // Добавьте ваш код для отрисовки графика в интерфейсе
});
