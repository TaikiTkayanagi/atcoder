import math

def is_ok(n, k, a, target):
    nk = 0
    for i in range(n):
        if a[i] >= target:
            continue
        nk += (target - a[i] + (i + 1) - 1) // (i + 1)
        if nk > k:
            return False
    return True

def is_ok_2(n, k, a, target):
    for i in range(n):
        if a[i] >= target:
            continue
        diff = target - a[i]
        necessary = math.ceil(diff / (i + 1))
        k -= necessary
        if k < 0:
            return False
    return True


    

N, K = map(int, input().split())
A = list(map(int, input().split()))
min_v = 0
max_v = 0
for i, a in enumerate(A):
    c = a + ((i+1) * K)
    if max_v == 0 or max_v > c:
        max_v = c + 1 

while max_v > min_v + 1:
    mid = (min_v + max_v) // 2
    if is_ok(N, K, A, mid):
        min_v = mid
    else:
        max_v = mid

print(min_v)