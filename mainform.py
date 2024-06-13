# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\bitacora.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(833, 456)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\ui\\resources/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainForm.setWindowIcon(icon)
        mainForm.setStyleSheet("/* General styling */\n"
"* {\n"
"    font-family: \"Iosevka\", \"Monospace\";\n"
"    color: #D0D0D0; /* Light gray text */\n"
"    background-color: #1E1E1E; /* Dark background */\n"
"}\n"
"\n"
"/* QPushButton */\n"
"QPushButton {\n"
"    background-color: #2D2D2D; /* Slightly lighter than background */\n"
"    border: 1px solid #555555;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3D3D3D;\n"
"    border: 1px solid #777777;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5D5D5D;\n"
"    border: 1px solid #AAAAAA;\n"
"}\n"
"\n"
"/* QLabel */\n"
"QLabel {\n"
"    color: #D0D0D0;\n"
"    background-color: transparent; /* To keep the background consistent */\n"
"}\n"
"\n"
"/* QLineEdit */\n"
"QLineEdit {\n"
"    background-color: #2D2D2D;\n"
"    border: 1px solid #555555;\n"
"    padding: 5px;\n"
"    color: #D0D0D0;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #777777;\n"
"}\n"
"\n"
"/* QComboBox */\n"
"QComboBox {\n"
"    background-color: #2D2D2D;\n"
"    border: 1px solid #555555;\n"
"    padding: 5px;\n"
"    color: #D0D0D0;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #777777;\n"
"}\n"
"\n"
"/* QComboBox drop-down */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #1E1E1E;\n"
"    border: 1px solid #555555;\n"
"    color: #D0D0D0;\n"
"}\n"
"\n"
"/* QMenuBar */\n"
"QMenuBar {\n"
"    background-color: #1E1E1E;\n"
"    color: #D0D0D0;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: #1E1E1E;\n"
"    color: #D0D0D0;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #3D3D3D;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* QMenu */\n"
"QMenu {\n"
"    background-color: #2D2D2D;\n"
"    border: 1px solid #555555;\n"
"    color: #D0D0D0;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: #2D2D2D;\n"
"    padding: 5px 25px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #3D3D3D;\n"
"}\n"
"\n"
"/* QTabWidget */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #555555;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #2D2D2D;\n"
"    border: 1px solid #555555;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #3D3D3D;\n"
"    border: 1px solid #777777;\n"
"}\n"
"\n"
"/* QScrollBar */\n"
"QScrollBar:vertical {\n"
"    background-color: #2D2D2D;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px solid #555555;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #555555;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background-color: #2D2D2D;\n"
"    border: 1px solid #555555;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background-color: #2D2D2D;\n"
"}\n"
"")
        self.label_5 = QtWidgets.QLabel(mainForm)
        self.label_5.setGeometry(QtCore.QRect(410, 360, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Iosevka")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(mainForm)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Iosevka")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(mainForm)
        self.label_7.setGeometry(QtCore.QRect(10, 360, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Iosevka")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(mainForm)
        self.label_8.setGeometry(QtCore.QRect(10, 400, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Iosevka")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_8.setObjectName("label_8")
        self.textDescription = QtWidgets.QTextEdit(mainForm)
        self.textDescription.setGeometry(QtCore.QRect(160, 150, 631, 191))
        self.textDescription.setFrameShape(QtWidgets.QFrame.Box)
        self.textDescription.setLineWidth(2)
        self.textDescription.setObjectName("textDescription")
        self.label_9 = QtWidgets.QLabel(mainForm)
        self.label_9.setGeometry(QtCore.QRect(20, 0, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Iosevka")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(mainForm)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 561, 59))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Iosevka")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.cb_machine = QtWidgets.QComboBox(self.layoutWidget)
        self.cb_machine.setObjectName("cb_machine")
        self.verticalLayout.addWidget(self.cb_machine)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Iosevka")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.cb_id = QtWidgets.QComboBox(self.layoutWidget)
        self.cb_id.setObjectName("cb_id")
        self.verticalLayout_2.addWidget(self.cb_id)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Iosevka")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.cb_tech = QtWidgets.QComboBox(self.layoutWidget)
        self.cb_tech.setObjectName("cb_tech")
        self.verticalLayout_3.addWidget(self.cb_tech)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Iosevka")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_4.addWidget(self.dateEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.textWorkorder = QtWidgets.QTextEdit(mainForm)
        self.textWorkorder.setGeometry(QtCore.QRect(470, 390, 111, 31))
        self.textWorkorder.setLineWidth(3)
        self.textWorkorder.setObjectName("textWorkorder")
        self.splitter = QtWidgets.QSplitter(mainForm)
        self.splitter.setGeometry(QtCore.QRect(710, 380, 105, 56))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pb_submit = QtWidgets.QPushButton(self.splitter)
        self.pb_submit.setObjectName("pb_submit")
        self.pb_clear = QtWidgets.QPushButton(self.splitter)
        self.pb_clear.setObjectName("pb_clear")
        self.repairSpinbox = QtWidgets.QSpinBox(mainForm)
        self.repairSpinbox.setGeometry(QtCore.QRect(250, 361, 61, 31))
        self.repairSpinbox.setMinimum(0)
        self.repairSpinbox.setMaximum(1000)
        self.repairSpinbox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.repairSpinbox.setObjectName("repairSpinbox")
        self.downSpinbox = QtWidgets.QSpinBox(mainForm)
        self.downSpinbox.setGeometry(QtCore.QRect(250, 400, 61, 31))
        self.downSpinbox.setMinimum(0)
        self.downSpinbox.setMaximum(1000)
        self.downSpinbox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.downSpinbox.setObjectName("downSpinbox")
        self.pb_theme = QtWidgets.QPushButton(mainForm)
        self.pb_theme.setGeometry(QtCore.QRect(710, 10, 111, 28))
        self.pb_theme.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_theme.setAutoDefault(True)
        self.pb_theme.setObjectName("pb_theme")

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "Summit Planta Leon - Maintenance Form"))
        self.label_5.setText(_translate("mainForm", "Work Order # (si aplica)"))
        self.label_6.setText(_translate("mainForm", "Descripcion:"))
        self.label_7.setText(_translate("mainForm", " Tiempo de Reparacion:"))
        self.label_8.setText(_translate("mainForm", " Tiempo Muerto:"))
        self.label_9.setText(_translate("mainForm", "BITACORA DE MANTENIMIENTO"))
        self.label.setText(_translate("mainForm", "Equipo: "))
        self.label_2.setText(_translate("mainForm", "ID de Maquina:"))
        self.label_3.setText(_translate("mainForm", "Tecnico:"))
        self.label_4.setText(_translate("mainForm", "Fecha:"))
        self.dateEdit.setDisplayFormat(_translate("mainForm", "d/M/yyyy"))
        self.pb_submit.setText(_translate("mainForm", "Enviar Datos"))
        self.pb_clear.setText(_translate("mainForm", "Borrar Datos"))
        self.pb_theme.setText(_translate("mainForm", "Toggle Theme"))
