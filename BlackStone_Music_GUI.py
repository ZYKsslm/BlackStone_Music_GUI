import sys
import os
from PIL import Image, ImageQt

from PySide6.QtWidgets import *
from qdarkstyle.dark.palette import DarkPalette
from qdarkstyle.light.palette import LightPalette
from qdarkstyle import load_stylesheet
from ujson import dump

from Ui_mainWidget import Ui_mainWidget
from sponseorshipWindow import *
from work import *


__version__ = "v0.2.0"


class MainWindow(QWidget, Ui_mainWidget):
    def __init__(self):
        super().__init__()
        self.config()
        self.setupUi(self)
        self.bind()

    def config(self):
        with open("config.json", "r", encoding="utf-8") as f:
            configs = load(f)
        self.theme = configs["theme"]
        self.v = configs["v"]
        self.img_file = configs["img_file"]

        music_path = configs["music_path"]
        lyric_path = configs["lyric_path"]

        if music_path == "./Download":
            music_path = os.path.join(os.getcwd(), "Download")
        if lyric_path == "./Download":
            lyric_path = os.path.join(os.getcwd(), "Download")

        # 定义初始下载器对象
        self.downloader = Downloader(self, configs["ua"], configs["thread_num"], music_path, lyric_path)

    def setupUi(self, mainWidget):
        super().setupUi(mainWidget)
        self.setFixedSize(1040, 585)
        self.setWindowOpacity(self.v)
        self.change_theme(app, self.theme)
        if self.img_file is not None:
            self.bgLabel.setPixmap(QPixmap(self.img_file))

        self.verLabel.setText(__version__)
        self.impMenu = QMenu(self)
        self.imp_menu = self.impMenu.addAction("QQ音乐")
        self.impBtn.setMenu(self.impMenu)
        self.source_group = QButtonGroup(self)
        self.source_group.addButton(self.source_1, 1)
        self.source_group.addButton(self.source_2, 2)
        self.source_group.addButton(self.source_3, 3)
        self.source_group.addButton(self.source_4, 4)
        self.source_group.addButton(self.source_5, 5)
        self.source_group.addButton(self.source_6, 6)
        self.musicPathLineEdit.setText(self.downloader.music_path)
        self.lyricPathLineEdit.setText(self.downloader.lyric_path)
        self.comboBox.addItems(["默认", "明亮", "暗黑"])
        self.comboBox.setCurrentText(self.theme)
        self.visSlider.setMinimum(1)
        self.visSlider.setMaximum(10)
        self.visSlider.setSingleStep(1)
        self.visSlider.setValue(7)
        self.threadLineEdit.setText(str(self.downloader.thread_num))
        self.quality_group = QButtonGroup()
        self.quality_group.addButton(self.qCheck_1, 1)
        self.quality_group.addButton(self.qCheck_2, 2)
        self.quality_group.addButton(self.qCheck_3, 3)
        self.quality_group.addButton(self.qCheck_4, 4)
        self.qCheck_1.setEnabled(False)
        self.qCheck_2.setEnabled(False)
        self.qCheck_3.setEnabled(False)
        self.qCheck_4.setEnabled(False)
        self.imp_quality_group = QButtonGroup()
        self.imp_quality_group.addButton(self.qCheck_5, 1)
        self.imp_quality_group.addButton(self.qCheck_6, 2)
        self.imp_quality_group.addButton(self.qCheck_7, 3)
        self.imp_quality_group.addButton(self.qCheck_8, 4)
        # self.qCheck_5.setEnabled(False)
        # self.qCheck_6.setEnabled(False)
        # self.qCheck_7.setEnabled(False)
        # self.qCheck_8.setEnabled(False)
        self.lyricDownBtn.setEnabled(False)
        self.importLyricDownBtn.setEnabled(False)
        # TODO
        self.source_6.setEnabled(False)

    def sponsorshipWindowShow(self):
        self.sponsorshipWindow = sponsorshipWindow()
        self.sponsorshipWindow.show()

    def change_theme(self, widget, theme):
        if theme == "明亮":
            self.theme = "明亮"
            widget.setStyleSheet(load_stylesheet(qt_api="pyside6", palette=LightPalette()))
        elif theme == "暗黑":
            self.theme = "暗黑"
            widget.setStyleSheet(load_stylesheet(qt_api="pyside6", palette=DarkPalette()))
        else:
            self.theme = "默认"
            widget.setStyleSheet("")
    
    def vis(self, level):
        self.v = level / 10
        self.setWindowOpacity(self.v)

    def change_bg(self):
        image = QFileDialog.getOpenFileName(self, "选择图片", ".", "选择图片(*.jpg *.jpeg *.png *.JPG *.JPEG *.PNG)")[0]
        image = Image.open(image)
        suffix = image.format
        image = image.resize((1040, 585))
        image_file = f"Image/wallpaper.{suffix}"
        image.save(image_file)
        self.img_file = image_file
        self.bgLabel.setPixmap(ImageQt.toqpixmap(image))

    def resetStyle(self):
        self.theme = "默认"
        self.v = 0.9
        self.img_file = None

        self.change_theme(app, self.theme)
        self.bgLabel.clear()
        self.setWindowOpacity(self.v)

        self.comboBox.setCurrentText("默认")
        self.visSlider.setValue(self.v * 10)

    def setMusicPath(self):
        path = QFileDialog.getExistingDirectory(self, "选择文件夹", ".")
        self.downloader.music_path = path
        self.musicPathLineEdit.setText(self.downloader.music_path)

    def setLyricPath(self):
        path = QFileDialog.getExistingDirectory(self, "选择文件夹", ".")
        self.downloader.lyric_path = path
        self.lyricPathLineEdit.setText(self.downloader.lyric_path)

    def setThreadNum(self):
        self.downloader.thread_num = int(self.threadLineEdit.text())

    def setUa(self, state):
        if state == 2:
            self.downloader.ua = "random"
        else:
            self.downloader.ua = choice(choice(list(choice(user_agent_json).values())))

    def setSource(self, btn):
        self.downloader.source = btn.text()

    def setQuality(self, btn):
        if btn.objectName() == "母带":
            self.downloader.quality = 1
        elif btn.objectName() == "标准":
            self.downloader.quality = 2
        elif btn.objectName() == "HQ":
            self.downloader.quality = 3
        elif btn.objectName() == "无损":
            self.downloader.quality = 4

    def searchMusic(self):
        if self.downloader.source == "":
            QMessageBox.information(self, "无音源", "未选择音源！")
            return
        elif self.searchLineEdit.text() == "":
            QMessageBox.information(self, "无信息", "请输入查找信息！")
            return
        
        if self.downloader.source == "QQ音乐" or self.downloader.source == "MyFreeMP3":
            self.qCheck_1.setEnabled(True)
            self.qCheck_2.setEnabled(True)
            self.qCheck_3.setEnabled(True)
            self.qCheck_4.setEnabled(True)
        else:
            self.qCheck_1.setEnabled(False)
            self.qCheck_2.setEnabled(False)
            self.qCheck_3.setEnabled(False)
            self.qCheck_4.setEnabled(False)

        if self.downloader.source == "酷狗音乐" or self.downloader.source == "咪咕音乐" or self.downloader.source == "QQ音乐_2":
            self.lyricDownBtn.setEnabled(True)

        self.downloader.current_music = self.searchLineEdit.text()

        self.downloader.search_music(name=self.downloader.current_music)

    def download(self, mode):
        if mode == Mode.MUSIC:
            music_items = self.musicListWidget.selectedItems()
            if not music_items:
                QMessageBox.warning(self, "提示", "您未选择任何音乐")
                return

            music_index = []
            task_id = []
            for item in music_items:
                index = self.musicListWidget.row(item)
                self.taskList.addItem(item.text())
                task_id.append(item.text())
                music_index.append(index)

            for o, n in enumerate(music_index):
                self.downloader.download_music(n, task_id[o])
        
        elif mode == Mode.LYRIC:
            music_index = []
            task_id = []
            for item in music_items:
                index = self.musicListWidget.indexFromItem(item).row()
                self.taskList.addItem(item.text())
                task_id.append(f"{item.text()}")
                music_index.append(index)

            if self.downloader.source == "酷狗音乐":
                for o, n in enumerate(music_index):
                    self.downloader.download_lyric(task_id[o], n)
            else:
                for o, n in enumerate(music_index):
                    self.downloader.download_music(n, task_id[o], Mode.LYRIC)
        
        elif mode == Mode.IMPORT:
            music_items = self.musicImportListWidget.selectedItems()
            if not music_items:
                QMessageBox.warning(self, "提示", "您未选择任何音乐")
                return
            
            music_index = []
            task_id = []
            for item in music_items:
                index = self.musicImportListWidget.row(item)
                self.taskList.addItem(item.text())
                task_id.append(item.text())
                music_index.append(index)

            for o, n in enumerate(music_index):
                self.downloader.download_music(n, task_id[o])
            
    def importSongList(self):
        info = self.searchLineEdit.text()
        if  info == "":
            QMessageBox.information(self, "无信息", "请输入查找信息！")
            return
        
        self.downloader.source = "QQ音乐"
        self.downloader.import_music(info)


    def update(self):
        self.updateCheckBtn.setEnabled(False)
        version, info = update(self.downloader.ua)

        if version == __version__:
            QMessageBox.information(self, "检查更新", f"当前已是最新版本\n{__version__}")
            return
        
        self.latest_version = version
        QMessageBox.information(self, "检查更新", f"有可用的更新\n{version}")
        self.latestInfo.setMarkdown(info)
        self.mainStacked.setCurrentIndex(3)
        self.updateCheckBtn.setEnabled(True)

    def updating(self):
        self.updateLabel.setText("请稍后......")
        self.updateCheckBtn.setEnabled(False)
        self.updateBtn.setEnabled(False)
        self.downloader.update(self.latest_version)

    def bind(self):
        # 搜索按钮绑定
        self.searchBtn.clicked.connect(self.searchMusic)
        self.searchLineEdit.returnPressed.connect(self.searchMusic)
        # 导入歌单菜单按钮绑定
        self.imp_menu.triggered.connect(self.importSongList)
        # 音源按钮组绑定
        self.source_group.buttonClicked.connect(self.setSource)
        # 菜单按钮绑定
        self.taskBtn.clicked.connect(lambda: self.menuStacked.setCurrentIndex(0))
        self.styleBtn.clicked.connect(lambda: self.menuStacked.setCurrentIndex(1))
        self.fileBtn.clicked.connect(lambda: self.menuStacked.setCurrentIndex(2))
        self.downloadBtn.clicked.connect(lambda: self.menuStacked.setCurrentIndex(3))
        self.aboutBtn.clicked.connect(lambda: self.menuStacked.setCurrentIndex(4))
        # 更新按钮绑定
        self.updateCheckBtn.clicked.connect(self.update)
        self.updateBtn.clicked.connect(self.updating)
        # 主题下拉框绑定
        self.comboBox.currentIndexChanged.connect(lambda: self.change_theme(app, self.comboBox.currentText()))
        # 选择背景按钮绑定
        self.bgBtn.clicked.connect(self.change_bg)
        # 窗口透明度滑条绑定
        self.visSlider.valueChanged.connect(self.vis)
        # 恢复默认样式按钮绑定
        self.resetBtn.clicked.connect(self.resetStyle)
        # 打开音乐保存目录按钮绑定
        self.musicOpenBtn.clicked.connect(lambda: os.startfile(self.downloader.music_path))
        # 打开歌词保存目录按钮绑定
        self.lyricOpenBtn.clicked.connect(lambda: os.startfile(self.downloader.lyric_path))
        # 音乐和歌词保存目录选择按钮绑定
        self.musicPathBtn.clicked.connect(self.setMusicPath)
        self.lyricPathBtn.clicked.connect(self.setLyricPath)
        # 线程数设置按钮绑定
        self.threadBtn.clicked.connect(self.setThreadNum)
        # 随机UACheckBox绑定
        self.randomUaCheck.stateChanged.connect(self.setUa)
        # 下载按钮绑定
        self.importMusicDownBtn.clicked.connect(lambda: self.download(Mode.IMPORT))
        self.musicDownBtn.clicked.connect(lambda: self.download(Mode.MUSIC))
        self.lyricDownBtn.clicked.connect(lambda: self.download(Mode.LYRIC))
        # 音乐列表清空按钮绑定
        self.importMusicClearBtn.clicked.connect(self.musicImportListWidget.clear)
        self.musicResClearBtn.clicked.connect(self.musicListWidget.clear)
        # 音质按钮组绑定
        self.quality_group.buttonClicked.connect(self.setQuality)
        # 其他控件绑定
        self.sponserBtn.clicked.connect(self.sponsorshipWindowShow)

    def closeEvent(self, event):
        
        if self.taskList.count():
            res = QMessageBox.question(self, "退出", "当前还有任务正在进行，确定要退出吗？", QMessageBox.Yes | QMessageBox.No)
        else:
            res = QMessageBox.question(self, "退出", "确定要退出吗？", QMessageBox.Yes | QMessageBox.No)

        if res == QMessageBox.Yes:
            with open("config.json", "w", encoding="utf-8") as f:
                config = {
                    "theme": self.theme,
                    "v": self.v,
                    "music_path": self.downloader.music_path,
                    "lyric_path": self.downloader.lyric_path,
                    "img_file": self.img_file,
                    "thread_num": self.downloader.thread_num,
                    "ua": self.downloader.ua
                }
                dump(config, f)
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication()
    
    w = MainWindow()
    w.show()

    sys.exit(app.exec())