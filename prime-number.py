#素数判定を行うアルゴリズム


#簡単なやり方1
def alg1():

  #素数の個数カウンター
  counter = 0
  #除算の回数カウンター
  order = 0



  #1~1000までの素数判定
  print(2)
  for n in range(3,1001,2):
    for i in range(2, n):
      order += 1
      if n % i == 0:
        break
    else:
      counter += 1  
      print(n)

  print(f'素数の個数 : {counter}個, 除算回数 : {order}回')

alg1()
print()


#簡単なやり方2
def alg2():

  #素数の個数カウンター
  counter = 0
  #除算の回数カウンター
  order = 0
  #素数のリスト
  primes = [None]*500

  #1~1000までの素数判定
  print(2)
  for n in range(3,1001,2):
    for i in range(2, counter):
      order += 1
      if n % primes[i] == 0:
        break
    else:
      primes[counter] = n
      counter += 1  
      print(n)

  print(f'素数の個数 : {counter}個, 除算回数 : {order}回')

alg2()
print()


#改良版
#todo
