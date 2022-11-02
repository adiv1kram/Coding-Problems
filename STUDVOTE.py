# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    count=0
    for i in range(len(a)):
        if (i+1)!=a[i] and a.count(i+1)>=k:
            count+=1
    print(count)
        
    
    