import sys, os, glob
from PyQt4 import QtCore, QtGui, uic
import serial, time

qtCreatorFile = "Tugas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.pushButton_Openserial.clicked.connect(self.openserial)
		self.pushButton_Kirim.clicked.connect(self.kirim)
		self.pushButton_Keluar.clicked.connect(self.keluar)
		
		self.textEdit_Hasil.append("Pengaturan LED RGB")
		self.textEdit_Hasil.append(" ")
		self.pushButton_Kirim.setEnabled(False)
		
	def openserial(self):
			self.ser = serial.Serial("COM3", "9600", timeout=0.1)
			if self.ser.isOpen():
				self.textEdit_Hasil.append("Buka Serial Port")
				self.pushButton_Kirim.setEnabled(True)

			
	def kirim(self):
		nilaiMerah  = self.horizontalSlider_Merah.value()
		nilaiHijau  = self.horizontalSlider_Hijau.value()
		nilaiBiru   = self.horizontalSlider_Biru.value()
		self.textEdit_Hasil.append("merah = %d, hijau = %d ,biru = %d" %(nilaiMerah,nilaiHijau,nilaiBiru))
		self.TXdata = bytearray(3)
		self.TXdata[0]=nilaiMerah
		self.TXdata[1]=nilaiHijau
		self.TXdata[2]=nilaiBiru
		self.ser.write(self.TXdata)
		time.sleep(2)
		self.bytesToRead = self.ser.inWaiting()
		if (self.bytesToRead > 0):
			rxdata = self.ser.read(self.bytesToRead)
			self.textEdit_Hasil.append(rxdata)
				
				
	def keluar(self):
		sys.exit()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
