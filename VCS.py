#Problem Code: VCS #Contest Code: COOK57 #Difficulty Rating:1217

import math
t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    count=0
    for i in a:
        if i in b:
            count+=1 
    a+=b 
    a=set(a)
    print(count,n-len(a))
            
            
            
        
    
    
    