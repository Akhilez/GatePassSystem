#!/usr/bin/env python3
try:
    import cgi
    import sqlite3
    import cgitb; cgitb.enable()
    import time

    #THIS BRINGS TODAY'S DATE
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

    #CONNECTING DATABASE
    path="/var/www/html/html/gatepass.db"
    con=sqlite3.connect(path)
    cur=con.cursor()

    
    form=cgi.FieldStorage()
    print("Content-type:text/html\r\n\r\n")
    f=open("index.html","r")
    html1=f.read()
    f.close()
    f=open("index2.html","r")
    html2=f.read()
    f.close()
    f=open("index3.html")
    html3=f.read()
    temp1="<tr><td>"
    temp2="</td></tr>"

    #COUNTING NO OF PASSES TAKEN TODAY
    temp='select count(id) from passes where today = date("now")'
    cur.execute(temp)
    temp=cur.fetchall()
    tot=temp[0][0]


    #EXTRACTING DATA FROM TEXT BOXES 
    idno=str(form.getvalue("id"))
    reason=str(form.getvalue("reason"))
    regOut=str(form.getvalue("regOut"))
    regIn=str(form.getvalue("regIn"))


    #EXTRACTING STUDENT HISTORY
    html2=html2+'<table width="100%" border="1"><tr><th>Date</th><th>Time Out</th><th>Time In</th></tr>'
    temp='select today,actualOut,actualIn from passes where id="'+idno+'"'
    cur.execute(temp)
    temp=cur.fetchall()
    c=0
    for i in temp:
        html2=html2+temp1+i[0]+'</td><td>'+str(i[1])+'</td><td>'+str(i[2])+temp2
        if c>17:
            break
        c+=1
    html2=html2+'</table>'
    temp='select * from studetails where id= "'+idno+'"'
    cur.execute(temp)
    a=cur.fetchall()
    
    name=branch=sec=year=phno=fathersname=fathersphno=None
    if "submitId" in form:
        if a==[]:
            print("invalid id")
        else:
            name=a[0][1]
            
            fathersname=a[0][2]
            phno=a[0][3]
            fathersphno=a[0][4]
            year=a[0][5]
            branch=a[0][6]
            sec=a[0][7]
    if "issue" in form:

        #SMS INTEGRATION
        from getpass import getpass
        import sys
        import nsm2
        def smsinvgp(u,p,rm):
            global user
            global pwd1
            global msg1
            global rcmobile
            user=u
            pwd1=p

            #EXTRACTING TIME DETAILS FROM DATABASE
            temp='select reqOut,reqIn,today,reason from passes where id="'+idno+'" and today="'+today+'"'
            cur.execute(temp)
            temp=cur.fetchall()
            #EXTRACTING NAME
            temp3='select name,fathersphno from studetails where id="'+idno+'"'
            cur.execute(temp3)
            temp3=cur.fetchall()
            msg1='Dear parent, your ward '+temp3[0][0]+' has taken gatepass from KMIT on'+temp[0][2]+' from '+temp[0][0]+' to '+temp[0][1]+'. Reason:'+temp[0][3]+'. Please confirm. Thank you'   
            rcmobile=rm
            #print("in smsinvgrp")
            ###print("\n\n\n\n\n\n\n usr",user,pwd1,9849209018)
            #print("in sms inv",moblist)
            '''for mob in moblist:
                print(mob)'''
            #nsm2.smscall(user,pwd1,msg1,str(temp3[0][1]))
            #nsm2.smscall(user,pwd1,msg1,'9849209018')
            nsm2.smscall('8686956567','rajrocks',msg1,str(temp3[0][1]))
        



        

        #CHECKING IF ITS THE FIRST TIME
        temp='select id from passes where id="'+idno+'" and today = "'+today+'"'
        cur.execute(temp)
        temp=cur.fetchall()
        if temp!=[]:
            print("Pass already taken")
        else:   

        
            #CHECKING FOR ID VALIDITY
            cur.execute("select id from studetails")
            temp=cur.fetchall()
            for i in temp:
                if idno in i[0]:
                        temp='insert into passes values("'+idno+'",date("now"),"'+regOut+'","'+regIn+'",0,0,"'+reason+'")'
                        cur.execute(temp)
                        smsinvgp('9573205741','T6329H',12)
                        break
                    
            else:
                html=html3
#except Exception as e:
#    print("Error : ",e)
finally:
    con.commit()
    con.close()
    f.close()
    html=html1+html2+html3
    print(html.format(**locals()))
