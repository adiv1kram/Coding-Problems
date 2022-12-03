# Problem Code: EXPSTP


T=int(input()) #taking input for thr test cases
for i  in range(T):
    inp=list(map(int,input().split()))
    num=inp[0]+1 #Assigning the the length of the grid which is N
    sum_g1=abs(inp[3]-inp[1])+abs(inp[4]-inp[2])
    sum_g2=min(inp[1],inp[2],abs(num-inp[2]),abs(num-inp[1])) + min(inp[4],inp[3],abs(num-inp[4]),abs(num-inp[3]))
    print(min(sum_g1,sum_g2)) #printing the least of the two cost
    