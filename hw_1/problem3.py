print('Problem 3')
print('Hi! I`m Mahmud! First of all, let`s check your age!')

age=int(input())
if age>=18:
  print('Are you a boy or a girl?')
else:
  print('Sorry, we can`t continue our conversation:(')

gender=input()
a=('girl')
if gender==a:
  print('Welcome! I can help you with math! Choose two numbers!')
else:
  print('Sorry, we can`t continue our conversation:(')

b=int(input())
c=int(input())
print('Sum = ', b+c)
print('Difference=', b-c)
print('Product=', b*c)

print('Am I right?')
x=input()
if x==('yes'):
  print('Thank you, dear!')
if x==('no'):
  print('Sorry, I will improve:(')
