#!/usr/bin/env python3
import cgi
import sqlite3
con=sqlite3.connect("/var/www/html/html/gatepass.db")
cur=con.cursor()
form=cgi.FieldStorage()
print("Content-type:text/html\r\n\r\n")
import cgitb; cgitb.enable()
try:
    f=open("searchStudent.html","r")
    html1=f.read()
    f.close()
    f=open("searchStudent2.html","r")
    html3=f.read()
    f.close()
    html2=''
    searchIP=str(form.getvalue("search"))
    option=str(form.getvalue("searchBy"))
    #SEARCHING
    if option=="Si":
        #SEARCHING VIA ID
        temp='select * from studetails where id like "%'+searchIP+'%"'
        cur.execute(temp)
        temp=cur.fetchall()
        if temp==[]:
            print("NOT FOUND")
        else:
            html2='''<br/><br /><tr> 
                    <th>ID</th>
                    <th>Student's Name</th>
                    <th>Father's Name</th>
                    <th>Student no.</th>
                    <th>Father no.</th>
                    <th>Year</th>
                    <th>Branch</th>
                    <th>Sec</th>
                    <th>Email</th>
                    <th>DOB</th>
                    <th>Gender</th>
                     </tr>'''
            for i in temp:
                html2=html2+'<tr><td>'+i[0]+'</td><td>'+i[1]+'</td><td>'+i[2]+'</td><td>'+str(i[3])+'</td><td>'+str(i[4])+'</td><td>'+str(i[5])+'</td><td>'+i[6]+'</td><td>'+i[7]+'</td><td>'+i[8]+'</td><td>'+i[9]+'</td><td>'+i[10]+'</td></tr>'
                                            
    if option=="Sn":
                #SEARCHING VIA NAME
                temp='select * from studetails where name like "%'+searchIP+'%"'
                cur.execute(temp)
                temp=cur.fetchall()
                if temp==[]:
                    print("NOT FOUND")
                else:
                    html2='''<br/><br /><tr> 
                    <th>ID</th>
                    <th>Student's Name</th>
                    <th>Father's Name</th>
                    <th>Student no.</th>
                    <th>Father no.</th>
                    <th>Year</th>
                    <th>Branch</th>
                    <th>Sec</th>
                    <th>Email</th>
                    <th>DOB</th>
                    <th>Gender</th>
                     </tr>'''
                    for i in temp:
                        html2=html2+'<tr><td>'+i[0]+'</td><td>'+i[1]+'</td><td>'+i[2]+'</td><td>'+str(i[3])+'</td><td>'+str(i[4])+'</td><td>'+str(i[5])+'</td><td>'+i[6]+'</td><td>'+i[7]+'</td><td>'+i[8]+'</td><td>'+i[9]+'</td><td>'+i[10]+'</td></tr>'
            
    if option=="Fn":
        #SEARCHING VIA NAME
                temp='select * from studetails where fathersname like "%'+searchIP+'%"'
                cur.execute(temp)
                temp=cur.fetchall()
                if temp==[]:
                    print("NOT FOUND")
                else:
                    html2='''<br/><br /><tr> 
                    <th>ID</th>
                    <th>Student's Name</th>
                    <th>Father's Name</th>
                    <th>Student no.</th>
                    <th>Father no.</th>
                    <th>Year</th>
                    <th>Branch</th>
                    <th>Sec</th>
                    <th>Email</th>
                    <th>DOB</th>
                    <th>Gender</th>
                     </tr>'''
                    for i in temp:
                        html2=html2+'<tr><td>'+i[0]+'</td><td>'+i[1]+'</td><td>'+i[2]+'</td><td>'+str(i[3])+'</td><td>'+str(i[4])+'</td><td>'+str(i[5])+'</td><td>'+i[6]+'</td><td>'+i[7]+'</td><td>'+i[8]+'</td><td>'+i[9]+'</td><td>'+i[10]+'</td></tr>'
            
    if option=="m":
        #SEARCHING VIA NAME
                temp='select * from studetails where phno like "%'+searchIP+'%" or fathersphno like "%'+searchIP+'%"'
                cur.execute(temp)
                temp=cur.fetchall()
                if temp==[]:
                    print("NOT FOUND")
                else:
                    html2='''<br/><br /><tr> 
                    <th>ID</th>
                    <th>Student's Name</th>
                    <th>Father's Name</th>
                    <th>Student no.</th>
                    <th>Father no.</th>
                    <th>Year</th>
                    <th>Branch</th>
                    <th>Sec</th>
                    <th>Email</th>
                    <th>DOB</th>
                    <th>Gender</th>
                     </tr>'''
                    for i in temp:
                        html2=html2+'<tr><td>'+i[0]+'</td><td>'+i[1]+'</td><td>'+i[2]+'</td><td>'+str(i[3])+'</td><td>'+str(i[4])+'</td><td>'+str(i[5])+'</td><td>'+i[6]+'</td><td>'+i[7]+'</td><td>'+i[8]+'</td><td>'+i[9]+'</td><td>'+i[10]+'</td></tr>'
            



finally:
    html=html1+html2+html3
    print(html.format(**locals()))
