#!/user/bin/env python3
import cgi
print('Content-Type:text/html\r\n\r\n')
form=cgi.FieldStorage()
print('<html>')
print('<head>')
print('<title>Hello World-First CGI Program</title>')
print('</head>')
print('<body>')
print('<h2>Hello World! This is my first CGI program</h2>')
print('</body>')
print('</html>')
