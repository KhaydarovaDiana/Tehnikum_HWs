print('problem 4')

s=input()
r=[None]
for ch in s:
  if ch !=r[-1]: r.append(ch)
s_new=''.join(r[1:]) #чем можно заменить join? и за что он отвечает в этом коде, недоконца понятно
print(s_new) 
