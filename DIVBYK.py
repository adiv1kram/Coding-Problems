#Problem Code: DIVBYK #Contest Code: DEC221
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    multiply=1 
    flag=False
    for i in a:
        multiply*=i 
        if multiply%k==0:
            flag=True
            break 
    if flag==True:
        print("YES")
    else:
        print("NO")