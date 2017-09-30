# -*- encoding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from PyQt4 import QtGui, QtCore
from source import source_rc
from util.excel import Exce
import time
from MainWindow import Ui_MainWindow
class Main(QtGui.QMainWindow, Ui_MainWindow):
    filePath = None
    notifyProgress = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(u"Excel拆分工具")

        self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint)
        # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height())


        #绑定信号槽
        self.connect(self.confirm, QtCore.SIGNAL("clicked()"), self.confirm_split) #确认拆分
        self.connect(self.selectFile, QtCore.SIGNAL("clicked()"), self.select_file) #打开文件
        self.notifyProgress.connect(self.__onProgress) #绑定进度条

    def select_file(self):
        filename = QtGui.QFileDialog.getOpenFileName(self.selectFile, 'Open file', './','Excel Files(*.xlsx);;Excel Files (*.xls)')
        self.filePathEdit.setText(filename)
        self.filePath = str(filename)

    def confirm_split(self):
        limit = int(self.limit.text())

        if (self.if_title.isChecked()):
            if_title = True
        else:
            if_title = False

        if (self.has_title.isChecked()):
            has_title = True
        else:
            has_title = False

        if (self.multi_file.isChecked()):
            is_multi = True
        else:
            is_multi = False

        excel = Exce(limit=limit,read_file=self.filePath,if_title=if_title,has_title=has_title,is_multi=is_multi)
        excel.file_split()
        # self.notifyProgress.emit(10)
        self.progressBar.setRange(0, 100) #设置进度条
        # self.informationMessage()
        for i in range(0,101):
            self.notifyProgress.emit(i)
            time.sleep(0.001)
        self.informationMessage()


    def informationMessage(self):
        QtGui.QMessageBox.information(self, u"信息框",u"拆分成功",u"确定")

    #   更新进度条数据
    def __onProgress(self,i):
        self.progressBar.setValue(i)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dialog = Main()
    dialog.show()
    app.exec_()