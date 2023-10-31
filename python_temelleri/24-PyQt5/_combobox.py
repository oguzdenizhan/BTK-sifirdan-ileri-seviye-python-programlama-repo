import sys
from PyQt5 import  QtWidgets
from _comboboxForm import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)

        # combo=self.ui.cbSehirler
        # combo.addItem("Ankara")
        # combo.addItem("İstanbul")
        # combo.addItem("Kocaeli")
        # combo.addItems(["Adana","Antalya","Malatya"])

        self.ui.btnLoadItems.clicked.connect(self.LoadItems)
        self.ui.btnGetItem.clicked.connect(self.GetItem)
        self.ui.btnClearItems.clicked.connect(self.ClearItems)

        self.ui.cbSehirler.currentIndexChanged.connect(self.SelectedChangedIndex)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.SelectedChangedIndex)


    
    def LoadItems(self):

        sehirler = ["Adana","Antalya","Malatya"]
        self.ui.cbSehirler.addItems(sehirler)

    def GetItem(self):
        print(self.ui.cbSehirler.currentText())
        print(self.ui.cbSehirler.currentIndex())
        count =self.ui.cbSehirler.count()

        self.ui.lblResult.setText(self.ui.cbSehirler.currentText())


        for index in range(count):
            print(self.ui.cbSehirler.itemText(index))

    def ClearItems(self):
        self.ui.cbSehirler.clear()
        self.ui.lblResult.clear()

    def SelectedChangedIndex(self,index):
        print(index)

    def SelectedChangedText(self,text):
        print(text)

def app():
    app =QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()