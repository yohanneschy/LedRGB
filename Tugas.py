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
        #self.pushButton_Kirim.clicked.connect(self.kirim)
        self.pushButton_Keluar.clicked.connect(self.keluar)
        self.textEdit_Hasil.append("Pengaturan LED RGB")
        self.textEdit_Hasil.append(" ")
        #self.pushButton_Kirim.setEnabled(False)

        #self.horizontalSlider_Merah.setEnabled(False)
        #self.horizontalSlider_Hijau.setEnabled(False)
        #self.horizontalSlider_Biru.setEnabled(False)
        self.horizontalSlider_Merah.valueChanged.connect(self.Merah)   
        self.horizontalSlider_Hijau.valueChanged.connect(self.Hijau)        
        self.horizontalSlider_Biru.valueChanged.connect(self.Biru)
        self.TXdata = bytearray(3)
        
    def Merah(self):
        nilaiMerah  = self.horizontalSlider_Merah.value()   
        self.textEdit_Hasil.append("merah = %d" %(nilaiMerah))
        #self.TXdata = bytearray(3)
        self.TXdata[0]=nilaiMerah
        self.ser.write(self.TXdata)
        #time.sleep(1)
        self.bytesToRead = self.ser.inWaiting()
        if (self.bytesToRead > 0):
            rxdata = self.ser.read(self.bytesToRead)
            self.textEdit_Hasil.append(rxdata)
            
    def Hijau(self):
        nilaiHijau = self.horizontalSlider_Hijau.value()
        self.textEdit_Hasil.append("hijau = %d" %(nilaiHijau))
        #self.TXdata = bytearray(3)
        self.TXdata[1]=nilaiHijau
        self.ser.write(self.TXdata)
        #time.sleep(1)
        self.bytesToRead = self.ser.inWaiting()
        if (self.bytesToRead > 0):
            rxdata = self.ser.read(self.bytesToRead)
            self.textEdit_Hasil.append(rxdata)

    def Biru(self):
        nilaiBiru   = self.horizontalSlider_Biru.value()
        self.textEdit_Hasil.append("biru = %d" %(nilaiBiru))
        #self.TXdata = bytearray(3)
        self.TXdata[2]=nilaiBiru
        self.ser.write(self.TXdata)
        #time.sleep(1)
        self.bytesToRead = self.ser.inWaiting()
        if (self.bytesToRead > 0):
            rxdata = self.ser.read(self.bytesToRead)
            self.textEdit_Hasil.append(rxdata)
        
    def openserial(self):
                try:
                        arduino_ports = [
                                p.device
                                for p in serial.tools.list_ports.comports()
                                if 'Arduino' in p.description
                                ]

                        self.ser = serial.Serial(arduino_ports[0], 9600, timeout=0.1)
                        time.sleep(1)
                        #self.ui.pushButton.setEnabled(False)
                        #self.ui.horizontalSlider.setEnabled(True)
                        self.textEdit_Hasil.append("Serial Port Terbuka")
                        #self.pushButton_Kirim.setEnabled(True)
                        #self.workThread = Workthread(self)
                        #self.connect( self.workThread, QtCore.SIGNAL("update(QString)"), self.dummy )
                        #self.workThread.start()
                        
                except:
                       if not arduino_ports:
                        self.textEdit_Hasil.append('Arduino tidak terpasang')
                        
    #def kirim(self):
        #nilaiMerah  = self.horizontalSlider_Merah.value()
        #nilaiHijau  = self.horizontalSlider_Hijau.value()
        #nilaiBiru   = self.horizontalSlider_Biru.value()
        #self.textEdit_Hasil.append("merah = %d, hijau = %d ,biru = %d" %(nilaiMerah,nilaiHijau,nilaiBiru))
        #self.TXdata = bytearray(3)
        #self.TXdata[0]=nilaiMerah
        #self.TXdata[1]=nilaiHijau
        #self.TXdata[2]=nilaiBiru
        #self.ser.write(self.TXdata)
        #time.sleep(2)
        #self.bytesToRead = self.ser.inWaiting()
        #if (self.bytesToRead > 0):
            #rxdata = self.ser.read(self.bytesToRead)
            #self.textEdit_Hasil.append(rxdata)
                
                
    def keluar(self):
        sys.exit()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Aplikasi()
    window.show()
    sys.exit(app.exec_())
