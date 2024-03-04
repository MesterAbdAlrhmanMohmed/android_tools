import subprocess
from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("إلغاء تثبيت التطبيقات")
        self.إظهار=qt.QLabel("قائمة التطبيقات")
        self.ba=qt.QComboBox()
        self.ba.setAccessibleName("إختيار التطبيق")
        self.com=qt.QPushButton("إلغاء التثبيت")
        self.com.setDefault(True)
        self.com.clicked.connect(self.com1)
        layout=qt.QVBoxLayout()
        layout.addWidget(self.إظهار)
        layout.addWidget(self.ba)
        layout.addWidget(self.com)
        self.setLayout(layout)
        self.get()
    def get(self):
        result = subprocess.run('cd data/platform-tools && adb shell pm list packages', shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            package_names = result.stdout.strip().split('\n')
            package_names = [pkg.split(':')[-1] for pkg in package_names]
            self.ba.addItems(package_names)
    def com1(self):
        result = subprocess.run("cd data/platform-tools && adb uninstall " + self.ba.currentText(), shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            qt.QMessageBox.information(self,"تم","تم إلغاء التثبيت بنجاح")
        else:
            qt.QMessageBox.warning(self,"تنبيه","فشلت عملية إلغاء التثبيت")