#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

nn = sp.getstatusoutput("sudo ansible-playbook /root/nn.yml")

if nn[0] ==0:
    print("<h2>Master Node Ready</h2>")
else:
    pass



