N, K = map(int, input().split())


ans = 0
for i in range(1, N+1):
    s = str(i)

    ret = 0
    for v in s:
        ret += int(v)

    if K == ret:
        ans += 1

print(ans)
