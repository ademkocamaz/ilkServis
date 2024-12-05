const { updateElectronApp } = require('update-electron-app');
const { app, BrowserWindow } = require('electron');
const path = require('path');
const { shell } = require('electron')



// Handle creating/removing shortcuts on Windows when installing/uninstalling.
if (require('electron-squirrel-startup')) {
  app.quit();
}
const port = 11408

const { spawn } = require('node:child_process');
const startDjangoServer = () => {

  const djangoBackend = spawn(path.join(process.resourcesPath, 'manage.exe'), ['runserver', port, '--noreload']);

  app.on('before-quit', function () {
    djangoBackend.kill();
  });

  return djangoBackend;
}

const createWindow = () => {

  const splashWindow = new BrowserWindow({
    show: false,
    width: 300,
    height: 300,
    center: true,
    frame: false,
    hasShadow: true,
  });

  splashWindow.loadFile(path.join(__dirname, 'splash.html'));
  splashWindow.once('ready-to-show', function () {
    splashWindow.show();
    updateElectronApp();
    startDjangoServer();
    shell.openExternal('https://ilkadam.com.tr')
  });

  // Create the browser window.
  const mainWindow = new BrowserWindow({
    show: false,
    center: true,
    autoHideMenuBar: true,
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
    },
  });

  const http = require('node:http')

  const options = {
    host: '127.0.0.1',
    port: port,
    path: '/',
    method: 'GET'
  };

  function check() {
    http.get(options, function (response) {
      // console.log('statusCode:', response.statusCode);
      // console.log('headers:', response.headers);

      mainWindow.loadURL('http://127.0.0.1:' + port);
      mainWindow.once('ready-to-show', function () {
        splashWindow.close();
        mainWindow.show();
      });
      // Open the DevTools.
      // mainWindow.webContents.openDevTools();

    }).on('error', function (error) {
      // console.log('check_error:', error);
      setTimeout(check, 1000);
    });
  };

  check();

  // and load the index.html of the app.
  //mainWindow.loadFile(path.join(__dirname, 'index.html'));

  // Open the DevTools.
  //mainWindow.webContents.openDevTools();
};

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow);

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and import them here.
