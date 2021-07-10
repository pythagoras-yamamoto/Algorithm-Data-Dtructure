#基数変換のアルゴリズム


#10進数からn進数への変換関数
#xは変換する数, rは基数
def conv_10_to_N(x: int, r: int) -> str:

  d = ''
  dchar='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  while x > 0:
    d += dchar[x % r]
    x //= r
  
  return d[::-1]


#n進数から10進数への変換関数
#todo


#メイン部
if __name__ == '__main__':
  print('10進数からn進数に変換')
  print('基数nを2~32から選んでください。')

  while True:
    n = int(input('基数n :　'))
    if 2 <= n <= 32:
      break
  
  while True:
    num = int(input('変換する数を入力してください : '))
    if num > 0:
      break

  print(f'{num}(10進数) = {conv_10_to_N(num, n)}({n}進数)')

