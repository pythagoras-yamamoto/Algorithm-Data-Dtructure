from max import max_of

print('配列の最大値を求めます')
print('ENDで入力終了')

inputNumber = 0
x = []

while True:
  s = input(f'x[{inputNumber}]: ')
  if s == 'END':
    break
  x.append(int(s))
  inputNumber += 1

print(f'{inputNumber}個入力されました')
print(f'最大値は{max_of(x)}です')