import random

from max import max_of

print('乱数の最大値を求める')
num = int(input('乱数の個数: '))
lo = int(input('乱数の下限: '))
hi = int(input('乱数の上限: '))
x = [None] * num

for i in range(num):
  x[i] = random.randint(lo, hi)

print(f'{x}')
print(f'最大値: {max_of(x)}')
