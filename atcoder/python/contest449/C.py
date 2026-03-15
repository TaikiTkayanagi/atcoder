N, L, R = map(int, input().split())
S = input()
memo = []
for i, s in enumerate(S):
    if i == 0:
        memo.append({s : 1})
        continue
    previous = memo[i - 1]
    if s in previous.keys():
        memo.append({**previous, s : previous[s] + 1}) 
    else:
        memo.append({**previous, s: 1})
        

    

ans = 0
for i in range(1, N):
    if i + L > N:
        break
    min = i + L
    last = i + R if N > i + R else N

    left = ""
    if S[i-1] in memo[min-2].keys():
        left = memo[min-2][S[i-1]]
    else:
        left = 0
    
    right = ""
    if S[i-1] in memo[last-1].keys():
        right = memo[last-1][S[i-1]]
    else:
        right = 0
    ans += right - left
        

print(ans)
        
    