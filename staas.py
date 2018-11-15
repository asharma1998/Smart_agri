#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

form = cgi.FieldStorage()
stname = form.getvalue('sn')
stsize = form.getvalue('ss')
stunit = form.getvalue('size')

#stname = input("enter name")
#stsize= int(input("enter size"))
#stunit = input("enter Unit")

nfs = sp.getstatusoutput("sudo ansible-playbook /root/lv.yml --extra-vars='x={0} y={1} z={2}'".format(stsize,stunit,stname))

if nfs[0] ==0:
    print("<h1>")
    print("Storage is now available")
    print("</h1>")
    mount = sp.getstatusoutput("sudo ansible-playbook /root/lv_client.yml --extra-vars='x={0}'".format(stname))
    if mount[0] ==0: print("<h3>Now you can access storage</h3>")
    else: print("Storage not available")      
else:
    print("<h1>")
    print("Error!")
    print("</h1>")



