#Problem Code: SPLITMAX 
test_cases=int(input())
for i in range(test_cases):
    num = int(input())
    ci = list(map(int, input().split()))
    print((sum(ci) * (sum(ci)-1)) % 998244353) #the logic here is to sum the number of elements through which we will get 1's whose sum is also equal to the sum of given numbers in the array and multiply it with sum-1