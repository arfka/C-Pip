import re
import string
import urllib2
import time

def R_string (str_o) :
	st = str_o.replace("<td>", "").replace('&nbsp;', " ").replace('"', "").replace(">", "").replace("<", "").replace("/a", "")
	return st 

f = open ("out.ini", 'wb')
f.write (' ')
re1='">([A-z])([*-z])*.+<'
re2='<td>([A-z])(.)+<'
rg1 = re.compile(re1,re.IGNORECASE|re.DOTALL)
rg2 = re.compile(re2,re.IGNORECASE|re.DOTALL)
url = urllib2.urlopen('https://pypi.python.org/pypi?%3Aaction=index')
html = url.readlines()
for line in html:
    s = ""
    r = ""
    j = 0
    k = 0
    i = 0
    i1 = 0
    m = rg1.search(line)
    m1 = rg2.search(line)
    if m and line[0:3] == " <t":
        j = 1
        word1=m.group(i)
        s = s+word1
        i+= 1
    s = R_string (s) 
    if j is 1:
        f.write (s + ' :   ')
     
f.close()
print 'done'
        



    