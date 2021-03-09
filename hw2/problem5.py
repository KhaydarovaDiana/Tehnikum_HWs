print('problem 5’)

a = input()
i = 0 
while a[i] == ' ':
    a = a[1:]
while a[len(a)-1] == ' ':
    a = a[:-1]
i = 1
while i < len(a)-1:
    if a[i] == ' ' and a[i+1] == ' ':
        a = a[:i+1] + a[i+2:]
    else:
        i += 1
print(a)
