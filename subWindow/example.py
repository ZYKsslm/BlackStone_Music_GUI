import sys
from PySide6.QtCore import Qt
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider
from PySide6.QtMultimedia import QMediaFormat

class MyAudioPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.positionChanged.connect(self.positionChanged)
        self.audioOutput.setVolume(1)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

    def positionChanged(self, position):
        duration = self.player.duration()
        if duration > 0:
            progress = position / duration * 100
            self.slider.setValue(progress)

    def play(self):
        fp = 'F:\music\One Last Kiss-宇多田光.flac'
        self.player.setSource(QUrl.fromLocalFile(fp))
        self.player.play()

if __name__ == '__main__':
    # print(get_supported_mime_types())
    app = QApplication(sys.argv)
    audioPlayer = MyAudioPlayer()
    audioPlayer.setCentralWidget(audioPlayer.slider)
    audioPlayer.show()
    audioPlayer.play()
    sys.exit(app.exec())
