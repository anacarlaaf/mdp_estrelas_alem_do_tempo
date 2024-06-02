import math


def primo(n):
    prime_flag = 0
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            return True
        else:
            return False
    else:
        return False


def nprimo(n):
    b = 1
    aa = []
    for k in range(int((n-1)//2), 0, -1):
        if not primo(k) and not primo(k+b):
            return k, k+b
        else:
            b += 2
    return -1, -1


T = int(input())

for t in range(T):
    N = int(input())
    x, y = nprimo(N)
    if x == -1:
        print(-1)
    else:
        if x<y:
            print(x, y)
        else:
            print(y, x)
