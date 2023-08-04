import sys
import os

from PySide6.QtWidgets import *
from PySide6.QtCore import QThread
from PySide6.QtGui import QPixmap, QColor
from qfluentwidgets import SplitFluentWindow, setTheme, Theme, setThemeColor, FluentIcon, ColorPickerButton, NavigationItemPosition, Dialog, StateToolTip
from ujson import dump, load

from subWindow.searchWidget import SearchWindow
from subWindow.importWidget import ImportWindow
from subWindow.taskWidget import TaskWindow
from subWindow.settingWidget import SettingWindow
from subWindow.aboutWidget import AboutWindow
from source.work import Downloader, check_network


__version__ = "v0.2.1"


class Window(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.config()
        self.setupUi()
        self.bind()
        
    def config(self):
        with open("source/config.json", "r", encoding="utf-8") as f:
            configs = load(f)

        music_path = configs["music_path"]
        lyric_path = configs["lyric_path"]

        if music_path == "./Download":
            music_path = os.path.join(os.getcwd(), "Download")
        if lyric_path == "./Download":
            lyric_path = os.path.join(os.getcwd(), "Download")
            
        configs["music_path"] = music_path
        configs["lyric_path"] = lyric_path
        
        theme = configs["theme"]
        if theme == "明亮":
            setTheme(Theme.LIGHT)
        elif theme == "暗黑":
            setTheme(Theme.DARK)
        else:
            setTheme(Theme.AUTO)
            
        self.tasks = {}
        self.source = ""
        self.import_source = ""
        self.configs = configs
        
        if self.configs["checkNetwork"]:
            res = check_network(self.configs["ua"])
            if not res:
                Dialog("网络连接失败", "网络连接异常，请检查网络连接！", self).show()


    def setupUi(self):
        self.setFixedSize(1040, 585)
        self.setWindowIcon(QPixmap("source/Image/Icon.ico"))
        self.setWindowTitle("BlackStone_Music_GUI")
        self.setWindowOpacity(self.configs["v"])
        setThemeColor(QColor(self.configs["theme_color"]))
        
        # 子界面
        self.searchWindow = SearchWindow()
        self.importWindow = ImportWindow()
        self.taskWindow = TaskWindow()
        self.settingWindow = SettingWindow()
        self.aboutWindow = AboutWindow()
        
        img_file = self.configs["img_file"]
        
        if img_file is not None:
            self.settingWindow.bgViewLabel.setPixmap(QPixmap(img_file).scaled(160, 90))
            self.searchWindow.bgLabel.setPixmap(QPixmap(img_file).scaled(991, 585))
            self.importWindow.bgLabel.setPixmap(QPixmap(img_file).scaled(991, 585))
            self.taskWindow.bgLabel.setPixmap(QPixmap(img_file).scaled(991, 585))
            self.settingWindow.bgLabel.setPixmap(QPixmap(img_file).scaled(991, 585))
            self.aboutWindow.bgLabel.setPixmap(QPixmap(img_file).scaled(991, 585))
        
        self.settingWindow.threadNumEdit.setText(str(self.configs["thread_num"]))
        self.settingWindow.colorBtn = ColorPickerButton(QColor(self.configs["theme_color"]), "选择主题颜色", self.settingWindow.colorFrame, True)
        self.settingWindow.colorBtn.move(478, 2)
        if self.configs["ua"] == "random":
            self.settingWindow.randomUaBtn.setChecked(True)
            self.settingWindow.selfUaEdit.setEnabled(False)
        else:
            self.settingWindow.randomUaBtn.setChecked(False)
            self.settingWindow.selfUaEdit.setText(self.configs["ua"])
        if self.configs["downloadTip"] == True:
            self.settingWindow.downloadTipBtn.setChecked(True)
        else:
            self.settingWindow.downloadTipBtn.setChecked(False)
        if self.configs["checkNetwork"]:
            self.settingWindow.checkNetworkBtn.setChecked(True)
        else:
            self.settingWindow.checkNetworkBtn.setChecked(False)
        self.settingWindow.themeBox.setCurrentText(self.configs["theme"])
        self.settingWindow.opacitySlider.setValue(self.configs["v"]*10)
        self.settingWindow.musicPathEdit.setText(self.configs["music_path"])
        self.settingWindow.lyricPathEdit.setText(self.configs["lyric_path"])
        self.aboutWindow.verLabel.setText(__version__)
        
        self.addSubInterface(self.searchWindow, FluentIcon.SEARCH, "搜索音乐")
        self.addSubInterface(self.importWindow, FluentIcon.LIBRARY, "导入歌单")
        self.addSubInterface(self.taskWindow, FluentIcon.TAG, "下载任务")
        self.addSubInterface(self.settingWindow, FluentIcon.SETTING, "设置", NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.aboutWindow, FluentIcon.INFO, "关于", NavigationItemPosition.BOTTOM)
        
    def bind(self):
        self.aboutWindow.updateBtn.clicked.connect(self.check_update)
        self.searchWindow.searchLineEdit.searchSignal.connect(self.search)
        self.searchWindow.sourceBox.currentTextChanged.connect(self.setSource)
        self.importWindow.sourceBox.currentTextChanged.connect(self.setImportSource)
        self.searchWindow.musicTable.setMusicFunc(self.download_music)
        self.searchWindow.musicTable.setLyricFunc(self.download_lyric)
        self.settingWindow.opacitySlider.valueChanged.connect(self.setOpacity)
        self.settingWindow.bgBtn.clicked.connect(self.setBg)
        self.settingWindow.resetBtn.clicked.connect(self.resetStyle)
        self.settingWindow.themeBox.currentTextChanged.connect(lambda: self.resetTheme(self.settingWindow.themeBox.currentText()))
        self.settingWindow.openMusicPathBtn.clicked.connect(lambda: os.startfile(self.configs["music_path"]))
        self.settingWindow.openLyricPathBtn.clicked.connect(lambda: os.startfile(self.configs["lyric_path"]))
        self.settingWindow.threadNumEdit.textChanged.connect(self.setThreadNum)
        self.settingWindow.selfUaEdit.textChanged.connect(self.setUa)
        self.settingWindow.randomUaBtn.checkedChanged.connect(self.setUaState)
        self.settingWindow.downloadTipBtn.checkedChanged.connect(self.setDownloadTip)
        self.settingWindow.colorBtn.colorChanged.connect(self.resetThemeColor)
        self.settingWindow.musicPathBtn.clicked.connect(self.setMusicPath)
        self.settingWindow.lyricPathBtn.clicked.connect(self.setLyricPath)
        self.settingWindow.checkNetworkBtn.checkedChanged.connect(self.setCheckNetworkState)
        self.importWindow.importLineEdit.searchSignal.connect(self.import_music)
        self.importWindow.musicTable.setMusicFunc(self.download_music)
        
    def resetTheme(self, theme):
        if theme == "明亮":
            setTheme(Theme.LIGHT)
        elif theme == "暗黑":
            setTheme(Theme.DARK)
        else:
            setTheme(Theme.AUTO)
        self.configs["theme"] = theme
        
    def resetThemeColor(self, color: QColor):
        setThemeColor(color)
        self.configs["theme_color"] = color.name()
        
    def setBg(self):
        image = QFileDialog.getOpenFileName(self, "选择图片", ".", "选择图片(*.jpg *.jpeg *.png *.JPG *.JPEG *.PNG)")[0]
        if image == "":
            Dialog("选择图片", "您没有选择任何图片！", self).show()
        else:
            self.configs["img_file"] = image
            self.settingWindow.bgViewLabel.setPixmap(QPixmap(image).scaled(160, 90))
            self.searchWindow.bgLabel.setPixmap(QPixmap(image).scaled(991, 585))
            self.importWindow.bgLabel.setPixmap(QPixmap(image).scaled(991, 585))
            self.taskWindow.bgLabel.setPixmap(QPixmap(image).scaled(991, 585))
            self.settingWindow.bgLabel.setPixmap(QPixmap(image).scaled(991, 585))
            self.aboutWindow.bgLabel.setPixmap(QPixmap(image).scaled(991, 585))
            
    def resetStyle(self):
        self.configs["theme"] = "明亮"
        self.configs["v"] = 0.9
        self.configs["img_file"] = None
        self.configs["theme_color"] = "#009faa"

        self.resetTheme("明亮")
        setThemeColor(QColor("#009faa"))
        self.settingWindow.bgViewLabel.clear()
        self.searchWindow.bgLabel.clear()
        self.importWindow.bgLabel.clear()
        self.taskWindow.bgLabel.clear()
        self.settingWindow.bgLabel.clear()
        self.aboutWindow.bgLabel.clear()
        self.setOpacity(9)

        self.settingWindow.themeBox.setCurrentText(self.configs["theme"])
        self.settingWindow.opacitySlider.setValue(self.configs["v"] * 10)
            
    def setSource(self):
        self.source = self.searchWindow.sourceBox.currentText()
        
    def setImportSource(self):
        self.import_source = self.importWindow.sourceBox.currentText()
        
    def setMusicPath(self):
        path = QFileDialog.getExistingDirectory(self, "选择文件夹", ".")
        if path != "":
            self.configs["music_path"] = path
            self.settingWindow.musicPathEdit.setText(path)
    
    def setLyricPath(self):
        path = QFileDialog.getExistingDirectory(self, "选择文件夹", ".")
        if path != "":
            self.configs["lyric_path"] = path
            self.settingWindow.lyricPathEdit.setText(path)
            
    def setThreadNum(self, num):
        try:
            num = int(num)
        except ValueError:
            pass
        else:
            self.configs["thread_num"] = num
        finally:
            self.settingWindow.threadNumEdit.setText(str(self.configs["thread_num"]))
            
    def setUa(self, ua):
        if ua == "":
            self.settingWindow.randomUaBtn.setChecked(True)
            self.configs["ua"] = "random"
        else:
            self.configs["ua"] = ua
        
    def setUaState(self, state):
        if state:
            self.configs["ua"] == "random"
            self.settingWindow.selfUaEdit.clear()
            self.settingWindow.selfUaEdit.setEnabled(False)
        else:
            self.settingWindow.selfUaEdit.setEnabled(True)
            
    def setDownloadTip(self, state):
        if state:
            self.configs["downloadTip"] = True
        else:
            self.configs["downloadTip"] = False
            
    def setCheckNetworkState(self, state):
        if state:
            self.configs["checkNetwork"] = True
        else:
            self.configs["checkNetwork"] = False
        
    def setOpacity(self, level):
        self.configs["v"] = level / 10
        self.setWindowOpacity(self.configs["v"])
        
    def search(self, name):
        if self.source == "":
            Dialog("提示", "未选择音源", self).show()
            return
        elif name == "":
            Dialog("提示", "未输入内容", self).show()
            return
        
        self.searchTip = StateToolTip("搜索音乐", "正在搜索音乐，请稍后......", self)
        self.searchTip.move(750, 500)
        self.searchTip.show()
        
        self.searcher = Downloader(self.configs)
        self.searcher.music_name = name
        self.searcher.source = self.source
        self.search_thread = QThread()
        self.searcher.moveToThread(self.search_thread)
        self.search_thread.started.connect(self.searcher.search_music)
        self.searcher.task_done.connect(self.search_finished)
        self.tasks.update(
            {self.searcher: self.search_thread}
        )
        self.search_thread.start()
        
    def search_finished(self, res):
        choice_list, self.searcher.songids = res
        self.search_thread.quit()
        self.search_thread.wait()
        self.tasks.pop(self.searcher)
        
        self.searchWindow.musicTable.setColumnCount(2) 
        self.searchWindow.musicTable.setColumnWidth(0, 465)
        self.searchWindow.musicTable.setColumnWidth(1, 465)
        self.searchWindow.musicTable.setHorizontalHeaderLabels(["歌名", "作者"])
        self.searchWindow.musicTable.clearContents()
        self.searchWindow.musicTable.setRowCount(len(choice_list))
        for i, song_info in enumerate(choice_list):
            for j in range(2):
                self.searchWindow.musicTable.setItem(i, j, QTableWidgetItem(song_info[j]))
                
        self.searchWindow.musicTable.setToolTip("右键项目以操作")
        self.searchTip.setState(True)
        self.searchTip.setContent("搜索完成！")
    
    def download_music(self, state, n, content):
        downloader = Downloader(self.configs)
        downloader.n = n
        if state == "search":
            downloader.source = self.source
            downloader.songids = self.searcher.songids
            downloader.music_name = self.searcher.music_name
        elif state == "import":
            downloader.source = self.import_source
            downloader.songids = self.importer.songids
        downloader.task_id = QListWidgetItem(content)
        
        downloadMusicThread = QThread()
        downloader.moveToThread(downloadMusicThread)
        downloadMusicThread.started.connect(downloader.download_music)
        downloader.task_done.connect(self.download_music_finished)
        self.tasks.update(
            {downloader: downloadMusicThread}
        )
        self.taskWindow.add_task(downloader.task_id)
        downloadMusicThread.start()
        
    def download_music_finished(self, res):
        info, downloader = res
        if not info[0]:
            Dialog("下载失败", f"'{downloader.task_id.text()}'下载失败：\n{info[1]}").show()
        else:
            if self.configs["downloadTip"]:
                Dialog("下载成功", f"'{downloader.task_id.text()}'下载成功").show()
                
        self.taskWindow.remove_task(downloader.task_id)
        self.tasks[downloader].quit()
        self.tasks[downloader].wait()
        self.tasks.pop(downloader)
        
    def download_lyric(self, state, n, content):
        downloader = Downloader(self.configs)
        downloader.n = n
        if state == "search":
            downloader.source = self.source
            downloader.songids = self.searcher.songids
            downloader.music_name = self.searcher.music_name
        elif state == "import":
            downloader.source = self.import_source
            downloader.songids = self.importer.songids
        downloader.task_id = QListWidgetItem(content)
        
        downloadMusicThread = QThread()
        downloader.moveToThread(downloadMusicThread)
        downloadMusicThread.started.connect(downloader.download_lyric)
        downloader.task_done.connect(self.download_lyric_finished)
        self.tasks.update(
            {downloader: downloadMusicThread}
        )
        self.taskWindow.add_task(downloader.task_id)
        downloadMusicThread.start()
        
    def download_lyric_finished(self, res):
        info, downloader = res
        if not info[0]:
            Dialog("下载失败", f"'{downloader.task_id.text()}'下载失败：\n{info[1]}").show()
        else:
            if self.configs["downloadTip"]:
                Dialog("下载成功", f"'{downloader.task_id.text()}'下载成功").show()
                
        self.taskWindow.remove_task(downloader.task_id)
        self.tasks[downloader].quit()
        self.tasks[downloader].wait()
        self.tasks.pop(downloader)
        
    def import_music(self, info):
        if self.import_source == "":
            Dialog("提示", "未选择音源", self).show()
            return
        elif info == "":
            Dialog("提示", "未输入内容", self).show()
            return
        
        self.importTip = StateToolTip("导入歌单", "正在导入歌单，请稍后......", self)
        self.importTip.move(750, 500)
        self.importTip.show()

        self.importer = Downloader(self.configs)
        self.importer.info = info
        self.importer.source = self.import_source
        self.import_thread = QThread()
        self.importer.moveToThread(self.import_thread)
        self.import_thread.started.connect(self.importer.import_music)
        self.importer.task_done.connect(self.import_finished)
        self.tasks.update(
            {self.importer: self.import_thread}
        )
        self.import_thread.start()
        
    def import_finished(self, res):
        if res:
            self.import_thread.quit()
            self.import_thread.wait()
            self.tasks.pop(self.importer)
            
            data, tags, choice_list, self.importer.songids = res
            
            self.importWindow.nameLabel.setText(data["dissname"])
            self.importWindow.createrLabel.setText(data["nickname"])
            self.importWindow.contentLabel.setText(data["desc"])
            self.importWindow.numLabel.setText(str(data["total_song_num"]))
            self.importWindow.peopleLabel.setText(str((data["visitnum"])))
            self.importWindow.tagLabel.setText(tags)
            
            self.importWindow.musicTable.setColumnCount(3)
            self.importWindow.musicTable.setColumnWidth(0, 307)
            self.importWindow.musicTable.setColumnWidth(1, 307)
            self.importWindow.musicTable.setColumnWidth(2, 307)
            self.importWindow.musicTable.setHorizontalHeaderLabels(["歌名", "作者", "发布时间"])
            self.importWindow.musicTable.clearContents()
            self.importWindow.musicTable.setRowCount(len(choice_list))
            for i, song_info in enumerate(choice_list):
                for j in range(3):
                    self.importWindow.musicTable.setItem(i, j, QTableWidgetItem(song_info[j]))
            
            self.searchWindow.musicTable.setToolTip("右键项目以操作")
            self.importTip.setState(True)
            self.importTip.setContent("导入完成！")
        else:
            self.importTip.setState(True)
            self.importTip.setContent("导入失败！")
        
    def check_update(self):
        self.aboutWindow.updateBtn.setEnabled(False)
        self.checkUpdateTip = StateToolTip("检查更新", "正在检查更新，请稍后......", self)
        self.checkUpdateTip.move(750, 500)
        self.checkUpdateTip.show()
        self.updater = Downloader(self.configs)
        self.checkUpdateThread = QThread()
        self.updater.moveToThread(self.checkUpdateThread)
        self.checkUpdateThread.started.connect(self.updater.checkUpdate)
        self.updater.task_done.connect(self.check_update_finished)
        self.tasks.update(
            {self.updater: self.checkUpdateThread}
        )
        self.checkUpdateThread.start()
    
    def check_update_finished(self, res):
        self.tasks.pop(self.updater)
        self.checkUpdateThread.quit()
        self.checkUpdateThread.wait()
        version, info = res
        self.aboutWindow.updateText.setMarkdown(info)

        if version == __version__:
            self.checkUpdateTip.setState(True)
            self.checkUpdateTip.setContent(f"当前已经是最新版本：{version}")
        else:
            self.checkUpdateTip.setState(True)
            self.checkUpdateTip.setContent(f"有可用的更新：{version}")
            res = Dialog("更新", "有新版本可用，是否下载文件？", self)
            if res.exec():
                self.updateTip = StateToolTip("更新", "正在下载中，请稍后......", self)
                self.updateTip.move(750, 500)
                self.updateTip.show()
                
                # 创建更新线程
                self.update_thread = QThread()
                self.updater.moveToThread(self.update_thread)
                self.update_thread.started.connect(self.updater.update)
                self.updater.task_done.connect(self.update_finished)
                self.tasks.update(
                    {self.updater: self.update_thread}
                )
                self.update_thread.start()
        
        self.aboutWindow.updateBtn.setEnabled(True)
            
    def update_finished(self, res):
        self.tasks.pop(self.updater)
        self.update_thread.quit()
        self.update_thread.wait()
        self.updateTip.close()
        if res[0]:
            Dialog("下载更新", f"下载完成，文件在{res[1]}", self)
        else:
            Dialog("下载更新", "下载失败！", self)
    
    def closeEvent(self, event):
        if self.tasks:
            res = Dialog("退出", "当前还有任务正在进行，确定要退出吗？", self)
        else:
            res = Dialog("退出", "确定要退出吗？", self)

        if res.exec():
            with open("source/config.json", "w") as f:
                dump(self.configs, f)
            event.accept()
        else:
            event.ignore()
    

if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())