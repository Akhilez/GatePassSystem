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
   name:{n}<br>
   marks1:<input type="text" name="m11" value={n2} > </input>
   <input type="submit" name="update1" value="update"></input><br>
   marks2:<input type="text" name="m22" value={n3}> </input>
   <input type="submit" name="update2" value="update"></input><br>
   marks3:<input type="text" name="m33" value={n4} > </input>
   <input type="submit" name="update3" value="update"></input><br>
   
   <a href="http://127.0.0.1/p3.py">Click this</a>
 </div>
 <hr/>
</div>
</form>
    </body>
    </html>"""
n1=str(form.getvalue("idy","0"))
n=str(form.getvalue("name"))
n2=str(form.getvalue("m11"))
n3=str(form.getvalue("m22"))
n4=str(form.getvalue("m33"))
a="select m1,m2,m3,name from students where id="+n1


def up1():
    b="update students set m1="+n2+" where id = "+n1
    print(b)
    cur.execute(b)
    con.commit()
def up2():
    c="update students set m1="+n3+" where id = "+n1
    cur.execute(c)
    con.commit()
def up3():
    d="update students set m1="+n4+" where id = "+n1
    cur.execute(d)
    con.commit()
if "update1" in form:
    up1()
if "update2" in form:
    up2()
if "update3" in form:
    up3()
    

if "save" in form:
    select()

con.commit()
print(htmlFormat.format(**locals()))     n3=i[1]
        n4=i[2]
    con.commit()
print("Content-type:text/html\r\n\r\n")
htmlFormat="""<html><title> The Time Now</title><body>
    <div align="center" width="30%
    " style="font-size:25px;border:1px solid black">
    <form style="background-color:lightgrey">
    
    Enter your ID : <input type="text" name="idy" value={n1} ></input><br>
 <input type="submit" name="save" value="save" > </input><hr>
 <div id="buttons" style="background-color:lightgreen;padding:30px" >
   
   id:{n1}<br>
   name:{n}<br>
   marks1:<input type="text" name="m11" value={n2} > </input>
   <input type="submit" name="update1" value="update"></input><br>
   marks2:<input type="text" name="m22" value={n3}> </input>
   <input type="submit" name="update2" value="update"></input><br>
   marks3:<input type="text" name="m33" value={n4} > </input>
   <input type="submit" name="update3" value="update"></input><br>
   
   <a href="http://127.0.0.1/p3.py">Click this</a>
 </div>
 <hr/>
</div>
</form>
    </body>
    </html>"""
n1=str(form.getvalue("idy","0"))
n=str(form.getvalue("name"))
n2=str(form.getvalue("m11"))
n3=str(form.getvalue("m22"))
n4=str(form.getvalue("m33"))
a="select m1,m2,m3,name from students where id="+n1


def up1():
    b="update students set m1="+n2+" where id = "+n1
    print(b)
    cur.execute(b)
    con.commit()
def up2():
    c="update students set m1="+n3+" where id = "+n1
    cur.execute(c)
    con.commit()
def up3():
    d="update students set m1="+n4+" where id = "+n1
    cur.execute(d)
    con.commit()
if "update1" in form:
    up1()
if "update2" in form:
    up2()
if "update3" in form:
    up3()
    

if "save" in form:
    select()

con.commit()
print(htmlFormat.format(**locals())) global n
    global n2
    global n3
    global n4
    for i in myl:
        n=i[3]
        n2=i[0]
   name:{n}<br>
   marks1:<input type="text" name="m11" value={n2} > </input>
   <input type="submit" name="update1" value="update"></input><br>
   marks2:<input type="text" name="m22" value={n3}> </input>
   <input type="submit" name="update2" value="update"></input><br>
   marks3:<input type="text" name="m33" value={n4} > </input>
   <input type="submit" name="update3" value="update"></input><br>
   
   <a href="http://127.0.0.1/p3.py">Click this</a>
 </div>
 <hr/>
</div>
</form>
    </body>
    </html>"""
n1=str(form.getvalue("idy","0"))
n=str(form.getvalue("name"))
n2=str(form.getvalue("m11"))
n3=str(form.getvalue("m22"))
n4=str(form.getvalue("m33"))
a="select m1,m2,m3,name from students where id="+n1


def up1():
    b="update students set m1="+n2+" where id = "+n1
    print(b)
    cur.execute(b)
    con.commit()
def up2():
    c="update students set m1="+n3+" where id = "+n1
    cur.execute(c)
    con.commit()
def up3():
    d="update students set m1="+n4+" where id = "+n1
    cur.execute(d)
    con.commit()
if "update1" in form:
    up1()
if "update2" in form:
    up2()
if "update3" in form:
    up3()
    

if "save" in form:
    select()

con.commit()
print(htmlFormat.format(**locals()))     n3=i[1]
        n4=i[2]
    con.commit()
print("Content-type:text/html\r\n\r\n")
htmlFormat="""<html><title> The Time Now</title><body>
    <div align="center" width="30%
    " style="font-size:25px;border:1px solid black">
    <form style="background-color:lightgrey">
    
    Enter your ID : <input type="text" name="idy" value={n1} ></input><br>
 <input type="submit" name="save" value="save" > </input><hr>
 <div id="buttons" style="background-color:lightgreen;padding:30px" >
   
   id:{n1}<br>
   name:{n}<br>
   marks1:<input type="text" name="m11" value={n2} > </input>
   <input type="submit" name="update1" value="update"></input><br>
   marks2:<input type="text" name="m22" value={n3}> </input>
   <input type="submit" name="update2" value="update"></input><br>
   marks3:<input type="text" name="m33" value={n4} > </input>
   <input type="submit" name="update3" value="update"></input><br>
   
   <a href="http://127.0.0.1/p3.py">Click this</a>
 </div>
 <hr/>
</div>
</form>
    </body>
    </html>"""
n1=str(form.getvalue("idy","0"))
n=str(form.getvalue("name"))
n2=str(form.getvalue("m11"))
n3=str(form.getvalue("m22"))
n4=str(form.getvalue("m33"))
a="select m1,m2,m3,name from students where id="+n1


def up1():
    b="update students set m1="+n2+" where id = "+n1
    print(b)
    cur.execute(b)
    con.commit()
def up2():
    c="update students set m1="+n3+" where id = "+n1
    cur.execute(c)
    con.commit()
def up3():
    d="update students set m1="+n4+" where id = "+n1
    cur.execute(d)
    con.commit()
if "update1" in form:
    up1()
if "update2" in form:
    up2()
if "update3" in form:
    up3()
    

if "save" in form:
    select()

con.commit()
print(htmlFormat.format(**locals()))
