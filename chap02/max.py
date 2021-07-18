import typing
from typing import Any,Sequence

def max_of(a: Sequence) -> Any:
  """シーケンスの最大値を求める"""
  max = a[0]

  for i in range(1, len(a)):
    if a[i] > max:
      max = a[i]
  
  return max

if __name__=='__main__':
  print('配列の最大値を求める')
  num = int(input('要素数: '))
  x = [None] * num

  for i in range(num):
    x[i] = int(input(f'x[{i}] : '))

  print(f'最大値は{max_of(x)}です') 
