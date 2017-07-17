#!/usr/bin/env python3
import cgi
import sqlite3
path='/var/www/html/test0.db'
con=sqlite3.connect(path)
cur=con.cursor()
cur.execute("drop table emp")
cur.execute("create table emp(eid int PRIMARY KEY,ename varchar(20))")
form=cgi.FieldStorage()
print("Content-type:text/html\r\n\r\n")
htmlFormat="""<html><title> The Time Now</title>
    <body>
    <form method='POST'>
    Employee ID:<input type="text" name="num1" ><br>
    Employee Name:<input type="text" name="num2" ><br>
    <input type="submit" value="Enter"/><br>
    <p>Employee Details {data} </p></form></body>
    </html>"""
num11=form.getvalue("num1",'0')
num22=form.getvalue("num2",'0')
n1=int(num11)
n2=str(num22)
cur.execute("insert into emp values(?,?)",(n1,n2))
cur.execute("select *from emp")
data=cur.fetchall()
con.commit()
con.close()
print(htmlFormat.format(**locals()))

