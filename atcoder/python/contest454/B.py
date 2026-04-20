N, M = map(int, input().split())
F = list(map(int, input().split()))

memo = {}

for f in F:
    if f in memo:
        memo[f] = memo[f] + 1
    else:
        memo[f] = 1

is_1_ok = 'Yes'
for v in memo.values():
    if v > 1:
        is_1_ok = 'No'
        break
    
is_2_ok = 'Yes' if len(memo.keys()) == M else 'No'

print(is_1_ok)
print(is_2_ok)

