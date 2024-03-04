from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import winsound
import winsound
import subprocess
import install
import uninstall
import modes
import nav
class main (qt.QMainWindow):    
    def __init__(self):
        super().__init__()                        
        self.setWindowTitle("برنامج أدوات الandroid")        
        qt2.QTimer.singleShot(100,self.play_sound)        
        self.MIN_BRIGHTNESS = 0
        self.MAX_BRIGHTNESS = 255        
        self.القائمة1=qt.QLabel("تثبيت وإلغاء تثبيت التطبيقات")        
        self.التثبيت_وإلغاء=qt.QComboBox()
        self.التثبيت_وإلغاء.addItems(["تثبيت التطبيقات","إلغاء تثبيت التطبيقات"])
        self.التثبيت_وإلغاء.setAccessibleName("تثبيت وإلغاء تثبيت التطبيقات")
        self.إختيار1=qt.QPushButton("إختيار")
        self.إختيار1.setDefault(True)        
        self.إختيار1.clicked.connect(self.ch1)
        self.القائمة2=qt.QLabel("المكالمات")
        self.المكالمات=qt.QComboBox()
        self.المكالمات.setAccessibleName("المكالمات")
        self.المكالمات.addItems(["إجراء مكالمة","الرد على المكالمة","رفض المكالمة","إنهاء المكالمة"])
        self.إختيار2=qt.QPushButton("إختيار")
        self.إختيار2.setDefault(True)
        self.إختيار2.clicked.connect(self.ch2)
        self.القائمة3=qt.QLabel("خيارات الجهاز")
        self.الجهاز=qt.QComboBox()
        self.الجهاز.setAccessibleName("خيارات الجهاز")
        self.الجهاز.addItems(["إيقاف تشغيل الجهاز","إعادة تشغيل الجهاز","محو بيانات الجهاز"])
        self.إختيار3=qt.QPushButton("إختيار")
        self.إختيار3.setDefault(True)
        self.إختيار3.clicked.connect(self.ch3)        
        self.السطوع=qt.QLabel("مستوى السطوع")
        self.مستوا_السطوع=qt.QSlider()
        self.مستوا_السطوع.setRange(0,100)
        self.مستوا_السطوع.setAccessibleName("التحكم في مستوى السطوع")
        self.مستوا_السطوع.valueChanged.connect(self.set_brightness)
        self.السريعة=qt.QPushButton("الإعدادات السريعة")
        self.السريعة.setDefault(True)
        self.السريعة.clicked.connect(self.cw)        
        self.حول=qt.QPushButton("حول البرنامج")
        self.حول.setDefault(True)
        self.حول.clicked.connect(self.ab)        
        self.التنقل=qt.QPushButton("التنقل في الهاتف")
        self.التنقل.setDefault(True)
        self.التنقل.clicked.connect(self.nav)
        l=qt.QVBoxLayout()        
        l.addWidget(self.القائمة1)
        l.addWidget(self.التثبيت_وإلغاء)
        l.addWidget(self.إختيار1)
        l.addWidget(self.القائمة2)
        l.addWidget(self.المكالمات)
        l.addWidget(self.إختيار2)
        l.addWidget(self.القائمة3)
        l.addWidget(self.الجهاز)
        l.addWidget(self.إختيار3)        
        l.addWidget(self.السطوع)
        l.addWidget(self.مستوا_السطوع)        
        l.addWidget(self.السريعة)
        l.addWidget(self.التنقل)
        l.addWidget(self.حول)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)            
    def nav(self):
        nav.dialog(self).exec()
    def ch1(self):
        القائمة=self.التثبيت_وإلغاء.currentIndex()
        if القائمة ==0:
            install.dialog(self).exec()
        elif القائمة ==1:
            uninstall.dialog(self).exec()
    def ch2(self):
        القائمة=self.المكالمات.currentIndex()
        ok=False
        if القائمة ==0:
            text,ok=qt.QInputDialog.getText(self,"إجراء مكالمة","أكتب رقم الهاتف هنا")
        if ok:
            result = subprocess.run("cd data/platform-tools && adb shell am start -a android.intent.action.CALL -d tel:" + text, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                qt.QMessageBox.information(self,"تم","بدأت المكالمة")
            else:
                qt.QMessageBox.warning(self,"خطأ","فشلت عملية إجراء المكالمة")
        if القائمة ==1:                        
            command = "cd data/platform-tools && adb shell input keyevent 5"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                qt.QMessageBox.information(None, "نجاح", "تم الرد على المكالمة بنجاح")
            else:
                qt.QMessageBox.warning(None, "تحذير", "فشل في الرد على المكالمة")
        if القائمة ==2:            
            command = "cd data/platform-tools && adb shell input keyevent KEYCODE_ENDCALL"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                qt.QMessageBox.warning(self,"خطأ","فشل في رفد المكالمة")
        if القائمة ==3:            
            command = "cd data/platform-tools && adb shell input keyevent KEYCODE_ENDCALL"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                qt.QMessageBox.warning(self,"خطأ","فشل في إنهاء المكالمة")
    def ch3(self):
        القائمة=self.الجهاز.currentIndex()
        if القائمة==0:
            result = subprocess.run("cd data/platform-tools && adb shell reboot -p", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                qt.QMessageBox.information(self, "نجاح", "تم إيقاف تشغيل الجهاز بنجاح")
            else:
                qt.QMessageBox.warning(self, "تنبيه", "فشل في إيقاف تشغيل الجهاز")
        elif القائمة ==1:
            result = subprocess.run("cd data/platform-tools && adb shell reboot", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                qt.QMessageBox.information(self, "نجاح", "تم إعادة تشغيل الجهاز بنجاح")
            else:
                qt.QMessageBox.warning(self, "تنبيه", "فشل في إعادة تشغيل الجهاز")    
        elif القائمة ==2:
            confirmation = qt.QMessageBox.question(self, "تنبيه", "هل أنت متأكد أنك تريد محو بيانات الجهاز؟ ستخسر جميع بيانات الجهاز", 
            qt.QMessageBox.StandardButton.Yes | qt.QMessageBox.StandardButton.No)
            if confirmation == qt.QMessageBox.StandardButton.Yes:
                result = subprocess.run("cd data/platform-tools && adb shell recovery --wipe_data", shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    qt.QMessageBox.information(self, "نجاح", "تم محو بيانات الجهاز بنجاح")
                else:
                    qt.QMessageBox.warning(self, "تنبيه", "فشل في محو بيانات الجهاز")
    def cw(self):
        modes.dialog(self).exec()    
    def ab(self):
        qt.QMessageBox.information(self,"حول البرنامج","تم إنشاء هذا البرنامج لتشغيل بعض الوظائف على أجهزة الandroid, يرجى عدم حذف مجلد data الموجود بجانب البرنامج. معلومة هامة, إذا لم تعمل الوظائف يرجى تشغيل تصحيح أخطاء USP من خيارات المطور, يرجى العلم أن ليست جميع الوظائف تعمل على كل الأجهزة. (مطور البرنامج غير مسؤل عن إستخدام البرنامج في أي أفعال غير قانونية وغير أخلاقية), تحياتي, مطور البرنامج, (عبد الرحمن محمد)")
    def set_brightness(self, value):        
        brightness = int(self.MIN_BRIGHTNESS + (self.MAX_BRIGHTNESS - self.MIN_BRIGHTNESS) * value / 100)
        brightness_command = f"cd data/platform-tools && adb shell settings put system screen_brightness {brightness}"
        result = subprocess.run(brightness_command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            qt.QMessageBox.warning(self, "تنبيه", "فشل في تعديل سطوع الشاشة")        
    def play_sound(self):
        sound_file = "data/A.wav"
        winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()