import pytest
from akunModule import *

def test_convertCurrency1():
    assert(toCurrency(1000000) == "1.000.000") #testcase 1

def test_convertCurrency2():
    assert(toCurrency(0) == "0") # testcase dasar

def test_convertCurrency3():
    assert(toCurrency(561212937) == "561.212.937") #testcase 2

def test_checkIntegerOrNot():
    assert(isInt("12379a71923") == False) # data is not an integer

def test_checkIntegerOrNot():
    assert(isInt("2837") == True) # data is an integer

