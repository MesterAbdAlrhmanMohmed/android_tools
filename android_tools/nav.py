from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import subprocess
import apps
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)        
        self.ADB_PATH = "data/platform-tools/"
        self.setWindowTitle("التنقل في الهاتف")
        self.حول=qt.QPushButton("حول التنقل في الهاتف")
        self.حول.setDefault(True)
        self.حول.clicked.connect(self.ab)
        self.أعلا=qt.QPushButton("الأعلا")        
        self.أعلا.clicked.connect(self.navigate_up)
        self.أعلا.setShortcut("up")
        self.أسفل=qt.QPushButton("الأسفل")
        self.أسفل.setShortcut("down")
        self.أسفل.clicked.connect(self.navigate_down)
        self.يسار=qt.QPushButton("اليسار")
        self.يسار.clicked.connect(self.navigate_left)
        self.يسار.setShortcut("left")
        self.يمين=qt.QPushButton("اليمين")
        self.يمين.clicked.connect(self.navigate_right)
        self.يمين.setShortcut("right")
        self.السحب_أعلى=qt.QPushButton("السحب الى أعلا")
        self.السحب_أعلى.clicked.connect(self.swipe_up)
        self.السحب_أعلى.setShortcut("ctrl+up")
        self.السحب_أسفل=qt.QPushButton("السحب الى أسفل")        
        self.السحب_أسفل.clicked.connect(self.swipe_down)
        self.السحب_أسفل.setShortcut("ctrl+down")
        self.السحب_يسار=qt.QPushButton("السحب الى اليسار")
        self.السحب_يسار.clicked.connect(self.swipe_left)
        self.السحب_يسار.setShortcut("ctrl+left")
        self.السحب_يمين=qt.QPushButton("السحب الى اليمين")
        self.السحب_يمين.clicked.connect(self.swipe_right)
        self.السحب_يمين.setShortcut("ctrl+right")
        self.الدخول=qt.QPushButton("الدخول الى العنصر المركز عليه")
        self.الدخول.setDefault(True)    
        self.الدخول.clicked.connect(self.enter_selected_item)
        self.الدخول.setShortcut("return")
        self.الحديثة=qt.QPushButton("التطبيقات الحديثة")        
        self.الحديثة.clicked.connect(self.press_recent_apps)
        self.الحديثة.setShortcut("1")
        self.الرئسية=qt.QPushButton("الشاشة الرئسية")
        self.الرئسية.clicked.connect(self.press_home)
        self.الرئسية.setShortcut("2")
        self.الرجوع=qt.QPushButton("الرجوع")
        self.الرجوع.clicked.connect(self.press_back)
        self.الرجوع.setShortcut("3")        
        self.فتح=qt.QPushButton("فتح التطبيقات")        
        self.فتح.clicked.connect(self.appsO)
        self.فتح.setShortcut("4")
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.حول)        
        l.addWidget(self.أعلا)
        l.addWidget(self.أسفل)
        l.addWidget(self.يسار)
        l.addWidget(self.يمين)
        l.addWidget(self.السحب_أسفل)
        l.addWidget(self.السحب_أعلى)
        l.addWidget(self.السحب_يسار)
        l.addWidget(self.السحب_يمين)
        l.addWidget(self.الدخول)
        l.addWidget(self.الحديثة)
        l.addWidget(self.الرجوع)
        l.addWidget(self.الرئسية)    
        l.addWidget(self.فتح)
    def appsO(self):
        apps.dialog(self).exec()
    def ab(self):
        qt.QMessageBox.information(self,"معلومات هامة","للتنقل في الهاتف للأعلا أو الأسفل أو اليمين أو اليسار, قم بالضغط على السهم المراد, وللسحب الى نفس الإتجاهات قم بالضغط على CTRL زائد السهم المراد وللدخول إضغط enter, ولشريط التنقل إضغط 1 للتطبيقات الأخيرة و2 للشاشة الرئسية و3 للرجوع, ولإختيار تطبيق لفتحه قم بالضغت على الرقم 4")
    def run_adb_command(self, command):                
        try:
            subprocess.Popen([self.ADB_PATH + "adb"] + command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
        except subprocess.CalledProcessError as e:        
            qt.QMessageBox.warning(self,"خطأ","حدث خطأ أثناء تشغيل الأمر")
    def navigate_up(self):
        self.run_adb_command(["shell", "input", "keyevent", "KEYCODE_DPAD_UP"])
    def navigate_down(self):
        self.run_adb_command(["shell", "input", "keyevent", "KEYCODE_DPAD_DOWN"])
    def navigate_right(self):
        self.run_adb_command(["shell", "input", "keyevent", "KEYCODE_DPAD_RIGHT"])
    def navigate_left(self):
        self.run_adb_command(["shell", "input", "keyevent", "KEYCODE_DPAD_LEFT"])
    def swipe_up(self):
        self.run_adb_command(["shell", "input", "swipe", "500", "1500", "500", "500"])
    def swipe_down(self):
        self.run_adb_command(["shell", "input", "swipe", "500", "500", "500", "1500"])
    def swipe_right(self):
        self.run_adb_command(["shell", "input", "swipe", "700", "500", "100", "500"])
    def swipe_left(self):
        self.run_adb_command(["shell", "input", "swipe", "100", "500", "700", "500"])
    def enter_selected_item(self):
        self.run_adb_command(["shell", "input", "keyevent", "KEYCODE_ENTER"])
    def press_recent_apps(self):
        self.run_adb_command(["shell", "input", "keyevent", "KEYCODE_APP_SWITCH"])
    def press_back(self):
        self.run_adb_command(["shell", "input", "keyevent", "KEYCODE_BACK"])
    def press_home(self):
        self.run_adb_command(["shell", "input", "keyevent", "KEYCODE_HOME"])
