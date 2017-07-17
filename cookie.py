#!/usr/bin/env python3.4
from http.cookies import*

# create the cookie
c=SimpleCookie()

# assign a value
c['raspberrypi']='passwor'
# set the xpires time
c['raspberrypi']['expires']=1*1*3*60

# print the header, starting with the cookie
print(c)
print("Content-type: text/html\n");

# empty lines so that the browser knows that the header is over
print("");
print("");

# now we can send the page content
print("""
<html>
    <body>
        <h1>The cookie has been set</h1>
    </body>
</html>
""");
c['raspberrypi']="sagarvarma";
print(c);
