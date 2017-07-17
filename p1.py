#!/usr/bin/env python3
import cgi
form=cgi.FieldStorage()
print("Content-type:text/html\r\n\r\n")
htmlFormat="""<html><title> The Time Now</title>
    <body >
    <div align="center" width="30%" style="font-size:25px;border:1px solid black">
    <form style="background-color:lightgrey">
    Num1:<input type="text" name="num1" value='0' ></input><br>
 Num2:<input type="text" name="num2" value='0' ></input><hr>
 <div id="buttons" style="background-color:lightgreen;padding:30px" >
   <input type="submit" name="add" value="+" > </input>
   <input type="submit" name="subtract" value="-"> </input><br/>
   <input type="submit" name="multiply" value="*" > </input>
   <input type="submit" name="divide" value="/" > </input>
 </div>
 <hr/>
    Result:<input type="text" name="num3" value={n3} ></input><hr>
    </form>
    <p>Number 1:   {n1}</p>
    <p>Number 2:   {n2}</p>
    <p>Result  :   {n3}</p>
</div>
    </body>
    </html>"""
#num11=form.getvalue("num1",0)
#num33=form.getvalue("num3",0)
n1=int(form.getvalue("num1",0))
n2=int(form.getvalue("num2",0))
n3=int(form.getvalue("num3",0))
#def sqr():
#    global n3
#    n3=n1*n1
if "add" in form:
    n3=n1+n2
if "subtract" in form:
    n3=n1-n2
if "multiply" in form:
    n3=n1*n2
if "divide" in form:
    n3=n1/n2
    #n3=n1*n1 #neglect the function and use this statement

print(htmlFormat.format(**locals()))
