const fs = require('fs');
const Plotly = require('plotly.js-dist');
const graphDiv = document.getElementById('graphDiv');
document.getElementById('graphButton').addEventListener('click', () => {
  fs.readFile('graph_data.json', (err, data) => {
    if (err) throw err;
    let graphData = JSON.parse(data);
    let trace = {
      x: graphData['x'],
      y: graphData['y'],
      mode: 'lines'
    };
    let layout = {
      title: 'График',
      xaxis: {
        title: 'Длина волны (нм)'
      },
      yaxis: {
        title: 'Интенсивность'
      }
    };
    Plotly.newPlot(graphDiv, [trace], layout);
  });
});
