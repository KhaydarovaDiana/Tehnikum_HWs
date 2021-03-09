print('Problem 2’)
print('Three integers are entered. Determine which one is the greatest')
a=int(input())
b=int(input())
c=int(input())

if b<a>c or c<a>b:
  print(a)
if a<b>c:
  print(b)
if a<c>b:
  print(c)
