N, M = map(int, input().split())
ans = [0] * N 

i = 0
for _ in range(M):
    if i == N:
        i = 0
    ans[i] += 1
    i += 1

for a in ans:
    print(a)
    