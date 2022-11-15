# cook your dish here
from collections import OrderedDict
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    l=len(s)
    strlist=list()
    newlist=list()
    j=0
    if l%2==1:
        print("NO")
    else:
        for i in range(len(s)):
            strlist.append(s[i])
        for i in range(len(strlist)):
            if s[i] not in newlist:
        newlist.insert(j, s[i])
        j = j+1
        newstr = ""
        for c in newlist:
        newstr = newstr + c
        if newstr==s:
            print("NO")
        else:
            print("YES")
            
            
        
            
            