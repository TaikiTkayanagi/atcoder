N, K = map(int, input().split())
A = list(map(int, input().split()))
Sample = sorted(A)

diff = N
for i in range(N):
    if A[i] != Sample[i]:
        diff = i
        break

last = min(N, diff+K)
new_A = sorted(A[diff:last])

is_ok = True
for i in range(N):
    if diff > i:
        continue
    if last > i: 
        if Sample[i] != new_A[i-diff]:
            is_ok = False
            break
        else:
            continue
    if Sample[i] != A[i]:
        is_ok = False
        break 

if is_ok:
    print('Yes')
else:
    print('No')