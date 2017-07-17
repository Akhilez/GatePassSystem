#!/usr/bin/env python3
try:
    import cgi
    import sqlite3
    import cgitb; cgitb.enable()
    path="/var/www/html/html/gatepass.db"
    con=sqlite3.connect(path)
    cur=con.cursor()
    form=cgi.FieldStorage()
    print("Content-type:text/html\r\n\r\n")
    f=open("directorHome.html","r")
    html1=f.read()
    f.close()
    html2=''
    html2='No. of passes taken : {noOfPasses}<br /><br /><table width="50%" align="center" border="1px solid black">'
    f=open("directorHome2.html","r")
    html3=f.read()
    f.close()
    #months=["Jan","Feb","Mar","Apr","May",'Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    months2={"Jan":'01',"Feb":'02',"Mar":'03',"Apr":'04',"May":'05',"Jun":'06',"Jul":'07',"Aug":'08',"Sep":'09',"Oct":'10',"Nov":'11',"Dec":'12'}
    #months3={"Jan":'31',"Feb":'28',"Mar":'31',"Apr":'30',"May":'31',"Jun":'30',"Jul":'31',"Aug":'31',"Sep":'30',"Oct":'31',"Nov":'30',"Dec":'31'}
    noOfPasses=0
    if "submitMonth" in form:
        month=str(form.getvalue("month"))
        html2='No. of passes taken : {noOfPasses}<br /><br /><table width="50%" align="center" border="1px solid black">'
   
        temp='select count(id),today from passes where (strftime("%m",today)="'+month+'") group by today'
        cur.execute(temp)
        temp=cur.fetchall()
        for i in temp:
            noOfPasses=noOfPasses+i[0]
        html2=html2+'<tr><th>Date</th><th>No of passes issued</th></tr>'
        for i in temp:
            html2=html2+'<tr><td>'+str(i[1])+'</td><td>'+str(i[0])+'</td></tr>'
    html2=html2+'</table>'
        


finally:
    html=html1+html2+html3
    print(html.format(**locals()))
