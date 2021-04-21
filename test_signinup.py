import pytest
from loginModule import *
import mysql.connector as mysql


def test_passVerification():
    dummyLogin = Login()
    assert(Login.checkDatabase(dummyLogin, 'hajidadang', 'admin') == 1)