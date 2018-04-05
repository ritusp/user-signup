from flask import Flask, request, redirect, render_template
import os
import cgi 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("signup.html")

@app.route("/welcome")
def welcome():
    username=request.form["username"]
    return render_template("welcome_page.html")

@app.route('/signup', methods = ["POST"])
def signup():
    username=str.strip(request.form["username"])
    password=str.strip(request.form["password"])
    verify=str.strip(request.form["verify"])
    email=str.strip(request.form["email"])

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    
    error = False
   
    if len(username) == 0:
        username_error = 'User Name cannot be left blank'
      #  username=''
        error = True
    elif len(username) < 3 or len(username) > 20:
        username_error = 'User Name should be atleast from 4 characters to 20 characters long'
       # username  =''
        error = True
    elif username.find(' ') != -1:
        username_error = "No spaces are allowed"
        #username = ''
        error = True

    if len(password) == 0:
        password_error = 'Password cannot be left blank'
        password=''
        error = True
    elif password.find(' ') != -1:
        password_error = "No spaces are allowed"
        error = True
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Password should be atleast from 4 characters to 20 characters long'
        password  =''
        error = True
    

    if len(verify) == 0:
        verify_error = 'Verify Password cannot be left blank'
        verify=''
        error = True
    elif verify.find(' ') != -1:
        verify_error = "No spaces are allowed"
        error = True
    elif len(verify) < 3 or len(verify) > 20:
        verify_error = 'Verify Password should be atleast from 4 characters to 20 characters long'
        verify  =''
        error = True
    elif password != verify:
        verify_error = "User's Password and Verify passward do not match"
        verify = ''
        error = True

    if email != "":
        if not (email.count('.') == 1 and email.count('@') ==1 and email.find(' ') == -1 and len(email) > 3 and len(email) < 20):
            email_error = 'Not a valid email address! Email should have single @, single ., no spaces and is between 3 and 20 characters long'
        #email = ''
            error = True
    if error:
        return render_template('signup.html', username_error=username_error, 
                            password_error=password_error,verify_error=verify_error,
                            email_error=email_error, username=username,
                            email=email)
    else: 
        return render_template('welcome_page.html', username=username)


app.run()