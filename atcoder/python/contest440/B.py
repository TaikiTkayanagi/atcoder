N = int(input())
T = list(map(int, input().split()))

ans = [0] * N
for i, v in enumerate(T, start=1):
    insert = 0
    for j in range(N):
        if v == T[j]:
            continue
        if v > T[j]:
            insert += 1
    ans[insert] = i

for i in range(3):
    print(ans[i], end=" ")
