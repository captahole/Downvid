# DownVid
# A Simple Video Downloader for the Web
# pyinstaller --windowed --onefile --ico=/Users/erikmacbookAIR/Library/CloudStorage/Dropbox/Mac/Documents/Coding/YtDL/icon.png downloader.py

import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QLabel, QMessageBox
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QFont

class DownloadThread(QThread):
    status_update = pyqtSignal(str)
    finished = pyqtSignal()
    
    def __init__(self, urls):
        super().__init__()
        self.urls = urls
    
    def run(self):
        import yt_dlp  # Lazy import
        
        video_urls = [url.strip() for url in self.urls.split('\n') if url.strip()]
        
        downloads_folder = os.environ.get('DOWNLOAD_DIR', os.path.join(os.path.expanduser('~'), 'Downloads'))
        
        if not os.path.exists(downloads_folder):
            os.makedirs(downloads_folder)
        
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
            'ignoreerrors': True,
        }
        
        self.status_update.emit(f"Starting download of {len(video_urls)} video(s)...")
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                for url in video_urls:
                    self.status_update.emit(f"Downloading: {url}")
                    ydl.download([url])
            self.status_update.emit("All downloads completed!")
        except Exception as e:
            self.status_update.emit(f"Download failed: {str(e)}")
        
        self.finished.emit()

class YouTubeDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Downloader")
        self.setGeometry(100, 100, 600, 500)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # URL input
        layout.addWidget(QLabel("Video URLs (one per line):"))
        self.url_input = QTextEdit()
        self.url_input.setMaximumHeight(150)
        layout.addWidget(self.url_input)
        
        # Download button
        self.download_btn = QPushButton("Download")
        self.download_btn.clicked.connect(self.start_download)
        layout.addWidget(self.download_btn)
        
        # Quit button
        quit_btn = QPushButton("Quit")
        quit_btn.clicked.connect(self.close)
        layout.addWidget(quit_btn)
        
        # Status display
        layout.addWidget(QLabel("Status:"))
        self.status_display = QTextEdit()
        self.status_display.setReadOnly(True)
        self.status_display.setFont(QFont("Courier", 9))
        layout.addWidget(self.status_display)
    
    def start_download(self):
        urls = self.url_input.toPlainText().strip()
        if not urls:
            QMessageBox.warning(self, "Error", "Please enter at least one URL")
            return
        
        self.download_btn.setEnabled(False)
        self.status_display.clear()
        
        self.download_thread = DownloadThread(urls)
        self.download_thread.status_update.connect(self.update_status)
        self.download_thread.finished.connect(self.download_finished)
        self.download_thread.start()
    
    def update_status(self, message):
        self.status_display.append(message)
    
    def download_finished(self):
        self.download_btn.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec())