'''Problem
Chef is given 3 integers A, B and C such that A<B<C.

Chef needs to find the value of max(A, B, C) - min(A, B, C)max(A,B,C) - min(A,B,C).

Here max(A, B, C)max(A,B,C) denotes the maximum value among A, B, C while min(A,B,C) denotes the minimum value among A, B, C.'''
t = int(input())
for i in range(t):
    lst = list(map(int, input().split()))
    print(max(lst)-min(lst))
