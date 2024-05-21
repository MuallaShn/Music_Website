const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
    // Tarayıcı penceresini oluştur.
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false, // Bu güvenlik riski oluşturabilir, kullanımına dikkat edin.
            enableRemoteModule: true  // Electron 10 ve üzeri için gerekli olabilir.
        }
    });

    // index.html dosyasını yükle.
    mainWindow.loadFile('index.html');

    // Geliştirici Araçlarını aç.
    mainWindow.webContents.openDevTools();
}

app.whenReady().then(createWindow);

// Tüm pencereler kapandığında uygulamayı kapat.
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});
