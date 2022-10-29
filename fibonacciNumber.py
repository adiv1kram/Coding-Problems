n=int(input())
sum=0
if n>=0:
    if n==0 or n==1:
        print(n)
    else:
        for i in range(1,n+1):
            sum+=i
            i+=1
            print(sum,end=' ')
else:
    print("Print a positive number")

    