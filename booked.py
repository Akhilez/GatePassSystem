#!/usr/bin/env python3
try:
    import cgi
    import sqlite3
    import time
    path="/var/www/html/html/gatepass.db"
    con=sqlite3.connect(path)
    cur=con.cursor()
    form=cgi.FieldStorage()
    print("Content-type:text/html\r\n\r\n")
    f=open("booked.html","r")
    html1=f.read()
    f.close()
    f=open("booked2.html","r")
    html2=''
    html3=f.read()
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
    temp='select id, reqOut, actualOut, reqIn, actualIn, reason from passes where today="'+findtoday()+'"'
    cur.execute(temp)
    temp=cur.fetchall()
    for i in temp:
        html2=html2+"<tr><td>"+i[0]+"</td><td>"+i[1]+"</td><td>"+str(i[2])+"</td><td>"+i[3]+"</td><td>"+str(i[4])+'</td><td>'+i[5]+"</td></tr>"
    html=html1+html2+html3


finally:
    f.close()
    con.close()
    print(html.format(**locals()))
