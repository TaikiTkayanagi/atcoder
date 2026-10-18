N, K, T = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

p = T
ans = 0
for a in reversed(A):
    if a >= T:
        continue
    d = p - (a + K)

    if d > 0:
        tmp = d // K 
        if d % K != 0:
            tmp += 1
        ans += tmp
    
    p = a 

if T > A[0] and A[0] != 0:
    final_tmp = A[0] // K
    if A[0] % K != 0:
        final_tmp += 1
    ans += final_tmp
elif A[0] >= T:
    final_tmp = T // K
    if T % K != 0:
        final_tmp += 1
    ans += final_tmp

print(ans)