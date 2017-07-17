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
    f=open("studentHistory.html","r")
    html1=f.read()
    f.close()
    f=open("studentHistory2.html","r")
    html2=''
    html3=f.read()
    out=''
    idno=str(form.getvalue("id"))
    if "submitId" in form:
        temp='select count(id) from passes where id="'+idno+'"'
        cur.execute(temp)
        temp=cur.fetchall()
        out=temp[0][0]
        temp='select today, reqOut,actualOut, reqIn, actualIn, reason from passes where id="'+idno+'"'
        cur.execute(temp)
        temp=cur.fetchall()
        
        html2=html2+'''<tr>
						<th>Date</th>
						<th>Requested Out Time</th>
						<th>Actual Out Time</th>
						<th>Requested In Time</th>
						<th>Actual In Time</th>
                                                <th>Reason</th>
					</tr>	'''
        for i in temp:
            html2=html2+'<tr><td>'+i[0]+'</td><td>'+i[1]+'</td><td>'+str(i[2])+'</td><td>'+i[3]+'</td><td>'+str(i[4])+'</td><td>'+i[5]+'</tr>'
       


finally:
    f.close()
    con.close()
    html=html1+html2+html3
    print(html.format(**locals()))
