#!/usr/bin/env python3
import cgi
form=cgi.FieldStorage()
print("Content-type:text/html\r\n\r\n")
import cgitb; cgitb.enable()
try:
    htmlFormat="""
    <!DOCTYPE html>
    <html>
    <head>
	<title>Welcome to KMIT gatepass</title>
	<link rel="stylesheet" type="text/css" href="index.css" />
    </head>
    <body>
	<div id="container">
		<div id="header">
			<h1>Keshav Memorial Institute of Technology</h1>
		</div>
		<div id="nav">
				<div id="navItem1">
					<a href="adhm.py">Home</a>
				</div>
				<div id="navItem2">
					<a href="adstureg.py">Register New Student</a>
				</div>
				<div id="navItem3">
					<a href="adrecreg.py">Register New Receptionist</a>
				</div>
				<div id="navItem4">
					<a href="prelogin.py">Logout</a>
				</div>
				</div>
		<div id="content2">
		<div id="login_as">
		<ul><li>Gate Pass is a Web Application developed by Students of KMIT belonging to Second Year First Semester.</li><br><br>
		<li>This Web Application facilitates the College Management to Issue and Monitor the Students who are requesting for Gatepass.</li>
		</ul></div>
			
				
			<div id="main2">
				<h2>Welcome Admin </h2><br/><hr/></br><br><br>
			<ul type="disc"><table align="center"><tr><td></tr></td>
					<tr><td><li><a href="adkmit.py">Student Details</a></li><br></tr></td>
					<tr><td><li><a href="aregup.py">Staff Details</a></li><br></tr></td>
					</table>
				</ul>
			</div>
			</div>
		</div>
		<div id="footer">
			<p>Copyright@ CSE-D 2015</p>
		</div>
	</div>
    </body>
    </html>"""
#except Exception as e
#    print("Error:",e)
finally:
    print(htmlFormat.format(**locals()))
