#Problem Code: NEWPIECE || #Contest Code:START17

t=int(input())
for i in range(t):
    a,b,p,q=map(int,input().split())
    
    if a==p and b==q:
        print(0)
    elif ((a+b)%2==0 and (p+q)%2==0) or ((a+b)%2==1 and (p+q)%2==1):
        print(2)
    else:
        print(1)