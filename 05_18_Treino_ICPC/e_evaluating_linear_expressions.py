a, b, k = map(int, input().split())
ans = []
for i in range(1, k+1):
    ans.append(a*i+b)
print(*ans)
