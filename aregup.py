#!/usr/bin/env python3
import cgi
import sqlite3
path="/var/www/html/html/gatepass.db"
con=sqlite3.connect(path)
cur=con.cursor()
import cgitb; cgitb.enable()
form=cgi.FieldStorage()

try:
        def select():
            global m0,m1,m2,m3,m4,n
            cur.execute(a)
            myl=cur.fetchall()
            if(myl==[]):
                    print("No such email ID")
            for i in myl:
                m0=i[0]
                m1=i[1]
                m2=i[2]
                m3=i[3]
                m4=i[4]
            con.commit()
        def up():
            b='update staff set name="'+m0+'" where email = "'+n+'"'
            print(b)
            cur.execute(b)
            con.commit()
        def up0():
            b='update staff set mob="'+m1+'" where email = "'+n+'"'
            print(b)
            cur.execute(b)
            con.commit()
        def up1():
            b='update staff set gender="'+m2+'" where email = "'+n+'"'
            print(b)
            cur.execute(b)
            con.commit()
        def up2():
            b='update staff set dob="'+m3+'" where email = "'+n+'"'
            print(b)
            cur.execute(b)
            con.commit()
        def up3():
            b='update staff set role="'+m4+'" where email = "'+n+'"'
            print(b)
            cur.execute(b)
            con.commit()
        def delete():
            b='delete from staff where email = "'+n+'"'
            print(b)
            cur.execute(b)
            con.commit()
        print("Content-type:text/html\r\n\r\n")

        htmlFormat="""<html><head><title> Student Registration</title>
    <link rel="stylesheet" type="text/css" href="index.css" /></head>
    <body>
    <div id="container">
        <div id="header">KMIT Student Registration</div>
 <div id="nav">
<div id="navItem1">
					<a href="adhm.py">Home</a>
				</div>
				<div id="navItem2">
					<a href="adstureg.py">Register New Student</a>
				</div>
				<div id="navItem3">
					About Us
				</div>
				<div id="navItem4">
					<a href="prelogin.py">Log Out</a>
				</div>
        </div>
        
    <div id="content">
    
    <div id="main" align="center">
    <form></br>
    Enter Email ID : <input type="text" name="id" value={n}></input><br>
             <input type="submit" name="submit1" value="submit" > </input><hr>
    
    Email ID:{n}</br>
     Name:{m0}
     <table>
     <tr><td>Name:</td><td><input type="text" name="name" placeholder="Enter Name to update"></input>
              <input type="submit" name="update" value="update"></input></td></tr>
     <tr><td>Mobile Number:</td><td><input type="text" name="mob" value={m1}></input>
              <input type="submit" name="update0" value="update"></input></td></tr>
     <tr><td>Gender:</td><td><input type="text" name="gen" value={m2} ></input>
               <input type="submit" name="update1" value="update"></input></td></tr>
     <tr><td>Date of Birth:</td><td><input type="text" name="dob" value={m3} ></input>
               <input type="submit" name="update2" value="update"></input></td></tr>
     <tr><td>Role:</td><td><input type="text" name="role" value={m4}></input>
                <input type="submit" name="update3" value="update"></input></td></tr>
             </table>
 
   <input type="submit" name="delete" value="delete" > </input><br></form>
   
 </div>
 
</div>
<hr/>
</div>
</div>
<div id="footer">
			<p>Copyright@ CSE-D 2015</p>
		</div>
    </body>
    </html>"""

        n=str(form.getvalue("id"))
        m0=str(form.getvalue("name"))
        m1=str(form.getvalue("mob"))
        m2=str(form.getvalue("gen"))
        m3=str(form.getvalue("dob"))
        m4=str(form.getvalue("role"))
        a='select name,mob,gender,dob,role from staff where email= "'+n+'"'


        if "submit1" in form:
            select()
        if "update" in form:
            up()
        if "update0" in form:
            up0()
        if "update1" in form:
            up1()
        if "update2" in form:
            up2()
        if "update3" in form:
            up3()
        if "delete" in form:
            delete()
        con.commit()
        print(htmlFormat.format(**locals()))
except Exception as e:
    print(e)




