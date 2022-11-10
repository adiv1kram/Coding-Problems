#EVM Hacking #Problem Code: EVMHACK 
t=int(input())
for i in range(t):
    a,b,c,p,q,r=list(map(int,input().split()))
    avg=(p+q+r)/2
    if (a+b+r)>avg or (b+c+p)>avg or (a+c+q)>avg:
        print("YES")
    else:
        print("NO")