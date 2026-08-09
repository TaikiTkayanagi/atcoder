N = int(input())
C = list(map(int, input().split()))
cnt = [0] * N

for c in C:
    cnt[c] += 1

print(N - max(cnt))