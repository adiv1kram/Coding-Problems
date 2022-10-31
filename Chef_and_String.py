#Problem Code:  RECNDSTR  || #Difficulty Rating:1206 || #Contest Code: RC122020


t=int(input()) #giving input number of test cases
for i in range(t): 
    s=input() #taking input of the string
    if s[1:]+s[0]==s[-1]+s[0:-1]: #here we are slicing the string and adding first element at the last and last element at the first place respectively 
        print("YES") #if both are equal then print YES otherwise print NO
    else:
        print("NO")

