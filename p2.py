#!/usr/bin/env python3
import cgi
import sqlite3
path="/var/www/html/stud.db"
con=sqlite3.connect(path)
cur=con.cursor()
#cur.execute("drop table students;")
#cur.execute("create table students (name varchar,id int primary key,m1 float,m2 float,m3 float);")
def inmarks():
    print("Marks have been registered")
    cur.execute("insert into students values(?,?,?,?,?)",(n,n1,n2,n3,n4))
    con.commit()
form=cgi.FieldStorage()
print("Content-type:text/html\r\n\r\n")
htmlFormat="""<html><title> The Time Now</title>
    <?name=akhil&num2=01&m1=90&m2=80&m3=0&save=savebody >
    <div align="center" width="30%" style="font-size:25px;border:1px solid black">
    <form style="background-color:lightgrey">
    Name:<input type="text" name="name" value='0' ></input><br>
 id:<input type="text" name="id" value='0' ></input><hr>
 <div id="buttons" style="background-color:lightgreen;padding:30px" >
   marks1:<input type="text" name="m1" value="0" > </input><br>
   marks2:<input type="text" name="m2" value="0"> </input><br>
   marks3:<input type="text" name="m3" value="0" > </input><br>
   <input type="submit" name="save" value="save" > </input><br>
   <a href="http://127.0.0.1/p3.py">Click this</a>
 </div>
 <hr/>
</div>
    </body>
    </html>"""

n=str(form.getvalue("name",0))
n1=int(form.getvalue("id",0))
n2=int(form.getvalue("m1",0))
n3=int(form.getvalue("m2",0))
n4=int(form.getvalue("m3",0))


if "save" in form:
    inmarks()

print(htmlFormat.format(**locals()))
