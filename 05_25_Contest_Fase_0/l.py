n = int(input().strip())
a = input().strip().split()
b = input().strip().split()

aux = {nome: i+1 for (nome, i) in zip(a, range(len(a)))}
result = []
m=0
for i in range(n):
    ab = aux[b[i]]
    if ab>=m:
        r = (b[i]+" ")*(ab-m)
        result.append(r[:-1])
        m = ab
    else:
        continue

print(" ".join(result))