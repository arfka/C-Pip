from collections import OrderedDict

#count a character occurence in a text
def count_char(text, char):
    count = 0
    if char in "abcdefghijklmnopqrstuvwxyz":
        for c in text:
            if (c == char):
                count += 1        
    else:
        for c in text:
            if c not in "abcdefghijklmnopqrstuvwxyz":
                count += 1     
        
    return count

#count characters in a text file and return a % in a list.
def text_analyser ():
    filename = raw_input("Enter a filename: ")
    with open(filename, "rb") as f:
      text = f.read()
    out = OrderedDict()
    for char in "abcdefghijklmnopqrstuvwxyz":
      perc = 100 * float(count_char(text, char)) / len(text)
      out[char] = round(perc,3)
    perc1 = count_char(text,'*')
    perc1 = 100 * float(perc1) / len(text)
    out['Unknown'] = round(perc1,3)
    return out 
l = text_analyser()
for i in l:
    print i, "  ", l[i], " %"

#input a number
def input_int():
    n = int(raw_input("Enter a number : "))
    return n  


#primal_check
def primal (x):
    s = 0
    for i in range (1,x):
        if (x%i == 0) and (x/i != x) and i != 1 :
            s += 1
            #print "{2} is devided by {0} and the result is {1}".format(i, x/i, x)
    if s == 0:
        return True
    else:
        return False 

#primal extraction
def get_primes(x):
    num = 1
    if x ==1:
        yield 1
    else:
        while True:
            if primal(num):
                yield num
            num += 1
            if num == x:
                break 


#in decor, the wrap fct take the same number of arguments of the original fct.
#decoration example fonction
def decor(func):
    def wrap(s):
        p = ''
        for i in range (len(s)):
            p += '='
        print p
        func(s)
        print(p)
    return wrap
    
    
#linking a decoration to a fonction.
@decor #calling a decoration template for the fonction
def print_text(s):
  print(s)

  