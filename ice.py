from PyQt5 import QtWidgets, QtCore, QtGui
from loguru import logger
from typing import List
import random
import sys
import ice_design
import ice_data
import ice_random
import ice_resource


class IceField(QtWidgets.QMainWindow, ice_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.field = ice_data.IceField()
        self.ice_btns: List[List[QtWidgets.QPushButton]] = list()
        self.GBField.setLayout(QtWidgets.QGridLayout())
        self.BtnCreate.clicked.connect(self.generate_field)
        self.deaths = 0

    def generate_field(self):
        """
        generates field of selected size
        :return:
        """
        self.deaths = 0
        self.ice_btns = list()
        self.field.width = max(int(self.CBWidth.currentText()), int(self.CBHeight.currentText()))
        self.field.height = min(int(self.CBWidth.currentText()), int(self.CBHeight.currentText()))
        self.field.field = ice_random.generate_random_path(self.field.height, self.field.width)
        self.field.knowledge = self.SpinPercent.value()
        for i in reversed(range(self.GBField.layout().count())):
            self.GBField.layout().takeAt(i).widget().setParent(None)
        btn_width = self.GBField.width()//self.field.width - 20
        btn_height = self.GBField.height()//int(1.5*self.field.height) - 20
        for y in range(self.field.height):
            self.ice_btns.append(list())
            for x in range(self.field.width):
                btn: QtWidgets.QPushButton = QtWidgets.QPushButton()
                self.GBField.layout().addWidget(btn, 2*y + x, x, 2, 1)
                btn.setObjectName("BtnIce%i_%i" % (x, y))
                btn.setIcon(QtGui.QIcon(':/ice_icon/ice.png'))
                btn.setIconSize(QtCore.QSize(btn_width-3, btn_height-3))
                btn.setEnabled(False)
                self.ice_btns[y].append(btn)
                btn.clicked.connect(self.ice_button_clicked)
        self.ice_btns[0][0].setEnabled(True)
        self.ice_btns[0][1].setEnabled(True)
        self.ice_btns[1][0].setEnabled(True)
        self.ice_btns[0][0].setStyleSheet("background-color:cyan")
        self.ice_btns[self.field.height - 1][self.field.width - 1].setStyleSheet("background-color:cyan")
        self.ice_btns[self.field.height - 1][self.field.width - 1].setEnabled(True)
        self.statusbar.clearMessage()

    def ice_button_clicked(self):
        # noinspection PyTypeChecker
        btn: QtWidgets.QPushButton = self.sender()
        current_y = 0
        current_x = 0
        for y in range(self.field.height):
            if btn in self.ice_btns[y]:
                current_y = y
                current_x = self.ice_btns[y].index(btn)
        if current_y == self.field.height - 1 and current_x == self.field.width - 1:
            self.statusbar.showMessage("Переход через ледяное поле завершен. В вашем отряде погибло эльфов: %i"
                                       % self.deaths)

        if self.field.field[current_y][current_x] == 0:
            btn.setStyleSheet("background-color:red")
            self.deaths += 1
        else:
            btn.setStyleSheet("background-color:cyan")
            if current_x < self.field.width-1:
                self.ice_btns[current_y][current_x+1].setEnabled(True)
                self.roll_dice(current_x+1, current_y)
            if current_y < self.field.height-1:
                self.ice_btns[current_y + 1][current_x].setEnabled(True)
                self.roll_dice(current_x, current_y+1)
            if current_x < self.field.width-1 and current_y > 0:
                self.ice_btns[current_y - 1][current_x + 1].setEnabled(True)
                self.roll_dice(current_x+1, current_y - 1)
            if current_x  > 0 and current_y < self.field.height - 1:
                self.ice_btns[current_y + 1][current_x - 1].setEnabled(True)
                self.roll_dice(current_x - 1, current_y + 1)
            if current_x > 0 and current_y < self.field.height:
                self.ice_btns[current_y][current_x - 1].setEnabled(True)
                self.roll_dice(current_x - 1, current_y)
            if current_x < self.field.width and current_y > 0:
                self.ice_btns[current_y - 1][current_x].setEnabled(True)
                self.roll_dice(current_x, current_y - 1)

    def roll_dice(self, current_x, current_y):
        chance = random.random() * 100
        print(chance)
        if chance < self.field.knowledge:
            if self.field.field[current_y][current_x] == 0:
                self.ice_btns[current_y][current_x].setStyleSheet(
                    "border-style:outset;border-width:2px;border-color:red")
            else:
                self.ice_btns[current_y][current_x].setStyleSheet(
                    "border-style:outset;border-width:2px;border-color:blue")


def initiate_exception_logging():
    # generating our hook
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook

    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        logger.exception(f"{exctype}, {value}, {traceback}")
        # Call the normal Exception hook after
        # noinspection PyProtectedMember
        sys._excepthook(exctype, value, traceback)
        # sys.exit(1)
    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook


@logger.catch
def main():
    initiate_exception_logging()
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = IceField()  # Создаём объект класса
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
