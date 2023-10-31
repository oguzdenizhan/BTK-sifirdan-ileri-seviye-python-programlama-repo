import sys
from PyQt5 import  QtWidgets
from _checkboxForm import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cb_cinema.stateChanged.connect(self.show_state)
        self.ui.cb_kitap.stateChanged.connect(self.show_state)
        self.ui.cb_spor.stateChanged.connect(self.show_state)
        self.ui.cb_Math.stateChanged.connect(self.show_state)
        self.ui.cb_programming.stateChanged.connect(self.show_state)
        self.ui.cb_webdesign.stateChanged.connect(self.show_state)

        self.ui.btn_kaydet_dersler.clicked.connect(self.getAllClasses)
        self.ui.btn_kaydet_hobiler.clicked.connect(self.getAllHobbies)


    def getAllHobbies(self):
        items = self.ui.groupHobbies.findChildren(QtWidgets.QCheckBox)
        result=""
        for cb in items:
            if cb.isChecked():
                result +=cb.text() +"\n"
        self.ui.lbl_sonuc_hobiler.setText(result)

    def getAllClasses(self):
        items = self.ui.groupClasses.findChildren(QtWidgets.QCheckBox)
        result=""
        for cb in items:
            if cb.isChecked():
                result +=cb.text() +"\n"
        self.ui.lbl_sonuc_dersler.setText(result)


    def show_state(self,value):
        # print(value)
        # print(self.ui.cb_cinema.isChecked())
        # print(self.ui.cb_cinema.text())

        print(value)
        cb= self.sender()
        print(cb.text())
        print(cb.isChecked())

 
def app():
    app =QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()
