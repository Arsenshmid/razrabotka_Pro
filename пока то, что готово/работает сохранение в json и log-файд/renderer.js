const { ipcRenderer } = require('electron');

document.getElementById('data-form').addEventListener('submit', (e) => {
  e.preventDefault();
  
  const data = document.getElementById('data-input').value;
  
  ipcRenderer.send('submit-data', data);
});
