import subprocess
from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("تثبيت التطبيقات")
        self.path=qt.QLineEdit()
        self.path.setAccessibleName("مسار التطبيق")
        self.path.setReadOnly(True)
        self.brows=qt.QPushButton("إختيار التطبيق")
        self.brows.setDefault(True)
        self.brows.clicked.connect(self.fbrows)
        self.com=qt.QPushButton("تثبيت التطبيق")
        self.com.setDefault(True)
        self.com.clicked.connect(self.oncom)
        layout=qt.QVBoxLayout()
        layout.addWidget(self.path)
        layout.addWidget(self.brows)
        layout.addWidget(self.com)
        self.setLayout(layout)
    def fbrows(self):
        file=qt.QFileDialog(self)
        file.setDefaultSuffix("apk")
        file.setAcceptMode(qt.QFileDialog.AcceptMode.AcceptOpen)
        file.setNameFilters(["apk files(*.apk)"])
        if file.exec() == qt.QFileDialog.DialogCode.Accepted:
            self.path.setText(file.selectedFiles()[0])
    def oncom(self):
        result = subprocess.run("cd data/platform-tools && adb install " + self.path.text(), shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            qt.QMessageBox.information(self,"تم","تمت عملية التثبيت بنجاح")
        else:
            qt.QMessageBox.warning(self,"تنبيه","فشلت عملية التثبيت")