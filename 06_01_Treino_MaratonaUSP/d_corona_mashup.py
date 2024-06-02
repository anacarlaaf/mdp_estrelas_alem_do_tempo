n = int(input())
dates = list(map(int, input().split()))
dates.sort(reverse=True)

per_day = {}
for i in range(n):
    per_day[dates[i]] = per_day.get(dates[i], 0) + 1

total = n
i = 0
while True:
    if i == n:
        print(-1)
        break
    if total % 3 == 0:
        print(dates[i])
        break
    total -= per_day[dates[i]]
    i += per_day[dates[i]]

