# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(str,input().split()))
    ans="YES"
    if s[-1]=="cookie":
        ans="NO"
    else:
       for i in range(len(s)-1):
            if s[i]=="cookie" and s[i+1]!="milk":
                ans="NO"
                break
    print(ans)
        
