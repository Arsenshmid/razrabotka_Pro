const { ipcRenderer } = require('electron');

document.getElementById('data-form').addEventListener('submit', (e) => {
  e.preventDefault();
  
  const input1 = document.getElementById('input1').value;
  const input2 = document.getElementById('input2').value;
  
  const data = {
    input1,
    input2
  };
  
  ipcRenderer.send('submit-data', data);
});
