import sys
from PyQt5 import  QtWidgets
from _radiobuttonForm import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioTurkiye.setChecked(True)
        self.ui.radioilkokul.setChecked(True)

        self.ui.radioTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.radioAzerbaycan.toggled.connect(self.onClickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onClickedUlke)
        self.ui.radioYunanistan.toggled.connect(self.onClickedUlke)

        self.ui.radioilkokul.toggled.connect(self.onClickedEgitim)
        self.ui.radioLise.toggled.connect(self.onClickedEgitim)
        self.ui.radioUniversite.toggled.connect(self.onClickedEgitim)
        self.ui.radioYuksekLisans.toggled.connect(self.onClickedEgitim)

        self.ui.btnUlke.clicked.connect(self.getSelectedUlke)
        self.ui.btnEgitim.clicked.connect(self.getSelectedEgitim)

    def getSelectedUlke(self):
        items = self.ui.groupBoxUlke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblUlke.setText("Seçilen Ülke: "+rb.text())

    def getSelectedEgitim(self):
        items = self.ui.groupBoxUlke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblEgitim.setText("Seçilen Egitim "+rb.text())

    def onClickedUlke(self):
        rd = self.sender()
        if rd.isChecked():
            print("Seçilen Ülke: ",rd.text())

    def onClickedEgitim(self):
        rd = self.sender()
        if rd.isChecked():
            print("Seçilen Ülke: ",rd.text())
        

def app():
    app =QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()