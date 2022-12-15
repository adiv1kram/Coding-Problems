# 1.  Write a Python function that prints out the first n rows of Pascal's triangle.
def pascal(n):
   row = [1]
   y = [0]
   for x in range(max(n,0)):
      print(row)
      row=[l+r for l,r in zip(row+y, y+row)]
   return n>=1
pascal(6) 