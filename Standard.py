from PyQt5 import QtCore, QtGui, QtWidgets
from ultralytics import YOLO
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import cv2
import numpy as np
import os

class Ui_StandardWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 838, 541))
        self.groupBox.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, 20, 631, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 70, 611, 431))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(153, 204, 204);")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(40, 80, 241, 201))
        self.label_5.setStyleSheet("background-color: rgb(119, 119, 119);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(320, 80, 241, 201))
        self.label_6.setStyleSheet("background-color: rgb(119, 119, 119);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(40, 60, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(320, 60, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(380, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(102, 153, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.detect_disease)

        self.pushButton_load_image = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_load_image.setGeometry(QtCore.QRect(100, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_load_image.setFont(font)
        self.pushButton_load_image.setStyleSheet("background-color: rgb(102, 153, 0);")
        self.pushButton_load_image.setObjectName("pushButton_load_image")
        self.pushButton_load_image.setText("Đưa ảnh X-quang")
        self.pushButton_load_image.clicked.connect(self.load_xray_image)

        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(36, 362, 350, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 70, 181, 431))
        self.groupBox_3.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(100, 30, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 70, 60))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(r"C:\Users\Win10\Desktop\Data_UTV\Code\icon\thong_tin_ND.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 130, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 170, 141, 23))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 210, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_10.setGeometry(QtCore.QRect(50, 400, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 90, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 854, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.model = YOLO(r'C:\Users\Win10\Desktop\Data_UTV\Data_UTV\YOLOv8\runs\detect\train3\weights\best.pt')
        self.image_path = None

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "HỆ THỐNG CHẨN ĐOÁN VÀ GIẢI PHÁP BỆNH UNG THU VÚ"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Chẩn đoán bệnh"))
        self.label_7.setText(_translate("MainWindow", "Đưa ảnh vào nhận diện:"))
        self.label_8.setText(_translate("MainWindow", "Hình ảnh phát hiện:"))
        self.pushButton.setText(_translate("MainWindow", "Chẩn đoán bệnh"))
        self.label_9.setText(_translate("MainWindow", "Kết quả trả về:"))
        self.label_4.setText(_translate("MainWindow", "Menu"))
        self.pushButton_7.setText(_translate("MainWindow", "Chẩn đoán bệnh"))
        self.pushButton_8.setText(_translate("MainWindow", "Hồ sơ bệnh án"))
        self.pushButton_9.setText(_translate("MainWindow", "Đề xuất giải pháp"))
        self.pushButton_10.setText(_translate("MainWindow", "Đăng xuất"))
        self.pushButton_11.setText(_translate("MainWindow", "Thông tin bệnh nhân"))

    def load_xray_image(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Load X-ray Image", "", "Image Files (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if file_path:
            self.image_path = file_path
            pixmap = QtGui.QPixmap(file_path)
            self.label_5.setPixmap(pixmap.scaled(self.label_5.size(), QtCore.Qt.KeepAspectRatio))

    def detect_disease(self):
        if self.image_path:
            results = self.model.predict(source=self.image_path)
            img_with_boxes = results[0].plot()
            img_with_boxes = cv2.cvtColor(img_with_boxes, cv2.COLOR_BGR2RGB)
            h, w, ch = img_with_boxes.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QtGui.QImage(img_with_boxes.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(convert_to_Qt_format)
            self.label_6.setPixmap(pixmap.scaled(self.label_6.size(), QtCore.Qt.KeepAspectRatio))

            # Process results and determine the class label
            highest_confidence = 0
            final_label = 'Indeterminate'
            class_labels = {0: 'benign', 1: 'malignant', 2: 'normal'}

            for box in results[0].boxes:
                detected_class = int(box.cls.item())
                confidence = box.conf.item()
                if confidence > highest_confidence:
                    highest_confidence = confidence
                    final_label = class_labels.get(detected_class, 'Indeterminate')

            if final_label == 'malignant' and highest_confidence < 0.6:
                final_label = 'suspicious_malignant'
            elif final_label == 'normal' and highest_confidence < 0.5:
                final_label = 'Indeterminate'
            elif final_label == 'benign' and highest_confidence < 0.5:
                final_label = 'Indeterminate'

            self.label_9.setText(f"Kết quả trả về: {final_label} (Confidence: {highest_confidence:.2f})")

            # Save image to a file
            image_save_path = os.path.join(r'C:\Users\Win10\Desktop\Data_UTV\img', f'result_{final_label}_{highest_confidence:.2f}.png')
            cv2.imwrite(image_save_path, cv2.cvtColor(img_with_boxes, cv2.COLOR_RGB2BGR))

            # Save result to the database
            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    database='patients_info',
                    user='root',
                    password='Weak'
                )

                if conn.is_connected():
                    cursor = conn.cursor()
                    query = '''
                    UPDATE patients_info.patients 
                    SET `condition` = %s, `image_path` = %s 
                    WHERE id = (
                        SELECT * FROM (
                            SELECT id FROM patients_info.patients 
                            ORDER BY id DESC LIMIT 1
                        ) AS temp
                    )
                    '''

                    cursor.execute(query, (final_label, image_save_path))
                    conn.commit()

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
    ui = Ui_StandardWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
