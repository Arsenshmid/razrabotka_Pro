const { app, BrowserWindow } = require('electron');  // Импортируем модули Electron для создания приложения и окна.

const path = require('path');  // Импортируем модуль для работы с путями к файлам.

function createWindow () {
  // Создаем функцию для создания окна приложения.
  const win = new BrowserWindow({
    width: 800,  // Устанавливаем ширину окна.
    height: 600,  // Устанавливаем высоту окна.
    webPreferences: {
      nodeIntegration: true,  // Разрешаем использование Node.js в окне приложения.
      contextIsolation: false,  // Отключаем изоляцию контекста для возможности доступа к API Node.js.
    }
  });

  win.loadFile('index.html');  // Загружаем HTML-файл в окне приложения.
}

app.whenReady().then(createWindow);  // Создаем окно приложения, когда оно готово к запуску.

app.on('window-all-closed', function () {
  // Обрабатываем событие закрытия всех окон приложения.
  if (process.platform !== 'darwin') app.quit();  // Закрываем приложение, если не macOS.
});

app.on('activate', function () {
  // Обрабатываем событие активации приложения.
  if (BrowserWindow.getAllWindows().length === 0) createWindow();  // Создаем новое окно, если нет активных окон.
}
