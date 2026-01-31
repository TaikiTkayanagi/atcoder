N, T = map(int, input().split())
A = list(map(int, input().split()))

open = 0
ans = 0
for a in A:
    if a < open:
        continue
    ans += a - open
    open = a + 100

if T > open:
    ans += T - open

print(ans)
