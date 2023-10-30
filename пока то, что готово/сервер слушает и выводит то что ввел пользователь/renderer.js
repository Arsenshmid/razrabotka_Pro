const { ipcRenderer } = require('electron');

document.getElementById('data-form').addEventListener('submit', (e) => {
  e.preventDefault();
  
  const data = document.getElementById('data-input').value;
  
  ipcRenderer.send('submit-data', data);
});


ipcRenderer.on('display-plot', (event, plotData) => {

  document.getElementById('plot-container').innerHTML = '';
  

  const img = document.createElement('img');
  img.src = `data:image/png;base64,${plotData}`;
  

  document.getElementById('plot-container').appendChild(img);
});
