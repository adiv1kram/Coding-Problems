# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    count=0
    for i in range(n):
        if i>0:
            if lis[i]!=lis[i-1]: #if the second player misheards
                count+=1
                continue
        if i<n-1:
            if lis[i]!=lis[i+1]:
                count+=1 
    print(count)
    
 #pull request
                
            
        
    
    
    
