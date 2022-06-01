import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="SBME2024"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE sbme2024");


#CREATE TABLE Doctor (id INT, Password VARCHAR(255), Fname VARCHAR(255), Lname VARCHAR(255), Email VARCHAR(255), phonenumber INT, PRIMARY KEY(id))
#CREATE TABLE Employee (id INT, Password VARCHAR(255), Fname VARCHAR(255), Lname VARCHAR(255), Email VARCHAR(255), Phonenumber INT, PRIMARY KEY(id))
#CREATE TABLE Patient (name VARCHAR(255), Email VARCHAR(255), phonenumber INT, PRIMARY KEY(Email))
#CREATE TABLE Devices (dcode INT, supervisor VARCHAR(255), company VARCHAR(255), w_state VARCHAR(255), m_state VARCHAR(255), PRIMARY KEY(dcode))