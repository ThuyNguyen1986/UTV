from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error
from datetime import datetime

class Ui_HealthRecordWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 838, 541))
        self.groupBox.setMouseTracking(False)
        self.groupBox.setTabletTracking(False)
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(120, 30, 631, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Tạo QScrollArea để chứa thông tin bệnh nhân
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(200, 130, 611, 381))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 611, 381))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 611, 381))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.groupBox_2.setTitle("Hồ sơ bệnh án")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")

        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(330, 20, 261, 251))
        self.groupBox_3.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(80, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 241, 201))
        self.label_3.setStyleSheet("background-color: rgb(119, 119, 119);")
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")


        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 20, 311, 251))
        self.groupBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(20, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(20, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(20, 140, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(20, 170, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setGeometry(QtCore.QRect(20, 200, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setGeometry(QtCore.QRect(20, 230, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        # Thêm các QLabel để hiển thị thông tin bệnh nhân
        self.patient_name = QtWidgets.QLineEdit(self.groupBox_5)
        self.patient_name.setGeometry(QtCore.QRect(170, 50, 131, 20))
        self.patient_name.setObjectName("patient_name")

        self.patient_dob = QtWidgets.QLineEdit(self.groupBox_5)
        self.patient_dob.setGeometry(QtCore.QRect(170, 80, 131, 20))
        self.patient_dob.setObjectName("patient_dob")

        self.patient_address = QtWidgets.QLineEdit(self.groupBox_5)
        self.patient_address.setGeometry(QtCore.QRect(170, 110, 131, 20))
        self.patient_address.setObjectName("patient_address")

        self.patient_phone = QtWidgets.QLineEdit(self.groupBox_5)
        self.patient_phone.setGeometry(QtCore.QRect(170, 140, 131, 20))
        self.patient_phone.setObjectName("patient_phone")

        self.patient_id = QtWidgets.QLineEdit(self.groupBox_5)
        self.patient_id.setGeometry(QtCore.QRect(170, 170, 131, 20))
        self.patient_id.setObjectName("patient_id")

        self.patient_condition = QtWidgets.QLineEdit(self.groupBox_5)
        self.patient_condition.setGeometry(QtCore.QRect(170, 200, 131, 20))
        self.patient_condition.setObjectName("patient_condition")

        self.patient_date = QtWidgets.QLineEdit(self.groupBox_5)
        self.patient_date.setGeometry(QtCore.QRect(170, 230, 131, 20))
        self.patient_date.setObjectName("patient_date")

        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 280, 581, 101))
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton.setGeometry(QtCore.QRect(240, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 80, 181, 431))
        self.groupBox_4.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(100, 30, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 70, 60))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(r"C:\Users\Win10\Desktop\Data_UTV\Code\icon\thong_tin_ND.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 130, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_12.setGeometry(QtCore.QRect(20, 170, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 210, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_14.setGeometry(QtCore.QRect(50, 400, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_15.setGeometry(QtCore.QRect(20, 90, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_7.setGeometry(QtCore.QRect(330, 80, 261, 31))
        self.groupBox_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")

        # Thêm nhãn "Nhập CMND/CCCD:"
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(200, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(330, 80, 261, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        # self.lineEdit.setValidator(QtGui.QIntValidator())  # Chỉ cho phép nhập số
        # self.lineEdit.setMaxLength(12)  # Cho phép nhập tối đa 12 số

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 80, 31, 31))
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\Win10\Desktop\Data_UTV\Code\icon\find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Kết nối nút tìm kiếm với hàm tìm kiếm
        self.pushButton_4.clicked.connect(self.search_patient)
        # Kết nối nút sửa với hàm sửa
        self.pushButton.clicked.connect(self.update_patient)
        # Kết nối nút thêm với hàm thêm
        self.pushButton_2.clicked.connect(self.add_patient)
        # Kết nối nút xóa với hàm xóa
        self.pushButton_3.clicked.connect(self.delete_patient)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "HỆ THỐNG CHẨN ĐOÁN VÀ GIẢI PHÁP BỆNH UNG THU VÚ"))
        self.label_2.setText(_translate("MainWindow", "Ảnh chẩn đoán:"))
        self.label_4.setText(_translate("MainWindow", "Thông tin bệnh nhân"))
        self.label_7.setText(_translate("MainWindow", "Họ và tên:"))
        self.label_8.setText(_translate("MainWindow", "Ngày sinh:"))
        self.label_9.setText(_translate("MainWindow", "Địa chỉ:"))
        self.label_10.setText(_translate("MainWindow", "Số điện thoại:"))
        self.label_11.setText(_translate("MainWindow", "Số CMND/CCCD:"))
        self.label_12.setText(_translate("MainWindow", "Tình trạng bệnh:"))
        self.label_13.setText(_translate("MainWindow", "Ngày khám bệnh:"))
        self.label_17.setText(_translate("MainWindow", "Nhập CMND/CCCD:"))  # Thêm dòng này

        self.groupBox_6.setTitle(_translate("MainWindow", "Chức năng"))
        self.pushButton.setText(_translate("MainWindow", "Sửa "))
        self.pushButton_2.setText(_translate("MainWindow", "Thêm"))
        self.pushButton_3.setText(_translate("MainWindow", "Xóa"))
        self.label_14.setText(_translate("MainWindow", "Menu"))
        self.pushButton_11.setText(_translate("MainWindow", "Chẩn đoán bệnh"))
        self.pushButton_12.setText(_translate("MainWindow", "Hồ sơ bệnh án"))
        self.pushButton_13.setText(_translate("MainWindow", "Đề xuất giải pháp"))
        self.pushButton_14.setText(_translate("MainWindow", "Đăng xuất"))
        self.pushButton_15.setText(_translate("MainWindow", "Thông tin bệnh nhân"))

    def search_patient(self):
        input_id = self.lineEdit.text()

        if not input_id.isdigit():
            QtWidgets.QMessageBox.warning(None, 'Error', 'Vui lòng nhập CMND/CCCD')
            return

        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='patients_info',
                user='root',
                password='Weak'
            )

            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute('''SELECT name, dob, address, phone, id_number, `condition`, `date`, image_path 
                                  FROM patients WHERE id_number = %s''', (input_id,))
                result = cursor.fetchone()

                if result:
                    self.patient_name.setText(result[0])
                    self.patient_dob.setText(result[1].strftime('%Y-%m-%d'))
                    self.patient_address.setText(result[2])
                    self.patient_phone.setText(result[3])
                    self.patient_id.setText(result[4])
                    self.patient_condition.setText(result[5] if result[5] else "")
                    self.patient_date.setText(result[6].strftime('%Y-%m-%d %H:%M:%S'))

                    # Hiển thị hình ảnh
                    if result[7]:
                        image_path = result[7]
                        pixmap = QtGui.QPixmap(image_path)
                        self.label_3.setPixmap(pixmap.scaled(self.label_3.size(), QtCore.Qt.KeepAspectRatio))
                else:
                    QtWidgets.QMessageBox.warning(None, 'Error', 'Không tìm thấy thông tin bệnh nhân, vui lòng nhập lại')

        except Error as e:
            QtWidgets.QMessageBox.critical(None, 'Error', f'Error connecting to MySQL: {e}')

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


    def update_patient(self):
        name = self.patient_name.text()
        dob = self.patient_dob.text()
        address = self.patient_address.text()
        phone = self.patient_phone.text()
        id_number = self.patient_id.text()
        condition = self.patient_condition.text()
        date = self.patient_date.text()

        if not id_number.isdigit():
            QtWidgets.QMessageBox.warning(None, 'Error', 'Vui lòng nhập CMND/CCCD hợp lệ')
            return

        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='patients_info',
                user='root',
                password='Weak'  #Change yourpassword
            )

            if conn.is_connected():
                cursor = conn.cursor()
                query = '''UPDATE patients
                           SET name = %s, dob = %s, address = %s, phone = %s, `condition` = %s, `date` = %s
                           WHERE id_number = %s'''
                cursor.execute(query, (name, dob, address, phone, condition, date, id_number))
                conn.commit()
                QtWidgets.QMessageBox.information(None, 'Success', 'Thông tin bệnh nhân đã được cập nhật thành công!')

        except Error as e:
            QtWidgets.QMessageBox.critical(None, 'Error', f'Error connecting to MySQL: {e}')

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def add_patient(self):
        name = self.patient_name.text()
        dob = self.patient_dob.text()
        address = self.patient_address.text()
        phone = self.patient_phone.text()
        id_number = self.patient_id.text()
        condition = self.patient_condition.text()
        date = self.patient_date.text()

        if not id_number.isdigit():
            QtWidgets.QMessageBox.warning(None, 'Error', 'Vui lòng nhập CMND/CCCD hợp lệ')
            return

        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='patients_info',
                user='root',
                password='Weak'  #Change  yourpassword
            )

            if conn.is_connected():
                cursor = conn.cursor()
                query = '''INSERT INTO patients (name, dob, address, phone, id_number, `condition`, `date`)
                           VALUES (%s, %s, %s, %s, %s, %s, %s)'''
                cursor.execute(query, (name, dob, address, phone, id_number, condition, date))
                conn.commit()
                QtWidgets.QMessageBox.information(None, 'Success', 'Bệnh nhân đã được thêm thành công!')

        except Error as e:
            QtWidgets.QMessageBox.critical(None, 'Error', f'Error connecting to MySQL: {e}')

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def delete_patient(self):
        id_number = self.patient_id.text()

        if not id_number.isdigit():
            QtWidgets.QMessageBox.warning(None, 'Error', 'Vui lòng nhập CMND/CCCD hợp lệ')
            return

        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='patients_info',
                user='root',
                password='Weak'  # Change yourpassword
            )

            if conn.is_connected():
                cursor = conn.cursor()

                # Delete 
                delete_query = '''DELETE FROM patients WHERE id_number = %s'''
                cursor.execute(delete_query, (id_number,))
                conn.commit()
            
                # Reset ID
                cursor.execute('SET @num := 0;')
                cursor.execute('UPDATE patients SET id = @num := (@num+1);')
                cursor.execute('ALTER TABLE patients AUTO_INCREMENT = 1;')
                conn.commit()
            
                QtWidgets.QMessageBox.information(None, 'Success', 'Bệnh nhân đã được xóa thành công!')
            
                # Clear displayed patient information
                self.patient_name.setText("")
                self.patient_dob.setText("")
                self.patient_address.setText("")
                self.patient_phone.setText("")
                self.patient_id.setText("")
                self.patient_condition.setText("")
                self.patient_date.setText("")

        except Error as e:
            QtWidgets.QMessageBox.critical(None, 'Error', f'Error connecting to MySQL: {e}')

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_HealthRecordWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
