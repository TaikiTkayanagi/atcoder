N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    left = A[i]
    total = left
    for j in range(i+1, N):
        right = A[j]
        total += right
        ans += 1
        for z in range(i, j + 1):
            if total % A[z] == 0:
                ans -= 1
                break


print(ans)
