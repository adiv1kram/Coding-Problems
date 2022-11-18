# Problem Code: HOWMANYMAX

t=int(input())
for i in range(t):
    n=int(input())
    s=input() 
    s=s+s[n-2]
    max=1
    for i in range(n-1):
        if s[i]=='1' and s[i+1]=='0':
            max+=1 
    print(max)
    