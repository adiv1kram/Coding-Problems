#Problem Code: DIVAB
t=int(input())
for i in range(t):
    a,b,n=map(int,input().split())
    i=n
    if a%b==0:
        print(-1)
    else:
        if n%a!=0:
            n=((n//a)+1)*a
        while(1):
            if n%a==0 and n%b!=0:
                print(n)
                break
            else:
                n+=a 