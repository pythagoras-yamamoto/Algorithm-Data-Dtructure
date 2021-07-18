# 値Xと値Yの最大公約数を求めるアルゴリズム


def gcd(m, n):
    if (m % n) == 0: return n
    else: return gcd(n, m % n)


def printGCD(m, n):
    print(str(m) + "と" + str(n) + "の最大公約数は" + str(gcd(m, n)) + "です。")


printGCD(120,50)