from Server.server_gui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pytest
# @pytest.fixture
# def app(qtbot):
#      test_server_gui=Ui_Form()
#      qtbot.addWidget(test_server_gui)
#      return test_server_gui

def test_button_meintenance_otpion(qtbot):
    form = QtWidgets.QWidget()
    app = Ui_Form()
    app.setupUi(form)
    qtbot.addWidget(form)
    qtbot.mouseClick(app.pushButton,Qt.LeftButton)
    assert app.label_4.text()=="Server Port: "

def test_button_set_path(qtbot):
    form = QtWidgets.QWidget()
    app = Ui_Form()
    app.setupUi(form)
    qtbot.addWidget(form)
    qtbot.mouseClick(app.pushButton,Qt.LeftButton)
    assert app.label_3.text()=="Server Adress: localhost:"

def test_button_run(qtbot):
    form = QtWidgets.QWidget()
    window = Ui_Form()
    window.setupUi(form)
    qtbot.addWidget(form)
    qtbot.mouseClick(window.pushButton_4, Qt.LeftButton)
    assert window.label_2.text() == "Server Status: running"