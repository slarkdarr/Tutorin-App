import pytest
from loginModule import searchData,validate
import mysql.connector as mysql


def test_passVerification1():
    assert(validate('hajidadang', 'admin') == 1) # validation success

def test_passVerification2():
    assert(validate('budianakbaik', 'helofren123') == 0) # wrong password

def test_passVerification3():
    assert(validate('rplasik', 'yaudahiya') == 0) # data not in database

def test_checkData1():
    assert(searchData("hartatahta") == 1) # data is not in database, sign up success

def test_checkData2():
    assert(searchData("admin") == 0) # data is in database, sign up failed
