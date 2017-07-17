#!/usr/bin/env python3
import cgi
import sqlite3
con=sqlite3.connect("/var/www/html/html/gatepass.db")
cur=con.cursor()
form=cgi.FieldStorage()
print("Content-type:text/html\r\n\r\n")
import cgitb; cgitb.enable()
try:
    f=open("yearWise.html","r")
    html=f.read()
    f.close()
    a1=a2=a3=a4=0
    if "submitYear" in form:
        year=str(form.getvalue("year"))
        temp='select count(id) from passes where year='+str(year)+' group by branch'
        cur.execute(temp)
        temp=cur.fetchall()
        print(temp)
        for i in temp:
            a1=i[0]
            a2=i[1]
            a3=i[2]
            a4=i[3]
        
finally:
    print(html.format(**locals()))
