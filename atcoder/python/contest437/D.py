def find(threshold: int, target: list[int]):
    left = 0
    right = len(target) - 1

    while left <= right:
        mid = (left + right) // 2
        if threshold >= target[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left


N, M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()
prev = 0
c_sum = [prev]
for v in b:
    c_sum.append(prev + v)
    prev += v

ans = 0
for v in a:
    t = find(v, b)
    ans += t * v - c_sum[t]
    ans += (c_sum[M] - c_sum[t]) - ((M - t) * v)

print(ans % 998244353)
