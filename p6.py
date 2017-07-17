#!/usr/bin/env python3
import cgi
import sqlite3
path="/var/www/html/stud.db"
con=sqlite3.connect(path)
cur=con.cursor()
form=cgi.FieldStorage()

def select(): 
    cur.execute(a)
    myl=cur.fetchall()
    for i in myl:
        n=i[3]
        n2=i[0]
        n3=i[1]
        n4=i[2]
    con.commit()
print("Content-type:text/html\r\n\r\n")
htmlFormat="""<html><title> The Time Now</title><body>

    <form method="get" action="p3.py">
    <input type="submit" value="submit"></input> 

</form>
    </body>
    </html>"""
html1="""
    <html><body>
    <form method="get">
    Password:<input type="text" name="psd"></input><br>
    <input type="submit" value="submit">
    </form></body></html>
"""
p=int(form.getvalue("psd"))
print(html1)
if(p==123):
    html1=html
    print("Enter submit button to go to new file")
    print(html1)
print(html1)

    





