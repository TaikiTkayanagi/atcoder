N = int(input())

memo = {}
for i in range(N):
    v = input().lower()

    if v in memo:
        memo[v] += 1
    else:
        memo[v] = 1

print(max(memo.values()))
