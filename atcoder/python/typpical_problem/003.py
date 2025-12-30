N = int(input())
memo = {}

for i in range(1, N):
    a, b = map(int, input().split())

    if a in memo:
        memo[a] = memo[a] + 1
    else:
        memo[a] = 1

    if b in memo:
        memo[b] = memo[b] + 1
    else:
        memo[b] = 1

max = 0

for value in memo.values():
    if value > max:
        max = value

print(max + 1)
