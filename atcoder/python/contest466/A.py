N = int(input())
X = list(map(int, input().split()))

count = 0
for x in X:
    if x < 0:
        count += 1

print('Yes' if count == N else "No")
        