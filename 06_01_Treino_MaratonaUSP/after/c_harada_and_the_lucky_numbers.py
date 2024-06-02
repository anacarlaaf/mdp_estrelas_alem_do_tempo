x= input().split(" ")
q = int(x[0])
n = int(x[1])
l1 = input()
l2 = input()

l1 = [int(l) for l in l1.split(" ")]
l2 = [l for l in l2.split(" ")]

l1.sort()
"""
Só ordenar não daria certo:
Ex: 
4 10
111 112 145 167
1 1 1 1 1 2 4 5 6 7
3
112 145 167

Da nova forma não precisaria ordenar
"""

l1 = [str(l) for l in l1]

d = {}
dr = {}
for l in l2:
    if l not in d.keys():
        d[l] = 1
        dr[l] = 1
    else:
        d[l] += 1
        dr[l] += 1

k = dr.keys()
v = dr.values()
def reset():
    for k1, v1 in zip(k, v):
        d[k1] = v1

seq = []
f = 0
for x in range(q):
    f1 = 0
    seqaux = []
    for l in l1:
        dp = {}
        for i in range(len(l)):
            if l[i] not in dp.keys():
                dp[l[i]] = 1
            else:
                dp[l[i]] += 1
        k1 = dp.keys()
        j = 0
        for k2 in k1:
            if k2 in k:
                if d[k2] >= dp[k2]:
                    j += 1
        if j == len(k1):
            f1 += 1
            seqaux.append(l)
            for k2 in k1:
                if k2 in k:
                    if d[k2] >= dp[k2]:
                        d[k2] -= dp[k2]
    if f1 > f:
        f = f1
        seq = seqaux
    lx = l1.pop(0)
    l1.append(lx)
    reset()


print(f)
print(" ".join(seq)) 
