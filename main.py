t = int(input('Digite termo: '))
r = int(input('razão: '))

d = t+ (10 - 1) * r

for c in range(t, d + 1 ,r):
  print('{}'.format(c), end='-> ')
print('ACABOU')