n, a, p = map(int, input().split())
perc = a*p - a*(100-p)
ans = n+(1*perc/100)
print("{x:.9f}".format(x=ans))