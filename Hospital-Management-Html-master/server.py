from flask import Flask, redirect, url_for, request,render_template
import numpy as np
import mysql.connector
from sympy import Id
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="SBME2024"
)


mycursor = mydb.cursor()
app = Flask(__name__,template_folder="templates")




@app.route('/')
def hello_name():
   return render_template('index.html')
   
@app.route('/doctor',methods = ['POST', 'GET'])
def registerdoctor():
   if request.method == 'POST': ##check if there is post data
      Fname = request.form['First Name']
      Lname = request.form['Last Name']
      phonenumber = request.form['Mobile Number']
      Email = request.form['Email Address']
      Password = request.form['Password']
      print(Fname)
      print(Lname)
      print(phonenumber)
      print(Email)
      print(Password)
      sql = "INSERT INTO Doctor (Password,Fname, Lname, Email, phonenumber) VALUES (%s, %s, %s, %s, %s)"
      val = (Password,Fname, Lname, Email, phonenumber)
      mycursor.execute(sql, val)
      mydb.commit() 
      return render_template('eachdoctor.html')
   else:
      return render_template('doctors.html')


@app.route('/about')
def about():
   return render_template('about.html')
@app.route('/appointment')
def appointment():
   return render_template('appointment.html')
@app.route('/cancel')
def cancel():
   return render_template('cancel.html')  
@app.route('/contact')
def contact():
   return render_template('contact.html')
@app.route('/dataofdoctor')
def dataofdoctor():
   return render_template('dataofdoctor.html')
@app.route('/dataofpatient')
def dataofpatient():
   return render_template('dataofpatient.html')
@app.route('/eachdoctor')
def eachdoctor():
   return render_template('eachdoctor.html')
@app.route('/eachpatient')
def eachpatient():
   return render_template('eachpatient.html')
@app.route('/employee')
def employee():
   return render_template('employee.html')
@app.route('/login')
def login():
   return render_template('login.html')
@app.route('/patient')
def patient():
   return render_template('patient.html')
@app.route('/privacy')
def privacy():
   return render_template('privacy.html')
@app.route('/registration')
def registration():
   return render_template('registration.html')
@app.route('/review')
def review():
   return render_template('review.html')
@app.route('/terms')
def terms():
   return render_template('terms.html')




if __name__ == '__main__':
   app.run()
   