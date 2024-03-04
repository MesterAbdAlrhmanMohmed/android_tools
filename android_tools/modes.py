from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import subprocess
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("الإعدادات السريعة")
        self.وايفاي=qt.QCheckBox("Wi;Fi")
        self.وايفاي.toggled.connect(self.wifi)
        self.بيانات=qt.QCheckBox("بيانات الهاتف")
        self.بيانات.toggled.connect(self.data)
        self.لقطة=qt.QPushButton("أخذ لقطة شاشة")
        self.لقطة.setDefault(True)
        self.لقطة.clicked.connect(self.take_screenshot)
        l=qt.QVBoxLayout(self)                                    
        l.addWidget(self.وايفاي)
        l.addWidget(self.بيانات)
        l.addWidget(self.لقطة)
    def take_screenshot(self):
        result = subprocess.run("cd data/platform-tools && adb shell screencap -p /sdcard/screenshot.png", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            qt.QMessageBox.information(self, "نجاح", "تم أخذ لقطة للشاشة بنجاح")
        else:
            qt.QMessageBox.warning(self, "تنبيه", "فشل في أخذ لقطة للشاشة")    
    def wifi(self):
        if self.وايفاي.isChecked():
            result = subprocess.run("cd data/platform-tools && adb shell svc wifi enable", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                qt.QMessageBox.information(self, "نجاح", "تم تشغيل Wi;Fi")
            else:
                qt.QMessageBox.warning(self, "تنبيه", "فشل في تشغيل Wi;Fi")
        else:
            result = subprocess.run("cd data/platform-tools && adb shell svc wifi disable", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                qt.QMessageBox.information(self, "نجاح", "تم إيقاف Wi;Fi")
            else:
                qt.QMessageBox.warning(self, "تنبيه", "فشل في إيقاف Wi;Fi")    
    def data(self):
        if self.بيانات.isChecked():
            command = "cd data/platform-tools && adb shell svc data enable"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                qt.QMessageBox.information(self, "نجاح", "تم تفعيل بيانات الهاتف بنجاح")
            else:
                qt.QMessageBox.warning(self, "تحذير", "فشل في تفعيل بيانات الهاتف")
        else:
            command = "cd data/platform-tools && adb shell svc data disable"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                qt.QMessageBox.information(self, "نجاح", "تم إيقاف بيانات الهاتف بنجاح")
            else:
                qt.QMessageBox.warning(self, "تحذير", "فشل في إيقاف بيانات الهاتف")