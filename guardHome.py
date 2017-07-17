#!/usr/bin/env python3
import cgi
import sqlite3
con=sqlite3.connect("/var/www/html/html/gatepass.db")
cur=con.cursor()
form=cgi.FieldStorage()
print("Content-type:text/html\r\n\r\n")
import cgitb; cgitb.enable()
try:
    import time
    def findtoday():
        #return "2015-09-25"
        t=time.ctime()
        day=t[8]+t[9]
        if int(day)<10:
            day='0'+day[1]
        year=t[20]+t[21]+t[22]+t[23]
        month=t[4]+t[5]+t[6]
        months={"Jan":'01',"Feb":'02',"Mar":'03',"Apr":'04',"May":'05',"Jun":'06',"Jul":'07',"Aug":'08',"Sep":'09',"Oct":'10',"Nov":'11',"Dec":'12'}
        month=months[month]
        return year+"-"+month+"-"+day
    today=findtoday()
    f=open("guardHome.html","r")
    html1=f.read()
    f.close()
    html2='<select name="id" value={idno}>'
    f=open("guardHome2.html","r")
    html3=f.read()
    f.close()
    f=open("guardHome3.html","r")
    html4=f.read()
    temp='select id from passes where today="'+today+'"'
    cur.execute(temp)
    temp=cur.fetchall()
    for i in temp:
        html2=html2+'<option>'+i[0]+'</option>'
    html2=html2+"</select>"
    temp1='<br/><input type="submit" name="approve" value="Go out"></input>'
    temp2='''<br/><input type="submit" name="approve" value="Come in"></input>'''
    
    idno=str(form.getvalue("id"))
    
    name=branch=sec=year=phno=regOut=regIn=fathersname=fathersphno=realOut=realIn=None
    if "submitId" in form:
        temp='select today,reqOut,reqIn, actualOut,actualIn from passes where id="'+idno+'" and today="'+today+'"'
        cur.execute(temp)
        temp=cur.fetchall()
        if temp==[]:
            print("No such id")
        elif temp[0][0]!=today:
            print("Not booked")
        else:
            realOut=temp[0][3]
            realIn=temp[0][4]
            regOut=temp[0][1]
            regIn=temp[0][2]
        temp='select * from studetails where id= "'+idno+'"'
        cur.execute(temp)
        a=cur.fetchall()
        name=a[0][1]
        fathersname=a[0][2]
        phno=a[0][3]
        fathersphno=a[0][4]
        year=a[0][5]
        branch=a[0][6]
        sec=a[0][7]
        temp='select actualOut, actualIn from passes where id="'+idno+'" and today="'+today+'"'
        cur.execute(temp)
        temp=cur.fetchall()
        if temp[0][0]==0:
            html3=html3+temp1
        elif temp[0][0]!=0 and temp[0][1]==0:
            html3=html3+temp2
    if "approve" in form:
        temp='select actualOut, actualIn from passes where id = "'+idno+'" and today = "'+today+'"'
        cur.execute(temp)
        temp=cur.fetchall()
        realOut=temp[0][0]
        realIn=temp[0][1]
        if realOut==0:
            temp='update passes set actualOut=time("now") where id="'+idno+'" and today = "'+today+'"'
            print("bye bye ")
            cur.execute(temp)
        elif realIn==0:
            temp='update passes set actualIn = time("now") where id="'+idno+'" and today = "'+today+'"'
            print("welcome")
            cur.execute(temp)
        else:
           print("Pass already used")
    if "reset" in form:
        temp='update passes set actualOut=0,actualIn=0 where id="'+idno+'" and today = "'+today+'"'
        cur.execute(temp)
        
#except Exception as e:
#    print("Error  : ",e)
finally:
    con.commit()
    con.close()
    f.close()
    html=html1+html2+html3+html4
    print(html.format(**locals()))
