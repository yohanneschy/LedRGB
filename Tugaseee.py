# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tugas.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(673, 669)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 24, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit_Hasil = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_Hasil.setGeometry(QtCore.QRect(10, 110, 371, 501))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Fixedsys"))
        self.textEdit_Hasil.setFont(font)
        self.textEdit_Hasil.setObjectName(_fromUtf8("textEdit_Hasil"))
        self.pushButton_Openserial = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Openserial.setGeometry(QtCore.QRect(290, 20, 91, 23))
        self.pushButton_Openserial.setObjectName(_fromUtf8("pushButton_Openserial"))
        self.pushButton_Keluar = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Keluar.setGeometry(QtCore.QRect(290, 50, 91, 23))
        self.pushButton_Keluar.setObjectName(_fromUtf8("pushButton_Keluar"))
        self.horizontalSlider_Merah = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_Merah.setGeometry(QtCore.QRect(90, 20, 160, 22))
        self.horizontalSlider_Merah.setMaximum(255)
        self.horizontalSlider_Merah.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Merah.setObjectName(_fromUtf8("horizontalSlider_Merah"))
        self.horizontalSlider_Biru = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_Biru.setGeometry(QtCore.QRect(90, 80, 160, 22))
        self.horizontalSlider_Biru.setMaximum(255)
        self.horizontalSlider_Biru.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Biru.setObjectName(_fromUtf8("horizontalSlider_Biru"))
        self.horizontalSlider_Hijau = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_Hijau.setGeometry(QtCore.QRect(90, 50, 160, 22))
        self.horizontalSlider_Hijau.setMaximum(255)
        self.horizontalSlider_Hijau.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Hijau.setObjectName(_fromUtf8("horizontalSlider_Hijau"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 10, 241, 621))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("warna.jpg")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo LED Arduino", None))
        self.label.setText(_translate("MainWindow", "Merah", None))
        self.pushButton_Openserial.setText(_translate("MainWindow", "Open Serial", None))
        self.pushButton_Keluar.setText(_translate("MainWindow", "Keluar", None))
        self.label_2.setText(_translate("MainWindow", "Biru", None))
        self.label_3.setText(_translate("MainWindow", "Hijau", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

