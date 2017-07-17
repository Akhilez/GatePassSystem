#!/usr/bin/env python3
import cgi
import sqlite3
path="/var/www/html/html/gatepass.db"
con=sqlite3.connect(path)
cur=con.cursor()
try:
    #cur.execute("drop table stud;")
    #cur.execute("create table stud(name varchar,id int primary key,dob varchar,year int,branch varchar,mob int,email varchar,fatname varchar,fatmob int,fatemail varchar,gen varchar);")
    def insert():
        global n,n1,n2,n3,n4,n5,n6,n7,n8,n9,n0
        print("Inserted")
        cur.execute("insert into studetails values(?,?,?,?,?,?,?,?,?,?,?)",(n1,n,n7,n5,n8,n3,n4,n11,n6,n2,n0))
        con.commit()

    form=cgi.FieldStorage()
    print("Content-type:text/html\r\n\r\n")
    print()
    import cgitb; cgitb.enable()
    htmlFormat="""<html><head><title> Student Registration</title>
    <link rel="stylesheet" type="text/css" href="index.css" /></head>
    <body>
    <div id="container">
        <div id="header">KMIT Student Registration</div>
    <div id="content">
    <div id="nav">
<div id="navItem1">
					<a href="http://127.0.0.1/html/adhm.py">Home</a>
				</div>
				<div id="navItem2">
					<a href="adstureg.py">Register New Student</a>
				</div>
				<div id="navItem3">
					<a href="adrecreg.py">Register New Receptionist</a>
				</div>
				<div id="navItem4">
					<a href="prelogin.py">Log Out</a>
				</div>
    </div>
    <div id="main" align="center">
    <form></br>
    <table><tr><td>
     Name:</td><td><input id="name" name="name" required value="0" autofocus></input></td></tr>
     <tr><td>Hall Ticket No:</td><td><input type="text" name="id" required value='0' ></input></td></tr>
     <tr><td>Gender:</td><td><input type="radio" name="gen" value='Male' >Male<input type="radio" name="gen" value='female' >Female
     <tr><td>Date of Birth:</td><td><input type="text" name="dob" value='0' ></input></td></tr>
     <tr><td>Year:</td><td><input type="radio" name="year" required value='1' >1<input type="radio" name="year" value='2' >2<input type="radio" name="year" value='3' >3<input type="radio" name="year" value='4' >4</td></tr>
     <tr><td>Branch:</td><td><input type="radio" name="branch" required value='CSE' >CSE<input type="radio" name="branch" value='ECE' >ECE<input type="radio" name="branch" value='IT' >IT<input type="radio" name="branch" value='EIE' >EIE</td></tr>
     <tr><td>Section:</td><td><input type="text" name="sec" required></ input></tr>
     <tr><td>Mobile No:</td><td><input type="text" name="mob" required maxlength=10></td></tr>
     <tr><td>Email:</td><td><input type="email" name="email" required></td></tr>
     <tr><td>Father Name:</td><td><input type="text" name="fatname" required></td></tr>
     <tr><td>Father Mobile:</td><td><input type="text" name="fatmob" required maxlength=10></td></tr>
     <tr><td>Father Email:</td><td><input type="email" name="fatemail" ></td></tr></table>
 
   <input type="submit" name="save" value="Submit" > </input><br></form>
   
 </div>
 <hr/>
</div>
</div>
</div>
<div id="footer">
			<p>Copyright@ CSE-D 2015</p>
		</div>
    </body>
    </html>"""

    n=str(form.getvalue("name",0))
    n1=str(form.getvalue("id",0))
    n2=str(form.getvalue("dob",0))
    n3=int(form.getvalue("year",0))
    n0=str(form.getvalue("gen",0))
    n4=str(form.getvalue("branch",0))
    n5=int(form.getvalue("mob",0))
    n6=str(form.getvalue("email",0))
    n7=str(form.getvalue("fatname",0))
    n8=int(form.getvalue("fatmob",0))
    n9=str(form.getvalue("fatemail",0))
    n11=str(form.getvalue("sec"))


    if "save" in form:
        insert()

    print(htmlFormat.format(**locals()))
except Exception as e:
    print(e)
