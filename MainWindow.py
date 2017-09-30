# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sat Sep 30 10:42:21 2017
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(382, 158)
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.filePathEdit = QtGui.QLineEdit(self.centralwidget)
        self.filePathEdit.setGeometry(QtCore.QRect(20, 10, 261, 31))
        self.filePathEdit.setObjectName(_fromUtf8("filePathEdit"))
        self.selectFile = QtGui.QPushButton(self.centralwidget)
        self.selectFile.setGeometry(QtCore.QRect(300, 10, 71, 31))
        self.selectFile.setObjectName(_fromUtf8("selectFile"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 101, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.limit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.limit.setBaseSize(QtCore.QSize(0, 0))
        self.limit.setObjectName(_fromUtf8("limit"))
        self.horizontalLayout.addWidget(self.limit)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(230, 50, 141, 41))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.multi_file = QtGui.QRadioButton(self.horizontalLayoutWidget_3)
        self.multi_file.setChecked(True)
        self.multi_file.setObjectName(_fromUtf8("multi_file"))
        self.horizontalLayout_3.addWidget(self.multi_file)
        self.multi_sheet = QtGui.QRadioButton(self.horizontalLayoutWidget_3)
        self.multi_sheet.setObjectName(_fromUtf8("multi_sheet"))
        self.horizontalLayout_3.addWidget(self.multi_sheet)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 50, 211, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.if_title = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.if_title.setEnabled(True)
        self.if_title.setMouseTracking(True)
        self.if_title.setChecked(True)
        self.if_title.setObjectName(_fromUtf8("if_title"))
        self.horizontalLayout_2.addWidget(self.if_title)
        self.has_title = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.has_title.setChecked(True)
        self.has_title.setObjectName(_fromUtf8("has_title"))
        self.horizontalLayout_2.addWidget(self.has_title)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(130, 100, 171, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.confirm = QtGui.QPushButton(self.centralwidget)
        self.confirm.setGeometry(QtCore.QRect(300, 100, 71, 23))
        self.confirm.setObjectName(_fromUtf8("confirm"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.selectFile.setText(_translate("MainWindow", "选择文件", None))
        self.label.setText(_translate("MainWindow", "分割条数", None))
        self.limit.setText(_translate("MainWindow", "10", None))
        self.multi_file.setText(_translate("MainWindow", "多文件", None))
        self.multi_sheet.setText(_translate("MainWindow", "多工作簿", None))
        self.if_title.setText(_translate("MainWindow", "是否有表头", None))
        self.has_title.setText(_translate("MainWindow", "拆分是否包含表头", None))
        self.confirm.setText(_translate("MainWindow", "拆分", None))

# import source_rc
