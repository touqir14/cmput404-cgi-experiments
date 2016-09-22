#!/usr/bin/env python

import cgi
import os
import json
import sys

form = cgi.FieldStorage()
loggedInOk=False

if form.getvalue('user') == 'bob' and form.getvalue('password') == 'hunter2':
	loggedInOk=True
if 'loggedin=true' in os.environ['HTTP_COOKIE']:
	loggedInOk=True

print "Content-type: text/html"
if loggedInOk:
	print "Set-Cookie: loggedin=true"
print
print "<HTML><BODY><H1>Hello, world!</H1></BODY></HTML>"
print "<FORM method='POST'><INPUT name='user'/>"
print "  <INPUT name='password' type='password'>"
print "  <BUTTON type='submit'>Log in</BUTTON>"
print "</FORM>"

print "<P>Query string was: " + os.environ['QUERY_STRING'] + "</P>"
print "<P> Your browser is: " + os.environ['HTTP_USER_AGENT'] + "</P>"

# print "<P>"
# print "User name is : " + form.getvalue('user') + ". "
# print "Password was : " + form.getvalue('password') + '.'
# print "</P>"

if loggedInOk:
	print "<H2> LOG IN OK </H2>"

cgi.print_environ()

print json.dumps(dict(os.environ), indent=4)

print "</BODY></HTML>"