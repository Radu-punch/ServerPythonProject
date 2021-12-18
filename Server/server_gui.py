from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton,QLineEdit,QMessageBox
from server import *
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(695,461)
        #Form.resize(695, 461)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 191, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 310, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 360, 191, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 410, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(260, 316, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 366, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 416, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(440, 316, 70, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.button_set_port)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 365, 70, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.button_set_path)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 416, 100, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 30, 101, 31))
        self.pushButton_4.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.button_run_option)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 80, 101, 31))
        self.pushButton_5.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 130, 101, 31))
        self.pushButton_6.setStyleSheet("background-color:rgb(0, 0, 255)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.button_meintenance_otpion)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "WebServer info"))
        self.label_2.setText(_translate("Form", "Server Status:"))
        self.label_3.setText(_translate("Form", "Server Adress:"))
        self.label_4.setText(_translate("Form", "Server Port:"))
        self.label_5.setText(_translate("Form", "Set Port"))
        self.label_6.setText(_translate("Form", "Set Root Directory"))
        self.label_7.setText(_translate("Form", "Set Meintenance"))
        self.pushButton.setText(_translate("Form", "Port"))
        self.pushButton_2.setText(_translate("Form", "Root"))
        self.pushButton_3.setText(_translate("Form", "Meintenance"))
        self.pushButton_4.setText(_translate("Form", "Start"))
        self.pushButton_5.setText(_translate("Form", "Stop"))
        self.pushButton_6.setText(_translate("Form", "Meintenance"))

    def button_set_port(self):
        self.stp=self.lineEdit.text()
        self.label_4.setText("Server Port:"+" "+self.stp)
        self.label_4.adjustSize()
        self.label_3.setText("Server Adress: localhost:"+self.stp)
        self.label_3.adjustSize()


    def button_set_path(self):
        str=self.lineEdit_2.text()
        print(str)
        path="D:\pythonProject\Server"
        if str != path:
            msg=QMessageBox()
            msg.setWindowTitle("PATH incorect")
            msg.setText("path Root cu site-ul e data incorect")
            x=msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("PATH corect")
            msg.setText("Path-ul e corect")
            x = msg.exec_()

    def set_conection(self):
        port = int(self.stp)
        port = check_port(port)
        socket_server = conect_to_socket(port)
        while True:
            client, adresa = socket_server.accept()
            request = client.recv(4096)
            print(request.decode('utf-8'))
            print()
            print(adresa)
            return client ,request

    def button_meintenance_otpion(self):
        while True:
            client ,request = self.set_conection()
            ras = MentinanceReDirect()
            client.sendall(ras)
            #client.shutdown(socket.SHUT_WR)
    def button_run_option(self):
        while True:
            client , request = self.set_conection()
            response = server_response(request)
            client.sendall(response)

if __name__ == "__main__":
     import sys
     app = QtWidgets.QApplication(sys.argv)
     Form = QtWidgets.QWidget()
     ui = Ui_Form()
     ui.setupUi(Form)
     Form.show()
     sys.exit(app.exec_())
