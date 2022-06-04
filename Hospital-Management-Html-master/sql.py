import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="aishawaziry1",
  database="SBME2024"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE sbme2024");


#CREATE TABLE Doctor (id INT, Password VARCHAR(255), Fname VARCHAR(255), Lname VARCHAR(255), Email VARCHAR(255), phonenumber INT, PRIMARY KEY(id))
#CREATE TABLE Employee (id INT, Password VARCHAR(255), Fname VARCHAR(255), Lname VARCHAR(255), Email VARCHAR(255), Phonenumber INT, PRIMARY KEY(id))
#CREATE TABLE Patient (name VARCHAR(255), Email VARCHAR(255), phonenumber INT, PRIMARY KEY(Email))
# mycursor.execute("CREATE TABLE Devices (dcode INT, supervisor VARCHAR(255), company VARCHAR(255), w_state VARCHAR(255), m_state VARCHAR(255), PRIMARY KEY(dcode))")
# mycursor.execute("CREATE TABLE booking (date	date,time	time,d_id	INTEGER NOT NULL,p_email	VARCHAR(255) NOT NULL,FOREIGN KEY(p_email) REFERENCES patient(Email),FOREIGN KEY(d_id) REFERENCES doctor(id))")