#MAKING A MEAL #PROBLEM CODE :CFMM

t=int(input())
for i in range(t):
    n=int(input())
    c,o,d,e,h,f=0,0,0,0,0,0 #using counters for each letter in the word codechef
    for i in range(n): 
        s=input()
        #in the below step i am checking how many times each letter is present in the string
        c+=s.count('c')
        o+=s.count('o')
        d+=s.count('d')
        e+=s.count('e')
        h+=s.count('h')
        f+=s.count('f')
    #i am dividing c and e because each are present twice already in the codechef
    c//=2
    e//=2
    #minimum because with only the number of each letter, the maximum number of times the recipe "codechef" can be formed
    print(min(c,o,d,e,h,f))