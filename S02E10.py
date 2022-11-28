#The One with Russ  Difficulty Rating:1230    Problem Code:S02E10

t=int(input())
for i in range(t):
    n,x,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    for i in range(n):
        val=abs(a[i]-b[i])
        if val<=k:
            c+=1 
    if c>=x:
        print("YES")
    else:
        print("NO")
            