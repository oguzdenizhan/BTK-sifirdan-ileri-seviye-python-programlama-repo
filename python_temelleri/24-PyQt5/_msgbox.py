import sys
from PyQt5 import  QtWidgets
from _msgboxForm import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnExit.clicked.connect(self.showDialog)

    def showDialog(self):

        result =QMessageBox.question(self,"Close Application","Are you sure?",QMessageBox.Ok | QMessageBox.Ignore | QMessageBox.Cancel,QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print("Yes clicked")
            QtWidgets.qApp.quit()
        else:
            print("No clicked")

        # msg = QMessageBox()
    #     msg.setWindowTitle("Close Application")
    #     msg.setText("Are you sure?")
    #     # msg.setIcon(QMessageBox.Question)
    #     msg.setIcon(QMessageBox.Warning)
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Ignore | QMessageBox.Cancel)
    #     msg.setDefaultButton(QMessageBox.Cancel)
    #     msg.setDetailedText("details.....")
    #     msg.buttonClicked.connect(self.popup_button)


    #     x= msg.exec_()
    #     # print(x)
    # def popup_button(self,i):
    #     # print(i.text())
    #     if i.text()== "OK":
    #         print("Okey....")
    #         QtWidgets.qApp.quit()

    #     elif i.text()== "Ignore":
    #         print("Ignore....")

    #     elif i.text()== "Cancel":
    #         print("Cancel....")
def app():
    app =QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()