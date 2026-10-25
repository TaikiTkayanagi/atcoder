N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i, a in enumerate(A):
    if i == len(A) - 1:
        break
    
    if K > a:
        if A[i+1] >= K:
            ans += 1 

    elif a > K:
        if A[i+1] <= K:
            ans += 1
    else:
        if i == 0:
            ans += 1

        if A[i+1] == K:
            ans += 1


print(ans)