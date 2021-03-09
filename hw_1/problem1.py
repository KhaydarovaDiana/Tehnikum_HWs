print('Problem 1')
print('Three different numbers are entered. Find which one is the average') 
a=int(input())
b=int(input())
c=int(input())

if c>a>b or c<a<b:
  print(a)
if c>b>a or c<b<a:
  print(b)
if b>c>a or b<c<a:
  print(c)
