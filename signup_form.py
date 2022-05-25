# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background : #363636;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.confirmpass = QtWidgets.QLineEdit(self.centralwidget)
        self.confirmpass.setGeometry(QtCore.QRect(160, 312, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.confirmpass.setFont(font)
        self.confirmpass.setStyleSheet("color: rgb(243,243,243);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(243,243,243)")
        self.confirmpass.setObjectName("confirmpass")
        self.signupbutton = QtWidgets.QPushButton(self.centralwidget)
        self.signupbutton.setGeometry(QtCore.QRect(130, 410, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.signupbutton.setFont(font)
        self.signupbutton.setStyleSheet("background: rgb(243, 243, 243);\n"
"color: rgb(54, 54, 54);\n"
"border-radius: 10px;\n"
"border: none;")
        self.signupbutton.setObjectName("signupbutton")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(160, 240, 200, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setStyleSheet("\n"
"color: rgb(243,243,243);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(243,243,243)")
        self.password.setText("")
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(38, 250, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(243,243,243)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(38, 322, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(243,243,243)")
        self.label_4.setObjectName("label_4")
        self.invalid = QtWidgets.QLabel(self.centralwidget)
        self.invalid.setGeometry(QtCore.QRect(0, 470, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.invalid.setFont(font)
        self.invalid.setStyleSheet("color: #FFFF33;")
        self.invalid.setAlignment(QtCore.Qt.AlignCenter)
        self.invalid.setObjectName("invalid")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(160, 170, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.email.setFont(font)
        self.email.setStyleSheet("color: rgb(243,243,243);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(243,243,243);")
        self.email.setObjectName("email")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(38, 179, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(243,243,243)")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 60, 390, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(243,243,243)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnback = QtWidgets.QPushButton(self.centralwidget)
        self.btnback.setGeometry(QtCore.QRect(0, 10, 61, 41))
        self.btnback.setStyleSheet("background: transparent;")
        self.btnback.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Users/PC/Downloads/previous (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnback.setIcon(icon1)
        self.btnback.setIconSize(QtCore.QSize(32, 32))
        self.btnback.setObjectName("btnback")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(0, 10, 61, 41))
        self.btnBack.setStyleSheet("background: transparent;")
        self.btnBack.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/previous (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon2)
        self.btnBack.setIconSize(QtCore.QSize(32, 32))
        self.btnBack.setObjectName("btnBack")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBack = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Users/PC/Pictures/423-4237996_return-svg-png-icon-free-download-onlinewebfonts-return-back-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBack.setIcon(icon3)
        self.actionBack.setObjectName("actionBack")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign Up"))
        self.signupbutton.setText(_translate("MainWindow", "Sign up"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Confirm Pass"))
        self.invalid.setText(_translate("MainWindow", "Invalid email"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.label.setText(_translate("MainWindow", "Sign up"))
        self.actionBack.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
