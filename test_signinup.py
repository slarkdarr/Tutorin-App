import pytest
from loginModule import *
import mysql.connector as mysql


def test_passVerification1():
    assert(validate('hajidadang', 'admin') == 1) # validation success

def test_passVerification2():
    assert(validate('budianakbaik', 'helofren123') == 0) # wrong password

def test_passVerification2():
    assert(validate('rplasik', 'yaudahiya') == 0) # data not in database