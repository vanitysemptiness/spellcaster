const { app, BrowserWindow, ipcMain } = require('electron');
const fs = require('fs');
const pdf = require('pdf-parse');
const path = require('path');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  });

  mainWindow.loadFile('index.html');
  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});

ipcMain.on('pdf-dropped', (event, filePath) => {
  fs.readFile(filePath, (err, buffer) => {
    if (err) {
      console.error('Error loading PDF:', err);
      return;
    }

    pdf(buffer).then((data) => {
      const pdfData = {
        text: data.text,
        info: data.info,
        metadata: data.metadata,
      };

      mainWindow.webContents.send('pdf-loaded', pdfData);
    }).catch((err) => {
      console.error('Error parsing PDF:', err);
    });
  });
});

ipcMain.on('highlight-text', (event, text) => {
  mainWindow.webContents.send('highlight-text', text);
});
