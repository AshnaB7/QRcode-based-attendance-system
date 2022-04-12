import time
import getpass
from tqdm.auto import tqdm
import sqlite3
import pyzbar.pyzbar as pyzbar
import pyqrcode
import cv2
import os
import numpy
import colorama
from colorama import Back, Style
colorama.init(autoreset=True)


#------CreateDatabaseForeEmployee------------------
def database():
	conn = sqlite3.connect('EmployeeDatabase.db')
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS all_record(employee_name TEXT, employee_id TEXT, employee_contact, employee_department TEXT)")
	conn.commit()
	conn.close()
database()


#-------MainPage----------------------------
def markattendance():
	print("+------------------------------+")
	print("|  1- Mark Attendance          |")
	print("|  2- Admin Login              |")
	print("+------------------------------+")
	user_input2 = input("")
	if user_input2== '1':
		scan()
	if user_input2 == '2':
		login()
markattendance()
