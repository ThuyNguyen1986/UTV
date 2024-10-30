from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtCore import QTimer
from Main import Ui_MainWindow as MainUi_MainWindow 

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 838, 541))
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        
        # Set background image
        self.background_label = QtWidgets.QLabel(self.groupBox)
        self.background_label.setGeometry(0, 0, 838, 541)
        self.background_label.setPixmap(QPixmap(r"C:\Users\Win10\Desktop\Data_UTV\Code\background.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.lower()
        
        # Apply blur effect
        blur_effect = QtWidgets.QGraphicsBlurEffect()
        blur_effect.setBlurRadius(5)
        self.background_label.setGraphicsEffect(blur_effect)
        
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(140, 60, 631, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(230, 200, 271, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.username_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.username_input.setGeometry(QtCore.QRect(60, 50, 201, 31))
        self.username_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.password_input.setGeometry(QtCore.QRect(60, 110, 201, 31))
        self.password_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_input.setObjectName("password_input")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(330, 350, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(530, 210, 151, 141))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(r"C:\Users\Win10\Desktop\Data_UTV\Code\icon\khoa.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.check_login)

        # Add animation for the label
        self.animation = QPropertyAnimation(self.label, b"geometry")
        self.animation.setDuration(2000)
        self.animation.setStartValue(QRect(-self.label.width(), self.label.y(), self.label.width(), self.label.height()))
        self.animation.setEndValue(QRect(140, 60, 631, 41))
        self.animation.start()

        # Add blinking effect
        self.timer = QTimer()
        self.timer.timeout.connect(self.blink_label)
        self.timer.start(300)

    def blink_label(self):
        if self.label.isVisible():
            self.label.setVisible(False)
        else:
            self.label.setVisible(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "HỆ THỐNG CHẨN ĐOÁN VÀ GIẢI PHÁP BỆNH UNG THU VÚ"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Hệ thống đăng nhập"))
        self.label_2.setText(_translate("MainWindow", "Tài khoản:"))
        self.label_3.setText(_translate("MainWindow", "Mật khẩu:"))
        self.pushButton.setText(_translate("MainWindow", "Đăng nhập"))

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "Admin" and password == "123456":
            self.show_main_menu()
        else:
            QMessageBox.warning(None, 'Error', 'Sai tài khoản hoặc mật khẩu, vui lòng thử lại')
            self.username_input.clear()
            self.password_input.clear()

    def show_main_menu(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = MainUi_MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        QtWidgets.QApplication.instance().activeWindow().close()  #Close Window

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
