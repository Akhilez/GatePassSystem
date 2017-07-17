#!/usr/bin/env python3
import cgi
import sqlite3
con=sqlite3.connect("/var/www/html/html/gatepass.db")
cur=con.cursor()
form=cgi.FieldStorage()
print("Content-type:text/html\r\n\r\n")
import cgitb; cgitb.enable()
try:
    def login():
        global username
        global password
        global htmlFormat
        temp='select password,role from staff where email="'+username+'"'
        cur.execute(temp)
        temp=cur.fetchall()
        if temp==[]:
            print("Invalied email or password")
            return
        if temp[0][0]==password:
                role=temp[0][1]
                if role=="receptionist":
                    #print("login successful")
                    htmlFormat='''<html><body onload ="window.location.href='home.py'"></body></html>'''
                    print(htmlFormat)

                    
                if role=="director":
                    htmlFormat='''<html><body onload="window.location.href='http://127.0.0.1/html/directorHome.py'"></body></html>'''
                if role=="admin":
                    htmlFormat='''<html><body onload ="window.location.href='http://127.0.0.1/html/adhm.py'"></body></html>'''
                if role=="guard":
                    htmlFormat='''<html><body onload = "window.location.href='http://127.0.0.1/html/guardHome.py'"></body></html>'''
                    print(htmlFormat)
        else:
            print("login failed\nTry again")
    htmlFormat="""
    <!DOCTYPE html>
    <html>
    <head>
	<title>Welcome to KMIT gatepass</title>
	<link rel="stylesheet" type="text/css" href="index.css" />
    </head>
    <body>
	<div id="container">
		<div id="header">
		        <img src="kmit.gif" alt="KMIT" width="30%" height="100px" name="kmit_logo"></img>
			<!--<h1>Keshav Memorial Institute of Technology</h1>-->
		</div>
		<div id="nav">
				<div id="navItem1">
					<a href="prelogin.py">Home</a>
				</div>
				<div id="navItem2">
					<a href="signuphome.py">Staff Signup</a>
				</div>
				<div id="navItem3">
					About Us
				</div>
				<div id="navItem4">
					<a href="">Contact Us</a>
				</div>
				</div>
		<div id="content2">
		<div id="login_as">
		<ul><li>Gate Pass is a Web Application developed by Students of KMIT belonging to Second Year First Semester.</li><br><br>
		<li>This Web Application facilitates the College Management to Issue and Monitor the Students who are requesting for Gatepass.</li>
		</ul></div>
			
				
			<div id="main2">
				<h2>GATE PASS</h2><br/><hr/></br>
				<h4>Login into your Account</h4>
			<form method="get" >
    <table align="center">
    <tr><td>Username:</td><td><input type="text" name="username" required placeholder="Email"></input></td></tr>
   <tr><td>Password:</td><td>	<input type="password" name="psd" required placeholder="Password"></input></tr></table></br>
				<input type="submit" name="login" value="Log In" action="127.0.0.1/html/home.py"></input>	
				<input type="submit" name="forgotP" value="Forgot Password" ></input>
                        </form>
			</div>
		</div>
		<div id="footer">
			<p>Copyright@ CSE-D 2015</p>
		</div>
	</div>
    </body>
    </html>"""
    username=str(form.getvalue("username"))
    password=str(form.getvalue("psd"))
    if "forgotP" in form:
        print(html)
        print("clicked forgot password")
    if "login" in form:
        login()
    
#except Exception as e
#    print("Error:",e)
finally:
    print(htmlFormat.format(**locals()))
