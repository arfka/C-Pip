



s = 0
for x in P:
    s += x
print s 







def P(x):
    try:
        if x==0: raise TypeError
    except TypeError:
        print "Zero can't be treated!"
        return None
    i = 2
    j = 0
    while True:
        if (i != x)and(x%i) == 0:
            j = 1
            break
        elif x == 1:
            return True
        i+=1
    if j == 0:
        return True
    else:
        return False
        
print primal(5)