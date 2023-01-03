#Problem Code: HORSES
#Contest Code: SEP12
import math
t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    s.sort()
    diff=s[1]-s[0]
    for i in range(n-1):
        if(s[i+1]-s[i])<=diff:
            diff=s[i+1]-s[i]
    print(diff)
    