#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

form = cgi.FieldStorage()
contn = form.getvalue('cont')
software = form.getvalue('soft')

if software == "firefox":
    s = sp.getstatusoutput("sudo ansible-playbook /root/SAAS.yml --extra-vars='x={0}'".format(contn))
    print("Instructions: run this command on your shell-> ssh root@192.168.43.185 -p 9999 -X firefox")
    if s[0] == 0:
       print("Firefox is available")
else:
    pass



