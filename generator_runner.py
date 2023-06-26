import sys
from random import randint
from Generator_number import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.button_clicked = 0
        # self.e1 = self.e2 = False
        self.ButtonControl()
        self.lineEdit.textChanged.connect(self.ButtonControl)
        self.lineEdit_2.textChanged.connect(self.ButtonControl)
        self.pushButton.clicked.connect(lambda: self.ButtonClick(1))

    def ButtonClick(self,val):
        self.button_clicked += val
        a = self.lineEdit.text() or '10'
        b = self.lineEdit_2.text() or '100'
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        c = randint(int(a),int(b))
        self.label_4.setText(str(c))
        self.label_5.setText(str(self.button_clicked))
        self.label_4.adjustSize()
        self.label_5.adjustSize()

    def ButtonControl(self):
        e1, e2 = self.lineEdit.text() != '', self.lineEdit_2.text() != ''
        self.pushButton.setEnabled(e1 and e2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_obj = MyWindow()
    window_obj.show()
    app.exec()