# Problem Code: ADADISH 
# Contest Code: NOV20
t=int(input())
for i in range(t):
    n=int(input())
    c=list(map(int,input().split()))
    c.sort(reverse=True)
    burner1=burner2=0
    for i in range(n):
        if burner1<burner2:
            burner1+=c[i]
        else:
            burner2+=c[i]
    print(max(burner1,burner2))