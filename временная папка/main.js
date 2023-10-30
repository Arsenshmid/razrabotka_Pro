const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const fs = require('fs');
const { spawn } = require('child_process');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    }
  });

  mainWindow.loadFile('index.html');
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});

ipcMain.on('submit-data', (event, data) => {
  fs.writeFileSync('data.json', JSON.stringify(data));
  
  // Вызываем Python скрипт с входными данными
  const pythonProcess = spawn('python', ['t.py', data.input1, data.input2]);
  pythonProcess.stdout.on('data', (data) => {
    console.log('Python скрипт вернул:', data.toString());
  });
});
