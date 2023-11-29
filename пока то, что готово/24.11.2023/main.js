const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });

  mainWindow.loadFile('index.html');

  // Добавляем слушатель события от процесса рендеринга
  ipcMain.on('request_init_data', (event) => {
    // Чтение файла init.json
    const initFilePath = path.join(__dirname, 'init.json');
    const initData = fs.readFileSync(initFilePath, 'utf-8');
    event.reply('init_data', initData);
  });
}

app.whenReady().then(createWindow);
