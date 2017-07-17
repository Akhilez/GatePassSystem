#!/usr/bin/env python3
import cgi
import sqlite3
path="/var/www/html/stud.db"
con=sqlite3.connect(path)
cur=con.cursor()
form=cgi.FieldStorage()
colors=form.getlist("color")

print("Content-type:text/html\r\n\r\n")
html="""<html><title> The Time Now</title><body>
    <div align="center" width="30%
    " style="font-size:25px;border:1px solid black">
    <form method="get" action="p3.py" style="background-color:lightgrey">
    <input type="submit" value="submit"></input>
    </form>
  
 <div id="buttons" style="background-color:lightgreen;padding:30px" >
   
     
 </div>
 <hr/>
</div>
    </body>
    </html>"""

html1="""<html><title> The Time Now</title><body>
    <div align="center" width="30%
    " style="font-size:25px;border:1px solid black">
    <form method="get" style="background-color:lightgrey">
    <input type="text" name="color" value="red"></input><br>
    <input type="text" name="color" value="green"></input><br>
    <input type="submit" value="submit"></input>
    </form>
  
 <div id="buttons" style="background-color:lightgreen;padding:30px" >
   
     
 </div>
 <hr/>
</div>
    </body>
    </html>"""
print(html1)
lst=[]
i=0
for color in colors:
    lst.append(color)
    print(lst[i])
    if(lst[i]=="green"):
        html1=html
        print("Enter submit button to go to new file")
        print(html1)
    i=i+1

