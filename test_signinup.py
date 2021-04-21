import pytest
from loginModule import *
import mysql.connector as mysql


def test_passVerification():
    assert(validate('hajidadang', 'admin') == 1)