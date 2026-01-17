N, K, X = map(int, input().split())
water = N - K
A = list(map(int, input().split()))
A.sort()
A.reverse()

total = 0
ans = -1
for i in range(water + 1, N + 1):
    total += A[i - 1]
    if total >= X:
        ans = i
        break
print(ans)
