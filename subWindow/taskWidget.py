from PySide6.QtWidgets import QWidget

from UI.Ui_taskWidget import Ui_taskWindow


class TaskWindow(QWidget, Ui_taskWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def add_task(self, task):
        self.taskWidget.addItem(task)
        task_num = self.taskWidget.count()
        self.label.setText(f"下载任务：{task_num}")
        
    def remove_task(self, task):
        self.taskWidget.takeItem(self.taskWidget.row(task))
        task_num = self.taskWidget.count()
        if task_num == 0:
            task_num = "暂无"
        self.label.setText(f"下载任务：{task_num}")