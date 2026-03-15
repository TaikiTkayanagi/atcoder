S = input()

memo = {}

for s in S:
    if s in memo:
        memo[s] += 1
    else:
        memo[s] = 1

max_value = max(memo.values())
exclude = []
for key in memo.keys():
    if max_value == memo[key]:
        exclude.append(key)

ans = ""
for s in S:
    if not s in exclude:
        ans += s

print(ans)
        
        
