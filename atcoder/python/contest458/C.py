S = input()

ans = 0
for i, s in enumerate(S):
    if s != 'C':
        continue

    ans += min(i-0, len(S) - 1 - i) + 1

print(ans)