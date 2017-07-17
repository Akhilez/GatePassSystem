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
            global m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,n
            cur.execute(a)
            myl=cur.fetchall()
            if(myl==[]):
                    print("No such Id")
            for i in myl:
                m0=i[0]
                m8=i[1]
                m6=i[2]
                m9=i[3]
                m3=i[4]
                m4=i[5]
                m5=i[6]
                m7=i[7]
                m2=i[8]
                m1=i[9]
            con.commit()
        def up():
            b='update studetails set name="'+m0+'" where id = "'+n+'"'
            cur.execute(b)
            con.commit()
        def up0():
            b='update studetails set gen="'+m1+'" where id = "'+n+'"'
            cur.execute(b)
            con.commit()
        def up1():
            b='update studetails set dob="'+m2+'" where id = "'+n+'"'
            cur.execute(b)
            con.commit()
        def up2():
            b='update studetails set year="'+m3+'" where id = "'+n+'"'
            cur.execute(b)
            con.commit()
        def up3():
            b='update studetails set branch="'+m4+'" where id = "'+n+'"'
            cur.execute(b)
            con.commit()
        def up4():
            b='update studetails set sec="'+m5+'" where id = "'+n+'"'
            cur.execute(b)
            con.commit()
        def up5():
            b='update studetails set phno="'+m6+'" where id = "'+n+'"'
            cur.execute(b)
            con.commit()
        def up6():
            b='update studetails set email="'+m7+'" where id = "'+n+'"'
            cur.execute(b)
            con.commit()
        def up7():
            b='update studetails set fathersname="'+m8+'" where id = "'+n+'"'
            cur.execute(b)
            con.commit()
        def up8():
            b='update studetails set fathersphno="'+m9+'" where id = "'+n+'"'
            cur.execute(b)
            con.commit()
        def delete():
            b='delete from studetails where id = "'+n+'"'
            cur.execute(b)
            con.commit()
        print("Content-type:text/html\r\n\r\n")

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
					<a href="adstureg.py">Register new Student</a>
				</div>
				<div id="navItem3">
					About Us
				</div>
				<div id="navItem4">
					<a href="prelogin.py">Log Out</a>
				</div>
    </div>
    <div id="main" align="center">
    <form></br>
    Enter ID : <input type="text" name="id" value={n}></input><br>
             <input type="submit" name="submit1" value="submit" > </input><hr>
    
    Hall Ticket No:{n}</br>
    Name:{m0}</br>
    <table>
     <tr><td>
    Name:</td><td><input type="text" name="name" placeholder="Enter Name to Update"></input>
                     <input type="submit" name="update" value="update"></input></td></tr>
     <tr><td>Gender:</td><td><input type="text" name="gen" value={m1}></input>
              <input type="submit" name="update0" value="update"></input></td></tr>
     <tr><td>Date of Birth:</td><td><input type="text" name="dob" value={m2} ></input>
               <input type="submit" name="update1" value="update"></input></td></tr>
     <tr><td>Year:</td><td><input type="text" name="year" value={m3} ></input>
               <input type="submit" name="update2" value="update"></input></td></tr>
     <tr><td>Branch:</td><td><input type="text" name="branch" value={m4}></input>
                <input type="submit" name="update3" value="update"></input></td></tr>
     <tr><td>Section:</td><td><input type="text" name="sec" value={m5}></input>
                 <input type="submit" name="update4" value="update"></input></td></tr>
     <tr><td>Mobile No:</td><td><input type="text" name="mob" value={m6}>
                 <input type="submit" name="update5" value="update"></input></td></tr>
     <tr><td>Email:</td><td><input type="text" name="email" value={m7}>
                 <input type="submit" name="update6" value="update"></input></td></tr>
     <tr><td>Father Name:</td><td>{m8}</br>
     <tr><td>Father Name:</td><td><input type="text" name="fatname" placeholder="Enter Father Name to update">
                  <input type="submit" name="update7" value="update"></input></td></tr>
     <tr><td>Father Mobile:</td><td><input type="text" name="fatmob" value={m9}>
                  <input type="submit" name="update8" value="update"></input></td></tr>
        
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
        m1=str(form.getvalue("gen"))
        m2=str(form.getvalue("dob"))
        m3=str(form.getvalue("year"))
        m4=str(form.getvalue("branch"))
        m5=str(form.getvalue("sec"))
        m6=str(form.getvalue("mob"))
        m7=str(form.getvalue("email"))
        m8=str(form.getvalue("fatname"))
        m9=str(form.getvalue("fatmob"))
        a='select name,fathersname,phno,fathersphno,year,branch,sec,email,dob,gender from studetails where id= "'+n+'"'


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
        if "update4" in form:
            up4()
        if "update5" in form:
            up5()
        if "update6" in form:
            up6()
        if "update7" in form:
            up7()
        if "update8" in form:
            up8()
        if "delete" in form:
            delete()
        con.commit()
        print(htmlFormat.format(**locals()))
except Exception as e:
    print(e)



