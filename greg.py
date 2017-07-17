#!/usr/bin/env python3
import cgi
import sqlite3
path="/var/www/html/html/gatepass.db"
con=sqlite3.connect(path)
cur=con.cursor()
form=cgi.FieldStorage()
print("Content-type:text/html\r\n\r\n")
print()
import cgitb; cgitb.enable()
try:
    #cur.execute("drop table staff")
    #cur.execute("create table staff(name varchar,mob int,email varchar primary key,gender varchar,dob varchar,password varchar,role varchar)");
    def insert():
        global n,n1,n2,n3,n4,n5,n6;
        print("Inserted")
        cur.execute("insert into staff values(?,?,?,?,?,?,?)",(n,n1,n2,n3,n4,n5,n6))
        con.commit()
        
    htmlFormat="""<html><title>KMIT REGISTRATION</title><head>
     <div id="header">
			<h1>Keshav Memorial Institute of Technology</h1>
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
		
    <link rel="stylesheet" type="text/css" href="index.css" /></head>
     <div id="content">
     <div id="form1" align="center">
    <form>
    <div id="heading"><h3 align="center">Guard Registration<h2></div><br>
    <table><tr><td>
    Name:*</td><td><input type="text" name="name" required ></input><br></td></tr>
    <tr><td>Mobile Number:*</td><td><input type="text" name="mob" required maxlength=10 ></input></td></tr>
    <tr><td>Email Id:*</td><td><input type="email" name="email" required></input></td></tr>
    <tr><td>Gender:</td><td><input type="radio" name="gen" value="Male">Male</input>
                            <input type="radio" name="gen" value="Female">Female</input></td></tr>
    <tr><td>Date of Birth:</td><td><input type="text" name="dob" placeholder="yyyy-mm-dd" ></input></td></tr>
    <tr><td>Password:*</td><td><input type="password" name="psd" required></input></td></tr>
    </table>
    
    <input type="submit" name="submit1" value="submit" > </input><br>
 </div>

    </div></div><hr/>
    <div><marquee>Note:Fields with * are Mandatory</marquee></div>
    <div id="footer">
			<p>Copyright@ CSE-D 2015</p>
		</div>
    </body>
    </html>"""
    n=str(form.getvalue("name",0))
    n1=int(form.getvalue("mob",0))
    n2=str(form.getvalue("email",0))
    n3=str(form.getvalue("gen",0))
    n4=str(form.getvalue("dob",0))
    n5=str(form.getvalue("psd",0))
    n6="guard"
    if "submit1" in form:
        insert()
    print(htmlFormat.format(**locals()))
except Exception as e:
    print(e)
