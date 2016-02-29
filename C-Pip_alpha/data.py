import crypt
import re
import string
import urllib2
import os
import filecmp
import commands
import pip 
from pip.operations import *


class Pack:
    def __init__(self, name, desc):
        self.n = name
        self.d = desc


def R_string (str_o) :
	st = str_o.replace("<td>", "").replace("<td>", "").replace("</td>", "").replace('&nbsp;', " ").replace('"', "").replace(">", "").replace("<", "").replace("/a", "")
	return st 


def fetch_all_pack(): #fetch all the packages in the repository
    f = open ("out.txt", 'wb')
    f.write (' ')
    re1='">([0-9-A-z])([*-z])*.+<'
    re2='<td>([0-9-A-z])(.)+'
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
        if m1 and line[0:4] == " <td":
            k = 1
            i1 = 0 
            word2=m1.group(i1)
            r = r+word2
            i1+= 1
        r = R_string (r) 
        
        if j is 1:
            q = s
        if k is 1:
            da = q + ',,' + r 
            da = crypt.encrypt(da) 
            f.write (da)
            f. write ('\n')
            q=""
         
    f.close()


def fetch_new_pack(): ##fetch not installed packages in the repository
    f = open ("newout.txt", 'wb')
    if os.path.exists('installed.txt') is False:
        export_ipackage()
    else:
        delete_old_file('installed.txt')
        export_ipackage()
    dp = open ('installed.txt', 'rb')
    f.write (' ')
    re1='">([0-9-A-z])([*-z])*.+<'
    re2='<td>([0-9-A-z])(.)+'
    rg1 = re.compile(re1,re.IGNORECASE|re.DOTALL)
    rg2 = re.compile(re2,re.IGNORECASE|re.DOTALL)
    url = urllib2.urlopen('https://pypi.python.org/pypi?%3Aaction=index')
    html = url.readlines()
    opack = package_installed()
    q=""
    j = 0
    for line in html:
        s = ""
        r = ""
        k = 0
        i = 0
        i1 = 0
        m = rg1.search(line)
        m1 = rg2.search(line)
        if m and line[0:3] == " <t":
            word1=m.group(i)
            s = s+word1
            i+= 1
            s = R_string (s)
            st = s.split(' ')
            for sp in opack:
                j = 0
                if sp == st[0]:
                    q44 = s
                    j = 1 
        if m1 and (line[0:4] == " <td") and (j == 1):
            k = 1
            i1 = 0 
            word2=m1.group(i1)
            r = r+word2
            i1+= 1
            r = R_string (r)
        if (k is 1):
            print q44
            da = q44 + ',,' + r 
            #da = crypt.encrypt(da) 
            f.write (da)
            f. write ('\n')
            q=""
            j = 0
         
    f.close()


def install_package(pa): #install a package
    pip.main(['install', pa])


def display_ipackage(): #display installed packages
    x = freeze.freeze()
    for p in x:
        print p
        
        
def export_ipackage(): #export installed packages to a text file named 'installed.txt'
    x = freeze.freeze()
    f = open ('installed.txt', "wb")
    for p in x:
        f.write(p)
        f.write('\n')


def delete_old_file(f): #Delete a file 
    if os.path.exists(f):
        os.remove(f)
 
       
def compare_files (f, f1): #compare two files 
    if filecmp.cmp (f, f1):
        return 1
    else:
        return 0
    
    
def data_extractor(f): #extract libs from a file
    da = [line.rstrip() for line in open(f)]
    pa = []
    for t in da:
        tab = t.split(',,')
        pa.append(Pack(tab[0], tab[1]))
    return pa


def package_installed(): #display installed package with no seperation
    commands.getstatusoutput('pip freeze > installed.txt')
    f = open ('installed.txt', 'rb')
    file = f.readlines()
    fo = []
    for s in file:
        k = s.split('==')
        fo.append(k[0])
    f.close()
    return fo

def ipackage_file(file): #install package from file
    f = open (file, 'rb')
    file = f.readlines()
    fo = ''
    for s in file:
        k = s.split('==')
        fo = k[0]
        print "installing", fo
        print " " 
        install_package(fo)
    f.close()
    return fo

fetch_new_pack()