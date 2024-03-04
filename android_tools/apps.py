from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import subprocess
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.populate_apps()        
        self.ADB_PATH = "data/platform-tools/"
        self.إظهار=qt.QLabel("قائمة التطبيقات")
        self.comboBox = qt.QComboBox()
        self.comboBox.setAccessibleName("قائمة التطبيقات")
        self.فتح = qt.QPushButton("فتح التطبيق")
        self.فتح.clicked.connect(self.__OSA)
        self.فتح.setDefault(True)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.إظهار)
        layout.addWidget(self.comboBox)
        layout.addWidget(self.فتح)
    def populate_apps(self):
        adb_command = f"{self.ADB_PATH}adb shell pm list packages -3"
        process = subprocess.Popen(adb_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = process.communicate()
        packages = []
        if process.returncode == 0:
            packages = output.decode('utf-8').splitlines()
        for package in packages:
            package_name = package.split(":")[-1].strip()
            self.comboBox.addItem(package_name)
    def __OSA(self):
        selected_package = self.comboBox.currentText()
        adb_command = f"{self.ADB_PATH}/adb shell monkey -p {selected_package} -c android.intent.category.LAUNCHER 1"
        subprocess.run(adb_command, shell=True)    