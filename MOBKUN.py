# cook your dish here
try:
 t=int(input())
 c=0
 for i in range(t):
    n,mob,k,xas=map(int,input().split()) #taking input here
    if (xas%((n*k)+mob))==0:
        print("YES")
    elif (xas%((n*k)+mob)-(n*(k-1)))>0:
        print("YES")
    else:
        print("NO")

except:
    pass