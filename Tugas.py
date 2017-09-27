import sys, os, glob
from PyQt4 import QtCore, QtGui, uic
from Tugaseee import Ui_MainWindow
import serial, time
import serial.tools.list_ports

qtCreatorFile = "Tugas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Aplikasi(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton_Openserial.clicked.connect(self.openserial)
        self.pushButton_Hapus.clicked.connect(self.hapus)
        self.pushButton_Keluar.clicked.connect(self.keluar)
        self.textEdit_Hasil.append("Pengaturan LED RGB")
        self.textEdit_Hasil.append(" ")

        self.horizontalSlider_Merah.valueChanged.connect(self.Merah)   
        self.horizontalSlider_Hijau.valueChanged.connect(self.Hijau)        
        self.horizontalSlider_Biru.valueChanged.connect(self.Biru)
        self.TXdata = bytearray(2)
        
    def Merah(self):
        nilaiMerah  = self.horizontalSlider_Merah.value()   
        self.textEdit_Hasil.append("merah = %d" %(nilaiMerah))
        self.TXdata[0]= bytes(b'R')
        self.TXdata[1]= nilaiMerah
        self.ser.write(self.TXdata)

    def Hijau(self):
        nilaiHijau = self.horizontalSlider_Hijau.value()
        self.textEdit_Hasil.append("hijau = %d" %(nilaiHijau))
        self.TXdata[0]= bytes(b'G')
        self.TXdata[1]=nilaiHijau
        self.ser.write(self.TXdata)

    def Biru(self):
        nilaiBiru   = self.horizontalSlider_Biru.value()
        self.textEdit_Hasil.append("biru = %d" %(nilaiBiru))
        self.TXdata[0]= bytes(b'B')
        self.TXdata[1]=nilaiBiru
        self.ser.write(self.TXdata)
        
    def openserial(self):
                try:
                        arduino_ports = [
                                a.device
                                for a in serial.tools.list_ports.comports()
                                if 'Arduino Uno' in a.description
                                ]

                        self.ser = serial.Serial(arduino_ports[0], 9600, timeout=0.1)
                        time.sleep(1)
                        self.textEdit_Hasil.append("Serial Port Terbuka")
                            
                except:
                       if not arduino_ports:
                        self.textEdit_Hasil.append('Arduino tidak terpasang')
                        
    def hapus(self):
        self.textEdit_Hasil.clear()
        
    def keluar(self):
        sys.exit()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Aplikasi()
    window.show()
    sys.exit(app.exec_())
