import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QMessageBox

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.__nameLine = QtWidgets.QLineEdit(self)
        self.__addressText = QtWidgets.QTextEdit(self)
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.addressLabel = QLabel(self)
        self.addressLabel.setText('Address:')

        self.__add_button = QPushButton("Add")
        self.__submit_button = QPushButton("Submit")
        self.__cancel_button = QPushButton("Cancel")
        self.__old_name, self.__old_address = "", ""
        self.__contacts = dict(zip(self.__old_name, self.__old_address))
        self.__add_button.show()
        self.__submit_button.hide()
        self.__cancel_button.hide()

        self.__nameLine.setReadOnly(True)
        self.__addressText.setReadOnly(True)

        self.__add_button.clicked.connect(self.addContact)
        self.__submit_button.clicked.connect(self.submitContact)
        self.__cancel_button.clicked.connect(self.cancel)

        self.main_layout = QGridLayout()

        self.button_layout1 = QtWidgets.QVBoxLayout()
        self.button_layout1.addWidget(self.__add_button)
        self.button_layout1.addWidget(self.__submit_button)
        self.button_layout1.addWidget(self.__cancel_button)
        self.button_layout1.addStretch()

        self.main_layout.addWidget(self.nameLabel, 0, 0)
        self.main_layout.addWidget(self.__nameLine, 0, 1)
        self.main_layout.addWidget(self.addressLabel, 1, 0)
        self.main_layout.addWidget(self.__addressText, 1, 1)
        self.main_layout.addLayout(self.button_layout1, 1, 2)
        self.setLayout(self.main_layout)

    @QtCore.Slot()
    def addContact(self):
        __old_name = self.__nameLine.text()
        __old_address = self.__addressText.toPlainText()
        self.__nameLine.clear()
        self.__addressText.clear()
        self.__nameLine.setReadOnly(False)
        self.__nameLine.setFocus()
        self.__addressText.setReadOnly(False)
        self.__add_button.setEnabled(False)
        self.__submit_button.show()
        self.__cancel_button.show()
    def submitContact(self):
        name = self.__nameLine.text()
        address = self.__addressText.toPlainText()
        if (not name or not address):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Empty field! Please enter a name and address.")
            msg.exec()
        if not name in self.__contacts:
            self.__contacts[name] = address
            msg = QMessageBox()
            msg.setText("Contact has been added to your address book.")
            msg.exec()
        if not self.__contacts:
            self.__nameLine.clear()
            self.__addressText.clear()
        self.__nameLine.setReadOnly(True)
        self.__addressText.setReadOnly(True)
        self.__add_button.setEnabled(True)
        self.__submit_button.hide()
        self.__cancel_button.hide()
        print(self.__contacts)
    def cancel(self):
        self.__nameLine.setText(self.__old_name)
        self.__nameLine.setReadOnly(True)

        self.__addressText.setText(self.__old_address)
        self.__addressText.setReadOnly(True)

        self.__add_button.setEnabled(True)
        self.__submit_button.hide()
        self.__cancel_button.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
