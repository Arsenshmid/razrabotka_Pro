const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const url = require('url');
const fs = require('fs');

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({ width: 800, height: 600 });

    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file:',
        slashes: true
    }));

    mainWindow.on('closed', () => {
        mainWindow = null;
    });
}

app.on('ready', createWindow);

ipcMain.on('requestPlot', (event, arg) => {
    const plotData = JSON.parse(fs.readFileSync('plotData.json')); // Читаем данные из JSON-файла
    event.reply('plotData', plotData); // Отправляем данные обратно в рендер-процесс
});
