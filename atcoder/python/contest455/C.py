N, K = map(int, input().split())
A = list(map(int, input().split()))

memo = {}
for a in A:
    if a in memo:
        memo[a] += 1
    else:
        memo[a] = 1

r = []
for key in memo.keys():
    r.append(key * memo[key])
        
r = sorted(r)
ans = 0
for i in range(len(r) - K):
    ans += r[i]
print(ans)
    
    
