N, M = map(int, input().split())

memo = {i: -1 for i in range(M)}
for _ in range(N):
    C, S = map(int, input().split())
    C -= 1 
    memo[C] = max(memo[C], S)

for i in memo.values():
    print(i, end=" ")

