from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SolutionWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 838, 541))
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
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 80, 181, 431))
        self.groupBox_4.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(100, 30, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 70, 60))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(r"C:\Users\Win10\Desktop\Data_UTV\Code\icon\thong_tin_ND.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 130, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 170, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 210, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_10.setGeometry(QtCore.QRect(50, 400, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 90, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 80, 621, 431))
        self.groupBox_2.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 50, 601, 170))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.groupBox_3)
        self.verticalScrollBar.setGeometry(QtCore.QRect(580, 9, 16, 158))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_1.setGeometry(QtCore.QRect(10, 20, 570, 140))
        self.textBrowser_1.setVerticalScrollBar(self.verticalScrollBar)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 240, 601, 170))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.groupBox_5)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(580, 9, 16, 158))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 20, 570, 140))
        self.textBrowser_2.setVerticalScrollBar(self.verticalScrollBar_2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(30, 10, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 10, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 10, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
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

        self.pushButton.clicked.connect(lambda: self.update_solution("benign"))
        self.pushButton_2.clicked.connect(lambda: self.update_solution("suspicious_malignant"))
        self.pushButton_3.clicked.connect(lambda: self.update_solution("malignant"))

        self.benign_info = {
            "Nguyên nhân và triệu chứng": (
                "Nguyên nhân:\n"
                "- Thay đổi hormone, đặc biệt liên quan đến chu kỳ kinh nguyệt.\n"
                "- Di truyền, chẳng hạn như gia đình có tiền sử mắc bệnh lành tính.\n"
                "- Sử dụng liệu pháp thay thế hormone.\n"
                "- Nhiễm trùng hoặc viêm trong mô vú.\n\n"
                "Triệu chứng:\n"
                "- Các khối u có thể sờ thấy, thường là mịn và có thể di chuyển.\n"
                "- Đau hoặc nhạy cảm ở vú.\n"
                "- Thay đổi kích thước hoặc hình dạng của vú.\n"
                "- Dịch tiết từ núm vú (không có máu).\n"
                "- Sưng hoặc đỏ cục bộ."
            ),
            "Đề xuất giải pháp": (
                "- Theo dõi và kiểm tra định kỳ với bác sĩ.\n"
                "- Chọc hút kim mảnh hoặc sinh thiết để xác nhận tính lành tính.\n"
                "- Dùng thuốc giảm đau và viêm như NSAID.\n\n"
                "- Thay đổi lối sống:\n"
                "  + Mặc áo ngực vừa vặn để giảm khó chịu.\n"
                "  + Duy trì chế độ ăn uống lành mạnh và tập thể dục đều đặn.\n"
                "  + Giảm lượng caffeine và thực phẩm nhiều chất béo.\n"
                "  + Quản lý căng thẳng thông qua các kỹ thuật thư giãn như yoga và thiền.\n\n"
                "- Can thiệp phẫu thuật (nếu cần thiết):\n"
                "  + Phẫu thuật cắt bỏ khối u lớn hoặc gây khó chịu.\n"
                "  + Dẫn lưu các u nang nếu chúng đau hoặc tái phát."
            )
        }

        self.suspicious_malignant_info = {
            "Nguyên nhân và triệu chứng": (
                "Nguyên nhân:\n"
                "- Đột biến gen, như BRCA1 và BRCA2.\n"
                "- Gia đình có tiền sử ung thư vú.\n"
                "- Tiếp xúc với bức xạ.\n"
                "- Các yếu tố hormone, như kinh nguyệt sớm hoặc mãn kinh muộn.\n"
                "- Các yếu tố lối sống, bao gồm béo phì và tiêu thụ rượu.\n\n"
                "Triệu chứng:\n"
                "- Khối u mới hoặc khối u trong vú, cứng, không đều và không di chuyển.\n"
                "- Thay đổi kích thước, hình dạng hoặc vẻ ngoài của vú.\n"
                "- Da bị lõm hoặc nhăn.\n"
                "- Núm vú bị thụt vào hoặc biến dạng.\n"
                "- Dịch tiết núm vú bất thường, có thể có máu.\n"
                "- Đỏ hoặc bong tróc da vú hoặc núm vú."
            ),
            "Đề xuất giải pháp": (
                "- Chuyển ngay lập tức để chụp nhũ ảnh và/hoặc siêu âm chẩn đoán.\n"
                "- Sinh thiết kim lõi để lấy mẫu mô phân tích mô học.\n\n"
                "- Quản lý y tế:\n"
                "  + Thảo luận về các kế hoạch điều trị tiềm năng, bao gồm phẫu thuật, xạ trị, hóa trị hoặc liệu pháp hormone.\n"
                "  + Tư vấn di truyền và xét nghiệm nếu nghi ngờ ung thư vú di truyền.\n\n"
                "- Hỗ trợ bệnh nhân:\n"
                "  + Hỗ trợ tâm lý và tư vấn để quản lý lo lắng và sợ hãi.\n"
                "  + Thảo luận chi tiết về các lựa chọn điều trị, tác dụng phụ tiềm ẩn và tiên lượng.\n"
                "  + Hỗ trợ dinh dưỡng để tăng cường hệ thống miễn dịch và duy trì sức khỏe tổng thể."
            )
        }

        self.malignant_info = {
            "Nguyên nhân và triệu chứng": (
                "Nguyên nhân:\n"
                "- Tương tự như các nguyên nhân của ung thư vú nghi ngờ ác tính: đột biến gen, tiền sử gia đình, các yếu tố hormone, các yếu tố lối sống, v.v.\n"
                "- Tiếp xúc lâu dài với estrogen.\n"
                "- Tiền sử ung thư vú hoặc một số bệnh vú không ung thư nhất định.\n\n"
                "Triệu chứng:\n"
                "- Khối u chắc hoặc cứng trong vú hoặc nách không di chuyển.\n"
                "- Thay đổi rõ ràng kích thước, hình dạng hoặc vẻ ngoài của vú.\n"
                "- Thay đổi da trên vú, chẳng hạn như đỏ, lõm hoặc kết cấu da cam.\n"
                "- Thay đổi núm vú, bao gồm thụt vào, tiết dịch (đặc biệt là máu) hoặc loét.\n"
                "- Đau hoặc khó chịu vú dai dẳng."
            ),
            "Đề xuất giải pháp": (
                "- Khám chẩn đoán toàn diện:\n"
                "  + Chụp hình toàn thân, như MRI, CT và PET để xác định sự lan rộng.\n"
                "  + Xét nghiệm máu để đánh giá sức khỏe tổng thể và các dấu hiệu khối u cụ thể.\n\n"
                "- Phương pháp điều trị đa phương thức:\n"
                "  + Phẫu thuật (cắt bỏ khối u, cắt bỏ vú) để loại bỏ khối u và các hạch bạch huyết bị ảnh hưởng.\n"
                "  + Xạ trị để tiêu diệt các tế bào ung thư còn sót lại.\n"
                "  + Hóa trị để nhắm mục tiêu các tế bào ung thư trên toàn cơ thể.\n"
                "  + Liệu pháp hormone cho các ung thư dương tính với thụ thể hormone.\n"
                "  + Liệu pháp nhắm mục tiêu cho các ung thư có các dấu hiệu di truyền cụ thể.\n\n"
                "- Chăm sóc hỗ trợ:\n"
                "  + Quản lý đau và chăm sóc giảm nhẹ để cải thiện chất lượng cuộc sống.\n"
                "  + Hỗ trợ tâm lý và tư vấn cho bệnh nhân và gia đình.\n"
                "  + Hỗ trợ dinh dưỡng để đối phó với tác dụng phụ của điều trị và duy trì sức mạnh.\n"
                "  + Chăm sóc theo dõi định kỳ để giám sát tái phát hoặc quản lý các triệu chứng liên tục."
            )
        }

    def update_solution(self, diagnosis):
        if diagnosis == 'benign':
            self.textBrowser_1.setText(self.benign_info["Nguyên nhân và triệu chứng"])
            self.textBrowser_2.setText(self.benign_info["Đề xuất giải pháp"])
        elif diagnosis == 'suspicious_malignant':
            self.textBrowser_1.setText(self.suspicious_malignant_info["Nguyên nhân và triệu chứng"])
            self.textBrowser_2.setText(self.suspicious_malignant_info["Đề xuất giải pháp"])
        elif diagnosis == 'malignant':
            self.textBrowser_1.setText(self.malignant_info["Nguyên nhân và triệu chứng"])
            self.textBrowser_2.setText(self.malignant_info["Đề xuất giải pháp"])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "HỆ THỐNG CHẨN ĐOÁN VÀ GIẢI PHÁP BỆNH UNG THU VÚ"))
        self.label_4.setText(_translate("MainWindow", "Menu"))
        self.pushButton_7.setText(_translate("MainWindow", "Chẩn đoán bệnh"))
        self.pushButton_8.setText(_translate("MainWindow", "Hồ sơ bệnh án"))
        self.pushButton_9.setText(_translate("MainWindow", "Đề xuất giải pháp"))
        self.pushButton_10.setText(_translate("MainWindow", "Đăng xuất"))
        self.pushButton_11.setText(_translate("MainWindow", "Thông tin bệnh nhân"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Nguyên nhân và triệu chứng:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Đề xuất giải pháp:"))
        self.pushButton.setText(_translate("MainWindow", "Benign"))
        self.pushButton_2.setText(_translate("MainWindow", "suspicious_malignant"))
        self.pushButton_3.setText(_translate("MainWindow", "Malignant"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SolutionWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
