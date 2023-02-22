import sqlite3

connection = sqlite3.connect("regTable.db")

cursor = connection.cursor()

sqlcommand = """CREATE TABLE reg(
id integer primary key AUTOINCREMENT,
name varchar(20),
email varchar(20),
phone integer(12),
password varchar(20)
);"""

cursor.execute(sqlcommand)

connection.commit()

connection.close()

import re
connection = sqlite3.connect("regTable.db")
cursor = connection.cursor()

def verifyandinput_name(name):
  name_reg = re.compile("^[a-zA-Z]+$")
  name_match = name_reg.match(name)
  if name_match==None:
    return "not_matched"
  else:
    return "matched"
def verifyandinput_phone(phone):
  phone_reg = re.compile("[0-9]{10}")
  phone_match = phone_reg.match(phone)
  if phone_match!=None:
    return "matched"
  else:
    return "not_matched"
def verifyandinput_email(email):
  email_reg = re.compile("[a-z 0-9 A-Z]*@gmail.com$")
  email_match = email_reg.match(email)
  if email_match!=None:
    return "matched"
  else:
    return "not_matched"

def verifyandinput_password(password):
  password_reg = re.compile("\w{8}")
  password_match = password_reg.match(password) 
  if password_match!=None:
    return "matched"
  else:
    return "not_matched"


def new_reg():
  i = 0
  while True:
    if i ==1 :
      break
    print("Hello!!!\n WELLCOME To new registration portal")
    print("The following details are required Name,email,phone and password ")
    print()
    print("Name")
    name = input("enter your name ")
    namever = verifyandinput_name(name)
    print()
    if namever != "matched":
      print("Didn't matched the requirement")
      continue
    print("email")
    email = input("enter your email ")
    emailver = verifyandinput_email(email)
    print()
    if emailver != "matched":
      print("Didn't matched the requirement")
      continue
    print("phone")
    phone = input("enter your phone ")
    phonever = verifyandinput_phone(phone)
    print()
    if phonever != "matched":
      print("Didn't matched the requirement")
      continue
    print("password")
    print("lenth should be of min 8 char")
    password = input("enter your passoword ")
    passwordver = verifyandinput_password(password)
    print()
    if passwordver != "matched":
      print("Didn't matched the requirement")
      continue
    else:
      l = [name,email,phone,password]
      sqlcommand = """insert into reg(name,email,phone,password) values(?,?,?,?)"""
      cursor.execute(sqlcommand,l)
      connection.commit()
      del l
      i=1
      return 1

def login():
  i = 0
  while True:
    if i ==1 :
      break
    print("Hello!!!\n WELLCOME To login portal")
    print("The following details are required Name,email,phone and password ")
    print()
    email = input("enter your email ")
    emailver = verifyandinput_email(email)
    print()
    if emailver != "matched":
      print("Didn't matched the requirement")
      continue
    print("phone")
    phone = input("enter your phone ")
    phonever = verifyandinput_phone(phone)
    print()
    if phonever != "matched":
      print("Didn't matched the requirement")
      continue
    print("password")
    print("lenth should be of min 8 char")
    password = input("enter your passoword ")
    passwordver = verifyandinput_password(password)
    print()
    if passwordver != "matched":
      print("Didn't matched the requirement")
      continue
    else:
      l = [email,phone,password]
      cursor.execute("select * from reg Where email= (?) and phone = (?) and password= (?)",l)
      a = cursor.fetchall()
      print(a)
      if len(a) != 0 :
        print(f"{a[0][1]} have been logged in")
        del l
        i =1
        return a
      else :
        continue


def update_reg():
  print("Wellcome to Updating Portal")
  a = login()
  i = 0
  while True:
    if i ==1 :
      break
    if len(a)!= 0 :
      print()
      i +=1
      print()
      print("Updating Values")
      print()
      print("email")
      email = input("enter your email ")
      emailver = verifyandinput_email(email)
      print()
      if emailver != "matched":
        print("Didn't matched the requirement")
        continue
      print("phone")
      phone = input("enter your phone ")
      phonever = verifyandinput_phone(phone)
      print()
      if phonever != "matched":
        print("Didn't matched the requirement")
        continue
      print("password")
      print("lenth should be of min 8 char")
      password = input("enter your passoword ")
      passwordver = verifyandinput_password(password)
      print()
      if passwordver != "matched":
        print("Didn't matched the requirement")
        continue
      else:
        l = [email,phone,password,a[0][0]]
        cursor.execute("update reg set email= (?),phone=(?),password=(?) Where id=(?);",l)
        connection.commit()
        del l
        print("done")
        i=1
        return 1
    else:
      continue

i=0  
while True:
  print("Welcome to Sakib's portal")
  print()
  print("Press 1:New registration")
  print("Press 2:Login")
  print("Press 3:Update Informations")
  print("Press 0:Exit")
  print()
  user_input= input("Enter your choice ")
  if user_input == "1":
    new_reg()
  elif user_input=="2":
    login()
  elif user_input=="3":
    update_reg()
  elif user_input=="0":
    break
  else:
    print("Invalid entry")
    print()
    continue
