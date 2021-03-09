print('problem 4')

s=input()
r=[None]
for ch in s:
  if ch !=r[-1]: r.append(ch)
s_new=''.join(r[1:]) #чем можно заменить эту строку
print(s_new) 
