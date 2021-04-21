import pytest
import mysql.connector as mysql
from pembayaran import *
from pemesanan import *

def test_orderConfirmation():
	order = True
	assert(testingPemesanan(order), True)	# Testing Konfirmasi Pemesanan

def test_orderCancelation():
	order = False
	assert(testingPemesanan(order), False)	# Testing Pembatalan Pemesanan

def test_confirmationPembayaran():
	confirmation = True
	assert(testingPembayaran(confirmation), True)	# Testing Konfirmasi Pembayaran

def test_cancelationPembayaran():
	confirmation = False
	assert(testingPembayaran(confirmation), False)	# Testing Pembatalan Pembayaran

def test_insertToPemesanan1():			# Testing Insert to Database Pemesanan
	assert(insertPemesanan(39208329, 92018527, 48290129, "Rudi", "Matematika", "SMA", "Tingkat 3", "Jum'at"), True)

def test_insertToPemesanan2():			# Testing Insert to Database Pemesanan (but duplicate data(double OrderID))
	assert(insertPemesanan(12345678, 12345678, 12345678, "XXX", "XXX", "XXX", "XXX", "XXX"), False)

def test_insertToPembayaran1():			# Testing Insert to Database Pembayaran
	assert(insertFormPembayaran(39208329, 92018527, 48290129, 92018372, "2021-10-19 00:59:33.870541", 100000, False), True)

def test_insertToPembayaran2():			# Testing Insert to Database Pembayaran (but duplicate data(double OrderID))
	assert(insertFormPembayaran(12345678, 12345678, 12345678, 12345678, "2021-10-21 22:10:33.870541", 0, True), False)
