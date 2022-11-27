import sys

from PySide6 import QtWidgets

from ui.loginform import Ui_Form
from ui.form1 import Ui_MainWindow


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Авторизация")
        self.ui.lineEdit_login.setPlaceholderText("введите логин")
        self.ui.lineEdit_password.setPlaceholderText("введите пароль")
        self.ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()
    app.exec()

    # app = QtWidgets.QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # app.exec()

