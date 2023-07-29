import sys
import time

from PyQt5.QtWidgets import *

"""from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton"""
from PyQt5 import uic, QtWidgets
import webbrowser
import os
import shutil


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.dirlist = ""
        uic.loadUi("file/main_ru.ui", self)
        with open("file/settings.txt", "r") as f:
            self.dirlist = f.readline()
            self.lineEdit.setText(self.dirlist)
        self.pushButton.clicked.connect(self.dirlist_searcher)
        self.pushButton_2.clicked.connect(lambda: webbrowser.open('http://www.google.com'))
        self.pushButton_3.clicked.connect(
            lambda: webbrowser.open('https://github.com/dxx573kwot/Music_modifier_for_BPM'))
        self.Asgard_1.clicked.connect(self.asgard_1)
        self.Asgard_2.clicked.connect(self.asgard_2)
        self.Asgard_Crypts.clicked.connect(self.asgard_Crypts)
        self.Vanaheim_1.clicked.connect(self.vanaheim_1)
        self.Vanaheim_2.clicked.connect(self.vanaheim_2)
        self.Svartalfheim_1.clicked.connect(self.svartalfheim_1)
        self.Svartalfheim_2.clicked.connect(self.svartalfheim_2)
        self.Helheim_1.clicked.connect(self.helheim_1)
        self.Helheim_2.clicked.connect(self.helheim_2)
        self.pushButton_4.clicked.connect(self.loading_trek)
        self.pushButton_5.clicked.connect(self.save_preset)
        self.pushButton_6.clicked.connect(self.loading_preset)
        self.clear.clicked.connect(self.clear_all)
        for i in os.listdir("file/prebilds"):
            self.comboBox.addItem(i)

    def dirlist_searcher(self):
        self.dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        with open("file/settings.txt", "w") as f:
            f.write(self.dirlist)
        self.lineEdit.setText(self.dirlist)
        # self.lineEdit.text()
        # self.label_4.setText("Папка не выбранна")
        print(self.dirlist)

    def click(self):
        pass

    def asgard_1(self):
        self.asgard_1_treck = QFileDialog.getOpenFileName(
            self,
            'Open File', './',
            'Files (*.wav)')
        self.label_7.setText("Выбрано")
        print(1)

    def asgard_2(self):
        self.asgard_2_treck = QFileDialog.getOpenFileName(
            self,
            'Open File', './',
            'Files (*.wav)')
        self.label_8.setText("Выбрано")
        print(2)

    def asgard_Crypts(self):
        self.asgard_Crypts_treck = QFileDialog.getOpenFileName(
            self,
            'Open File', './',
            'Files (*.wav)')
        self.label_9.setText("Выбрано")
        print(3)

    def vanaheim_1(self):
        self.vanaheim_1_treck = QFileDialog.getOpenFileName(
            self,
            'Open File', './',
            'Files (*.wav)')
        self.label_10.setText("Выбрано")
        print(4)

    def vanaheim_2(self):
        self.vanaheim_2_treck = QFileDialog.getOpenFileName(
            self,
            'Open File', './',
            'Files (*.wav)')
        self.label_11.setText("Выбрано")
        print(5)

    def svartalfheim_1(self):
        self.svartalfheim_1_treck = QFileDialog.getOpenFileName(
            self,
            'Open File', './',
            'Files (*.wav)')
        self.label_12.setText("Выбрано")
        print(6)

    def svartalfheim_2(self):
        self.svartalfheim_2_treck = QFileDialog.getOpenFileName(
            self,
            'Open File', './',
            'Files (*.wav)')
        self.label_13.setText("Выбрано")
        print(7)

    def helheim_1(self):
        self.helheim_1_treck = QFileDialog.getOpenFileName(
            self,
            'Open File', './',
            'Files (*.wav)')
        self.label_14.setText("Выбрано")
        print(8)

    def helheim_2(self):
        self.helheim_2_treck = QFileDialog.getOpenFileName(
            self,
            'Open File', './',
            'Files (*.wav)')
        self.label_15.setText("Выбрано")
        print(9)

    def loading_trek(self):
        if self.checkBox.isChecked():
            num_core = int(os.environ['NUMBER_OF_PROCESSORS'])
            print(num_core)

        shutil.rmtree("file/CustomSoundtrack")
        shutil.copytree("file/base/CustomSoundtrack", "file/CustomSoundtrack", dirs_exist_ok=True)
        if self.label_7.text() == "Выбрано":
            shutil.copy(self.asgard_1_treck[0], "file/CustomSoundtrack/Asgard1")
        if self.label_8.text() == "Выбрано":
            shutil.copy(self.asgard_2_treck[0], "file/CustomSoundtrack/Asgard2")
        if self.label_9.text() == "Выбрано":
            shutil.copy(self.asgard_Crypts_treck[0], "file/CustomSoundtrack/AsgardCrypt")
        if self.label_10.text() == "Выбрано":
            shutil.copy(self.vanaheim_1_treck[0], "file/CustomSoundtrack/Vanaheim1")
        if self.label_11.text() == "Выбрано":
            shutil.copy(self.vanaheim_2_treck[0], "file/CustomSoundtrack/Vanaheim2")
        if self.label_12.text() == "Выбрано":
            shutil.copy(self.svartalfheim_1_treck[0], "file/CustomSoundtrack/Svartalfheim1")
        if self.label_13.text() == "Выбрано":
            shutil.copy(self.svartalfheim_2_treck[0], "file/CustomSoundtrack/Svartalfheim2")
        if self.label_14.text() == "Выбрано":
            shutil.copy(self.helheim_1_treck[0], "file/CustomSoundtrack/Helheim1")
        if self.label_15.text() == "Выбрано":
            shutil.copy(self.helheim_2_treck[0], "file/CustomSoundtrack/Helheim2")
        try:
            shutil.rmtree(self.dirlist)
            shutil.copytree("file/CustomSoundtrack", self.dirlist, dirs_exist_ok=True)
        except BaseException as a:
            print(a)

    def save_preset(self):
        try:
            shutil.rmtree(self.dirlist)
        except BaseException:
            pass
        shutil.copytree("file/CustomSoundtrack", f"file/prebilds/{self.lineEdit_2.text()}", dirs_exist_ok=True)

    def loading_preset(self):
        if self.comboBox.currentText() != 0:
            shutil.rmtree(self.dirlist)
            shutil.copytree(f"file/prebilds/{self.comboBox.currentText()}", self.dirlist, dirs_exist_ok=True)

    def clear_all(self):
        self.asgard_1_treck = ""
        self.asgard_2_treck = ""
        self.asgard_Crypts_treck = ""
        self.vanaheim_1_treck = ""
        self.vanaheim_2_treck = ""
        self.svartalfheim_1_treck = ""
        self.svartalfheim_2_treck = ""
        self.helheim_1_treck = ""
        self.helheim_2_treck = ""
        self.label_7.setText("Пусто")
        self.label_8.setText("Пусто")
        self.label_9.setText("Пусто")
        self.label_10.setText("Пусто")
        self.label_11.setText("Пусто")
        self.label_12.setText("Пусто")
        self.label_13.setText("Пусто")
        self.label_14.setText("Пусто")
        self.label_15.setText("Пусто")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())