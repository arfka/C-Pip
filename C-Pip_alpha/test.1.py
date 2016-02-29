import crypt
from data import *
import re
import string
import urllib2
import os
import filecmp
import commands
import pip
from pip.operations import *

crypt.decrypt_file ("out.txt", "outd.txt")
p = data_extractor("outd.txt")
for i in p:
    print i.n, i.d