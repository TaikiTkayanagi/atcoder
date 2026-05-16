N, K = map(int, input().split())

L = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    L.append(tmp[1:])
C = list(map(int, input().split()))

ans = 0 
count = 0
for i in range(N):
    if count + len(L[i]) * C[i] >= K:
        j = K - count 
        ans = L[i][j % len(L[i]) - 1] 
        break

    count += len(L[i]) * C[i]


print(ans)
        