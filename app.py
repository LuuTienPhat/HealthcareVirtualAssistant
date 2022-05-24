# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
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
        MainWindow.setStyleSheet("background: #F0F0F0")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 391, 491))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("border:none;\n"
"outline:none;\n"
"background: #F0F0F0;")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.chat_user_widget = QtWidgets.QWidget(self.tab)
        self.chat_user_widget.setGeometry(QtCore.QRect(50, 40, 330, 51))
        self.chat_user_widget.setStyleSheet("background: #F0F0F0")
        self.chat_user_widget.setObjectName("chat_user_widget")
        self.chat_user = QtWidgets.QLabel(self.chat_user_widget)
        self.chat_user.setGeometry(QtCore.QRect(30, 5, 250, 41))
        self.chat_user.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-right: 10px")
        self.chat_user.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.chat_user.setObjectName("chat_user")
        self.label_5 = QtWidgets.QLabel(self.chat_user_widget)
        self.label_5.setGeometry(QtCore.QRect(290, 10, 31, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("icon/woman.png"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.chat_bot_widget = QtWidgets.QWidget(self.tab)
        self.chat_bot_widget.setGeometry(QtCore.QRect(10, 110, 330, 51))
        self.chat_bot_widget.setStyleSheet("background: transparent")
        self.chat_bot_widget.setObjectName("chat_bot_widget")
        self.chat_bot = QtWidgets.QLabel(self.chat_bot_widget)
        self.chat_bot.setGeometry(QtCore.QRect(50, 5, 250, 41))
        self.chat_bot.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-left: 10px")
        self.chat_bot.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.chat_bot.setWordWrap(True)
        self.chat_bot.setObjectName("chat_bot")
        self.label_7 = QtWidgets.QLabel(self.chat_bot_widget)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("icon/bot.png"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.heart_widget = QtWidgets.QWidget(self.tab)
        self.heart_widget.setEnabled(True)
        self.heart_widget.setGeometry(QtCore.QRect(80, 40, 220, 181))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.heart_widget.setFont(font)
        self.heart_widget.setStyleSheet("background: #fff;\n"
"border-radius:10px")
        self.heart_widget.setObjectName("heart_widget")
        self.label_4 = QtWidgets.QLabel(self.heart_widget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(0, 10, 220, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("icon/heart.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.heart_rate_label = QtWidgets.QLabel(self.heart_widget)
        self.heart_rate_label.setGeometry(QtCore.QRect(0, 80, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(10)
        self.heart_rate_label.setFont(font)
        self.heart_rate_label.setStyleSheet("")
        self.heart_rate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.heart_rate_label.setWordWrap(True)
        self.heart_rate_label.setObjectName("heart_rate_label")
        self.spo2_label = QtWidgets.QLabel(self.heart_widget)
        self.spo2_label.setGeometry(QtCore.QRect(0, 113, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(10)
        self.spo2_label.setFont(font)
        self.spo2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spo2_label.setObjectName("spo2_label")
        self.weather_widget = QtWidgets.QWidget(self.tab)
        self.weather_widget.setEnabled(True)
        self.weather_widget.setGeometry(QtCore.QRect(80, 100, 220, 220))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.weather_widget.setFont(font)
        self.weather_widget.setStyleSheet("background: #fff;\n"
"border-radius:10px")
        self.weather_widget.setObjectName("weather_widget")
        self.label_11 = QtWidgets.QLabel(self.weather_widget)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(80, 10, 71, 71))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("icon/sun.png"))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.city_label = QtWidgets.QLabel(self.weather_widget)
        self.city_label.setGeometry(QtCore.QRect(0, 87, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.city_label.setFont(font)
        self.city_label.setAlignment(QtCore.Qt.AlignCenter)
        self.city_label.setObjectName("city_label")
        self.degree_label = QtWidgets.QLabel(self.weather_widget)
        self.degree_label.setGeometry(QtCore.QRect(0, 112, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(14)
        self.degree_label.setFont(font)
        self.degree_label.setAlignment(QtCore.Qt.AlignCenter)
        self.degree_label.setObjectName("degree_label")
        self.weather_label = QtWidgets.QLabel(self.weather_widget)
        self.weather_label.setGeometry(QtCore.QRect(0, 140, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.weather_label.setFont(font)
        self.weather_label.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_label.setObjectName("weather_label")
        self.humidty_label = QtWidgets.QLabel(self.weather_widget)
        self.humidty_label.setGeometry(QtCore.QRect(0, 170, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(8)
        self.humidty_label.setFont(font)
        self.humidty_label.setAlignment(QtCore.Qt.AlignCenter)
        self.humidty_label.setObjectName("humidty_label")
        self.wind_label = QtWidgets.QLabel(self.weather_widget)
        self.wind_label.setGeometry(QtCore.QRect(0, 187, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(8)
        self.wind_label.setFont(font)
        self.wind_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wind_label.setObjectName("wind_label")
        self.btn_active = QtWidgets.QPushButton(self.tab)
        self.btn_active.setGeometry(QtCore.QRect(260, 400, 75, 23))
        self.btn_active.setStyleSheet("background: rgb(255, 255, 255)")
        self.btn_active.setObjectName("btn_active")
        self.screen = QtWidgets.QTextEdit(self.tab)
        self.screen.setGeometry(QtCore.QRect(50, 380, 104, 71))
        self.screen.setStyleSheet("background: rgb(255, 255, 255)")
        self.screen.setObjectName("screen")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.alarm_list = QtWidgets.QListWidget(self.tab_2)
        self.alarm_list.setGeometry(QtCore.QRect(10, 80, 371, 241))
        self.alarm_list.setStyleSheet("border:1px solid black;\n"
"padding: 10px")
        self.alarm_list.setObjectName("alarm_list")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(150, 40, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("size: 16px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_new_alarm = QtWidgets.QPushButton(self.tab_2)
        self.btn_new_alarm.setGeometry(QtCore.QRect(230, 35, 31, 31))
        self.btn_new_alarm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_new_alarm.setAutoFillBackground(False)
        self.btn_new_alarm.setStyleSheet("background: transparent;\n"
"")
        self.btn_new_alarm.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_new_alarm.setIcon(icon1)
        self.btn_new_alarm.setIconSize(QtCore.QSize(48, 48))
        self.btn_new_alarm.setObjectName("btn_new_alarm")
        self.alarm_widget_item = QtWidgets.QWidget(self.tab_2)
        self.alarm_widget_item.setGeometry(QtCore.QRect(60, 360, 281, 51))
        self.alarm_widget_item.setStyleSheet("border: 1px solid black")
        self.alarm_widget_item.setObjectName("alarm_widget_item")
        self.chat_bot_2 = QtWidgets.QLabel(self.alarm_widget_item)
        self.chat_bot_2.setGeometry(QtCore.QRect(56, 13, 101, 21))
        self.chat_bot_2.setStyleSheet("")
        self.chat_bot_2.setObjectName("chat_bot_2")
        self.label_12 = QtWidgets.QLabel(self.alarm_widget_item)
        self.label_12.setGeometry(QtCore.QRect(10, 9, 31, 31))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("icon/clock.png"))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.alarm_widget_item)
        self.pushButton.setGeometry(QtCore.QRect(240, 12, 31, 23))
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_51 = QtWidgets.QLabel(self.tab_3)
        self.label_51.setGeometry(QtCore.QRect(0, 10, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("font-size: 16px;\n"
"text-decoration: underline;")
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(35, 70, 71, 16))
        self.label_6.setObjectName("label_6")
        self.lineEditPatientCode = QtWidgets.QLineEdit(self.tab_3)
        self.lineEditPatientCode.setGeometry(QtCore.QRect(115, 70, 241, 20))
        self.lineEditPatientCode.setAutoFillBackground(False)
        self.lineEditPatientCode.setStyleSheet("border: 1px solid #888;\n"
"background: #fff")
        self.lineEditPatientCode.setText("")
        self.lineEditPatientCode.setFrame(True)
        self.lineEditPatientCode.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditPatientCode.setDragEnabled(False)
        self.lineEditPatientCode.setReadOnly(True)
        self.lineEditPatientCode.setClearButtonEnabled(False)
        self.lineEditPatientCode.setObjectName("lineEditPatientCode")
        self.lineEditName = QtWidgets.QLineEdit(self.tab_3)
        self.lineEditName.setGeometry(QtCore.QRect(115, 120, 241, 20))
        self.lineEditName.setAutoFillBackground(False)
        self.lineEditName.setStyleSheet("border: 1px solid black;\n"
"background: #fff")
        self.lineEditName.setObjectName("lineEditName")
        self.label_71 = QtWidgets.QLabel(self.tab_3)
        self.label_71.setGeometry(QtCore.QRect(35, 120, 71, 16))
        self.label_71.setObjectName("label_71")
        self.lineEditPhone = QtWidgets.QLineEdit(self.tab_3)
        self.lineEditPhone.setGeometry(QtCore.QRect(115, 170, 241, 20))
        self.lineEditPhone.setAutoFillBackground(False)
        self.lineEditPhone.setStyleSheet("border: 1px solid black;\n"
"background: #fff")
        self.lineEditPhone.setObjectName("lineEditPhone")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(35, 170, 71, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(35, 260, 81, 16))
        self.label_9.setObjectName("label_9")
        self.textEditDisease = QtWidgets.QTextEdit(self.tab_3)
        self.textEditDisease.setGeometry(QtCore.QRect(115, 260, 241, 91))
        self.textEditDisease.setStyleSheet("border: 1px solid #888;\n"
"background: #fff")
        self.textEditDisease.setReadOnly(True)
        self.textEditDisease.setObjectName("textEditDisease")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(35, 210, 71, 16))
        self.label_10.setObjectName("label_10")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(110, 210, 241, 20))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButtonMale = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonMale.setGeometry(QtCore.QRect(5, 0, 82, 17))
        self.radioButtonMale.setChecked(True)
        self.radioButtonMale.setObjectName("radioButtonMale")
        self.radioButtonFemale = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonFemale.setGeometry(QtCore.QRect(135, 0, 82, 17))
        self.radioButtonFemale.setObjectName("radioButtonFemale")
        self.btnUpdate = QtWidgets.QPushButton(self.tab_3)
        self.btnUpdate.setGeometry(QtCore.QRect(265, 370, 91, 23))
        self.btnUpdate.setStyleSheet("border-radius: 4px;\n"
"border: 1px solid black;\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #37455E;")
        self.btnUpdate.setObjectName("btnUpdate")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 50, 371, 411))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("QListWidget::item {\n"
"    background-color: #d9d9d9;\n"
"    margin: 5px;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.tabWidget.addTab(self.tab_4, "")
        self.btn_speak = QtWidgets.QPushButton(self.centralwidget)
        self.btn_speak.setGeometry(QtCore.QRect(165, 500, 60, 60))
        self.btn_speak.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_speak.setAutoFillBackground(False)
        self.btn_speak.setStyleSheet("background: transparent;\n"
"")
        self.btn_speak.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/blue-mic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_speak.setIcon(icon3)
        self.btn_speak.setIconSize(QtCore.QSize(48, 48))
        self.btn_speak.setObjectName("btn_speak")
        self.btn_send = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send.setGeometry(QtCore.QRect(340, 570, 41, 41))
        self.btn_send.setAutoFillBackground(False)
        self.btn_send.setStyleSheet("background: transparent;\n"
"")
        self.btn_send.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_send.setIcon(icon4)
        self.btn_send.setIconSize(QtCore.QSize(32, 32))
        self.btn_send.setObjectName("btn_send")
        self.ask_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.ask_entry.setGeometry(QtCore.QRect(10, 570, 321, 41))
        self.ask_entry.setStyleSheet("background: transparent;\n"
"border:none;\n"
"border-raidus: 10px;")
        self.ask_entry.setInputMask("")
        self.ask_entry.setCursorPosition(0)
        self.ask_entry.setDragEnabled(False)
        self.ask_entry.setObjectName("ask_entry")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Healthcare Virtual Assistant"))
        self.chat_user.setText(_translate("MainWindow", "..."))
        self.chat_bot.setText(_translate("MainWindow", "..."))
        self.heart_rate_label.setText(_translate("MainWindow", "Your heart rate is 79bpm "))
        self.spo2_label.setText(_translate("MainWindow", "Your spo2 is 99%"))
        self.city_label.setText(_translate("MainWindow", "Ho Chi Minh city"))
        self.degree_label.setText(_translate("MainWindow", "16*C"))
        self.weather_label.setText(_translate("MainWindow", "Weather"))
        self.humidty_label.setText(_translate("MainWindow", "Humidty"))
        self.wind_label.setText(_translate("MainWindow", "Wind"))
        self.btn_active.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Chat"))
        self.label.setText(_translate("MainWindow", "Alarm"))
        self.chat_bot_2.setText(_translate("MainWindow", "It\'s 9:00 pm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Alarm"))
        self.label_51.setText(_translate("MainWindow", "Patient Information"))
        self.label_6.setText(_translate("MainWindow", "Patient Code:"))
        self.lineEditPatientCode.setPlaceholderText(_translate("MainWindow", "Patient code..."))
        self.lineEditName.setPlaceholderText(_translate("MainWindow", "..."))
        self.label_71.setText(_translate("MainWindow", "Name:"))
        self.lineEditPhone.setPlaceholderText(_translate("MainWindow", "..."))
        self.label_8.setText(_translate("MainWindow", "Phone:"))
        self.label_9.setText(_translate("MainWindow", "Disease Infor:"))
        self.textEditDisease.setPlaceholderText(_translate("MainWindow", "..."))
        self.label_10.setText(_translate("MainWindow", "Sex:"))
        self.radioButtonMale.setText(_translate("MainWindow", "Male"))
        self.radioButtonFemale.setText(_translate("MainWindow", "Female"))
        self.btnUpdate.setText(_translate("MainWindow", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Information"))
        self.label_2.setText(_translate("MainWindow", "Your measurement history"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "HR: 100 bpm, spo2: 98% | 5/24/2022 2:19 AM"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "HR: 100 bpm, spo2: 98% | 5/24/2022 2:19 AM"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "HR: 100 bpm, spo2: 98% | 5/24/2022 2:19 AM"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "History"))
        self.ask_entry.setPlaceholderText(_translate("MainWindow", "Ask me"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
