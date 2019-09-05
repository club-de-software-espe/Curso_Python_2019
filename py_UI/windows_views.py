import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from models import *
from PyQt5 import uic


class WindowMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('window_main.ui', self)
        self.users_group = UsersGroup()
        self.btn_save.clicked.connect(self.save_user)
        self.btn_delete.clicked.connect(self.delete_user)
        self.btn_search.clicked.connect(self.search_user)
        # self.cmb_gender.addItems([str(i) for i in range(8)])
        # self.btn_save.setStyleSheet('color:red;background:blue')

    def closeEvent(self, event):
        confirmation = QMessageBox.question(
            self, 'Salir', 'Esta seguro de salir de la aplicacion',
            QMessageBox.Yes | QMessageBox.No)

        if confirmation == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def moveEvent(self, event):
        pos_x = str(event.pos().x())
        pos_y = str(event.pos().y())
        print('PosX: {}\tPosY: {}'.format(pos_x, pos_y))

    def save_user(self):
        ci = self.txt_ci.text()
        name = self.txt_name.text()
        gender = self.cmb_gender.currentText()
        user = User(ci=ci, name=name, gender=gender)
        self.users_group.add(user, update=True)
        QMessageBox.information(
            self, 'Guardado con éxito', user.__repr__(),
            QMessageBox.Ok)
        self.txt_ci.clear()
        self.txt_name.clear()
        self.cmb_gender.setCurrentIndex(0)

    def search_user(self):
        ci = self.txt_search.text()
        result = self.users_group.search(ci)
        if result:
            QMessageBox.information(self, 'Usuario encontrado', result,
                                    QMessageBox.Ok)
            self.txt_search.clear()
        else:
            QMessageBox.critical(self, 'Usuario no encontrado',
                                 'No se han encontrado coincidencias',
                                 QMessageBox.Ok)

    def delete_user(self):
        ci = self.txt_ci.text()
        result = self.users_group.delete(ci)
        if result:
            QMessageBox.information(self, 'Usuario eliminado',
                                    'El usuario se eliminó del registro',
                                    QMessageBox.Ok)
        else:
            QMessageBox.critical(self, 'Error al eliminar',
                                 'No se encontró al usuario que desea \
                                    eliminar',
                                 QMessageBox.Ok)
        self.txt_ci.clear()


class WindowSecundary(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
